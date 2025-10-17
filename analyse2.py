import streamlit as st
import pandas as pd
import plotly.express as px
from docx import Document
from docx.shared import Inches, RGBColor
import tempfile
import os
import warnings
from io import BytesIO
from dotenv import load_dotenv
import google.generativeai as genai

# Supprimer les warnings FutureWarning de pandas
warnings.filterwarnings('ignore', category=FutureWarning)

# Import configuration depuis le fichier de config principal
from config import translations

# Import configuration depuis le fichier de config principal
from config import translations

# Import du module de crédits
try:
    from credits import initialize_credits, add_credits_to_word_report
    CREDITS_AVAILABLE = True
except ImportError:
    CREDITS_AVAILABLE = False
    st.warning("⚠️ Module 'credits.py' non trouvé. Les crédits ne seront pas affichés.")

# Gestion de la clé API Gemini (optionnelle pour ne pas bloquer l'app)
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
GEMINI_AVAILABLE = False

if api_key:
    try:
        genai.configure(api_key=api_key)
        GEMINI_AVAILABLE = True
    except Exception:
        pass  # L'API Gemini ne sera simplement pas disponible


def dataframe_to_markdown(df: pd.DataFrame) -> str:
    """
    Convertit un DataFrame en format Markdown sans dépendance externe.
    
    Args:
        df (pd.DataFrame): DataFrame à convertir
        
    Returns:
        str: Représentation Markdown du DataFrame
    """
    # Créer les en-têtes
    headers = df.columns.tolist()
    markdown = "| " + " | ".join(str(h) for h in headers) + " |\n"
    markdown += "|" + "|".join(["---" for _ in headers]) + "|\n"
    
    # Ajouter les lignes
    for _, row in df.iterrows():
        markdown += "| " + " | ".join(str(v) for v in row.values) + " |\n"
    
    return markdown


def generate_gemini_interpretation(df_zero_scores: pd.DataFrame, t: dict) -> str:
    """
    Génère une interprétation éducative et des recommandations en utilisant l'API Gemini.
    
    Args:
        df_zero_scores (pd.DataFrame): DataFrame avec l'analyse des scores nuls
        t (dict): Dictionnaire de traductions
        
    Returns:
        str: Le texte de l'interprétation générée par l'IA, ou None si erreur
    """
    import time
    
    # Vérifier si l'API Gemini est disponible
    if not GEMINI_AVAILABLE:
        st.error("❌ **API Gemini non configurée**")
        st.info("""
        **Pour activer l'interprétation par IA, suivez ces étapes :**
        
        1. Créez un fichier `.env` à la racine de votre projet
        2. Ajoutez votre clé API Gemini dans ce fichier :
           ```
           GEMINI_API_KEY=votre_clé_api_ici
           ```
        3. Obtenez une clé API gratuite sur [Google AI Studio](https://aistudio.google.com)
        4. Redémarrez l'application
        
        **En attendant**, vous pouvez consulter les tableaux et graphiques ci-dessus qui fournissent déjà des informations détaillées sur les performances.
        """)
        return None
    
    # Convertir le DataFrame en Markdown (sans utiliser tabulate)
    df_for_markdown = df_zero_scores[[
        t.get("task_column", "Task"),
        t.get("count_column", "Count of Zeros"),
        t.get("percentage_column", "Percentage of Zero Scores")
    ]].copy()
    
    data_as_markdown = dataframe_to_markdown(df_for_markdown)
    
    # Template de prompt
    prompt_template = f"""**Contexte :** Vous êtes un expert de renommée internationale en sciences de l'éducation, spécialisé dans l'analyse des évaluations à grande échelle comme l'EGRA. Votre analyse doit être rigoureuse, basée sur des données probantes, et vos recommandations doivent être pratiques pour les enseignants.

**Données Brutes à Analyser :** Le tableau ci-dessous présente le pourcentage d'élèves ayant obtenu un score de zéro pour plusieurs tâches d'évaluation fondamentales. Un score de zéro représente une absence totale de la compétence mesurée.

```markdown
{data_as_markdown}
```

**Votre Mission :** Rédigez un rapport d'analyse diagnostique complet en français. Votre réponse doit impérativement être structurée en trois sections distinctes au format Markdown.

## 1. Interprétation Pédagogique

**Résumé (Summary) :** Commencez par une synthèse de 2-3 phrases sur l'état général des compétences, en identifiant les domaines de force et de faiblesse critiques.

**Zones Préoccupantes (Concerning Areas) :** Identifiez les compétences les plus alarmantes (celles avec les pourcentages les plus élevés). Expliquez en détail pourquoi ces déficits sont critiques pour le développement futur de l'élève. Créez des liens de causalité entre les compétences.

**Points de Stabilité :** Mentionnez brièvement les compétences qui semblent acquises (celles avec les pourcentages les plus bas).

## 2. Recommandations Actionnables

**Recommandations Prioritaires :** Proposez des stratégies d'intervention très concrètes et ciblées pour les compétences les plus faibles.

**Stratégies de Mise en Œuvre :** Donnez des conseils sur la manière d'intégrer ces recommandations (différenciation, petits groupes, etc.).

**Recommandations d'Évaluation :** Suggérez un plan de suivi pour mesurer les progrès.

## 3. Sources et Références Fiables

Pour crédibiliser votre analyse, citez au moins deux sources académiques ou institutionnelles reconnues qui soutiennent vos recommandations. Listez-les clairement à la fin."""
    
    # Configuration du retry
    max_retries = 3
    retry_delay = 20  # secondes
    
    for attempt in range(max_retries):
        try:
            if attempt > 0:
                st.info(f"⏳ Nouvelle tentative ({attempt + 1}/{max_retries}) dans {retry_delay} secondes...")
                time.sleep(retry_delay)
            
            with st.spinner("🤖 L'IA analyse les résultats..."):
                model = genai.GenerativeModel('gemini-1.5-pro-latest')
                response = model.generate_content(prompt_template)
                
                # Afficher l'interprétation
                st.subheader(t.get("interpretation_title", "🔍 Educational Interpretation"))
                st.markdown(response.text)
                
                # Retourner le texte pour l'utiliser dans le rapport Word
                return response.text
                
        except Exception as e:
            error_message = str(e)
            
            # Détecter spécifiquement l'erreur 429 (quota dépassé)
            if "429" in error_message or "quota" in error_message.lower():
                if attempt < max_retries - 1:
                    st.warning(f"⚠️ Limite de quota API atteinte. Nouvelle tentative automatique dans {retry_delay} secondes...")
                    retry_delay *= 2  # Backoff exponentiel
                else:
                    st.error("❌ **Quota API Gemini dépassé**")
                    st.info("""
                    **Solutions possibles :**
                    1. 🕐 Attendez quelques minutes avant de réessayer
                    2. 🔑 Vérifiez votre plan API Gemini sur [Google AI Studio](https://aistudio.google.com)
                    3. 💳 Considérez passer à un plan payant pour des quotas plus élevés
                    4. 📊 Pour le moment, vous pouvez consulter les tableaux et graphiques ci-dessus
                    
                    **Limites du niveau gratuit :**
                    - 2 requêtes par minute
                    - 1 500 requêtes par jour
                    
                    [En savoir plus sur les quotas](https://ai.google.dev/gemini-api/docs/rate-limits)
                    """)
                    return None
            else:
                # Autre type d'erreur
                st.error(f"❌ Erreur lors de l'appel à l'API Gemini: {error_message}")
                if attempt < max_retries - 1:
                    st.warning(f"⏳ Nouvelle tentative dans {retry_delay} secondes...")
                else:
                    st.info("""
                    **Vérifications suggérées :**
                    - ✅ Votre clé API est correcte dans le fichier `.env`
                    - ✅ Vous avez une connexion internet active
                    - ✅ L'API Gemini est accessible depuis votre région
                    """)
                    return None
    
    return None


def create_complete_word_report(df_zero_scores: pd.DataFrame, fig, t: dict, ai_interpretation: str = None, language: str = "en") -> Document:
    """
    Crée un rapport Word COMPLET avec tableaux, graphiques ET interprétation IA.
    
    Args:
        df_zero_scores (pd.DataFrame): DataFrame avec l'analyse des scores nuls
        fig: Figure Plotly du graphique
        t (dict): Dictionnaire de traductions
        ai_interpretation (str): Texte de l'interprétation IA (optionnel)
        
    Returns:
        Document: Document Word complet
    """
    from datetime import datetime
    
    doc = Document()
    
    # ========== PAGE DE GARDE ==========
    doc.add_heading(t.get("title_zero_scores", "Zero Scores Analysis"), level=1)
    
    # Date et heure du rapport
    date_str = datetime.now().strftime("%d/%m/%Y %H:%M")
    doc.add_paragraph(f"📅 {t.get('report_date', 'Date du rapport')}: {date_str}")
    doc.add_paragraph("_" * 50)
    doc.add_paragraph()
    
    # ========== RÉSUMÉ EXÉCUTIF ==========
    doc.add_heading(t.get("executive_summary", "Résumé Exécutif"), level=2)
    
    # Calculer les statistiques globales
    total_tasks = len(df_zero_scores)
    avg_percentage = df_zero_scores[t.get("percentage_column", "Percentage of Zero Scores")].mean()
    critical_count = len(df_zero_scores[df_zero_scores[t.get("percentage_column", "Percentage of Zero Scores")] >= 30])
    concerning_count = len(df_zero_scores[
        (df_zero_scores[t.get("percentage_column", "Percentage of Zero Scores")] >= 20) &
        (df_zero_scores[t.get("percentage_column", "Percentage of Zero Scores")] < 30)
    ])
    
    summary_text = f"""
Ce rapport analyse les scores nuls (zéro) obtenus par les élèves sur {total_tasks} tâches d'évaluation.

Statistiques clés :
• Pourcentage moyen de scores nuls : {avg_percentage:.1f}%
• Tâches critiques (>30% de zéros) : {critical_count}
• Tâches préoccupantes (20-30% de zéros) : {concerning_count}

Un score de zéro indique une absence totale de maîtrise de la compétence évaluée et nécessite une attention particulière.
    """
    doc.add_paragraph(summary_text)
    doc.add_paragraph()
    
    # ========== TABLEAU DES RÉSULTATS ==========
    doc.add_heading(t.get("table_zero_scores", "Proportion of Students with Zero Scores"), level=2)
    
    # Créer le tableau
    table = doc.add_table(rows=1, cols=3)
    table.style = 'Light Grid Accent 1'
    
    # En-têtes
    header_cells = table.rows[0].cells
    header_cells[0].text = t.get("task_column", "Task")
    header_cells[1].text = t.get("count_column", "Count of Zeros")
    header_cells[2].text = t.get("percentage_column", "Percentage of Zero Scores")
    
    # Rendre les en-têtes en gras
    for cell in header_cells:
        for paragraph in cell.paragraphs:
            for run in paragraph.runs:
                run.font.bold = True
    
    # Ajouter les données
    for _, row in df_zero_scores.iterrows():
        row_cells = table.add_row().cells
        row_cells[0].text = str(row[t.get("task_column", "Task")])
        row_cells[1].text = str(row[t.get("count_column", "Count of Zeros")])
        percentage_val = row[t.get("percentage_column", "Percentage of Zero Scores")]
        row_cells[2].text = f"{percentage_val}%"
        
        # Colorer selon le seuil en utilisant RGBColor
        if percentage_val >= 30:
            # Rouge
            row_cells[2].paragraphs[0].runs[0].font.color.rgb = RGBColor(220, 20, 60)
        elif percentage_val >= 20:
            # Orange
            row_cells[2].paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 140, 0)
    
    doc.add_paragraph()
    
    # ========== GRAPHIQUE ==========
    doc.add_heading(t.get("visualization_title", "Visualisation"), level=2)
    
    # Exporter le graphique en image
    with tempfile.TemporaryDirectory() as tmp_dir:
        img_path = os.path.join(tmp_dir, "zero_scores_chart.png")
        try:
            fig.write_image(img_path, width=1200, height=600)
            doc.add_picture(img_path, width=Inches(6.5))
        except Exception as e:
            doc.add_paragraph(f"[Graphique non disponible: {str(e)}]")
    
    doc.add_paragraph()
    
    # ========== INTERPRÉTATION IA (si disponible) ==========
    if ai_interpretation:
        doc.add_heading(t.get("interpretation_title", "Interprétation Pédagogique par IA"), level=2)
        doc.add_paragraph("🤖 Cette interprétation a été générée par intelligence artificielle (Gemini)")
        doc.add_paragraph("_" * 50)
        
        # Ajouter l'interprétation IA (en préservant le formatage Markdown basique)
        for line in ai_interpretation.split('\n'):
            if line.strip().startswith('##'):
                # Titre de niveau 2
                doc.add_heading(line.replace('##', '').strip(), level=3)
            elif line.strip().startswith('**') and line.strip().endswith('**'):
                # Texte en gras
                p = doc.add_paragraph()
                p.add_run(line.strip().replace('**', '')).bold = True
            elif line.strip().startswith('- ') or line.strip().startswith('* '):
                # Liste à puces
                doc.add_paragraph(line.strip()[2:], style='List Bullet')
            elif line.strip():
                # Paragraphe normal
                doc.add_paragraph(line.strip())
        
        doc.add_paragraph()
    else:
        # ========== RECOMMANDATIONS DE BASE (si pas d'IA) ==========
        doc.add_heading(t.get("recommendations_title", "Recommandations"), level=2)
        
        # Catégoriser les tâches
        critical_tasks = df_zero_scores[
            df_zero_scores[t.get("percentage_column", "Percentage of Zero Scores")] >= 30
        ]
        concerning_tasks = df_zero_scores[
            (df_zero_scores[t.get("percentage_column", "Percentage of Zero Scores")] >= 20) &
            (df_zero_scores[t.get("percentage_column", "Percentage of Zero Scores")] < 30)
        ]
        
        if len(critical_tasks) > 0:
            doc.add_heading("🔴 Zones Critiques (>30% de scores nuls)", level=3)
            doc.add_paragraph(
                "Ces compétences nécessitent une intervention immédiate avec des programmes "
                "d'enseignement intensif et ciblé."
            )
            for _, task in critical_tasks.iterrows():
                doc.add_paragraph(
                    f"• {task[t.get('task_column', 'Task')]}: {task[t.get('percentage_column', 'Percentage')]}%",
                    style='List Bullet'
                )
        
        if len(concerning_tasks) > 0:
            doc.add_heading("🟠 Zones Préoccupantes (20-30% de scores nuls)", level=3)
            doc.add_paragraph(
                "Ces compétences nécessitent un renforcement significatif dans le cadre "
                "de l'enseignement régulier."
            )
            for _, task in concerning_tasks.iterrows():
                doc.add_paragraph(
                    f"• {task[t.get('task_column', 'Task')]}: {task[t.get('percentage_column', 'Percentage')]}%",
                    style='List Bullet'
                )
        
        doc.add_paragraph()
        doc.add_heading("Stratégies d'Intervention Générales", level=3)
        doc.add_paragraph("1. Enseignement différencié en petits groupes", style='List Number')
        doc.add_paragraph("2. Évaluation diagnostique approfondie pour identifier les lacunes spécifiques", style='List Number')
        doc.add_paragraph("3. Intervention précoce et intensive pour les élèves en difficulté", style='List Number')
        doc.add_paragraph("4. Suivi régulier des progrès (toutes les 2-3 semaines)", style='List Number')
        doc.add_paragraph("5. Collaboration avec les familles pour le soutien à domicile", style='List Number')
    
    # ========== NOTES MÉTHODOLOGIQUES ==========
    doc.add_page_break()
    doc.add_heading("Notes Méthodologiques", level=2)
    
    methodology_text = """
Ce rapport analyse les scores nuls (zéro) dans les évaluations EGRA/EGMA selon les critères suivants :

Seuils d'Interprétation :
• Acceptable : < 10% de scores nuls
• À surveiller : 10-20% de scores nuls
• Préoccupant : 20-30% de scores nuls
• Critique : > 30% de scores nuls

Un pourcentage élevé de scores nuls indique que de nombreux élèves n'ont pas acquis les compétences 
fondamentales évaluées. Ces lacunes peuvent compromettre les apprentissages futurs et nécessitent 
une attention immédiate.

Les recommandations sont basées sur les meilleures pratiques en matière d'enseignement de la lecture 
et des mathématiques au primaire, telles que documentées par la recherche en sciences de l'éducation.
    """
    doc.add_paragraph(methodology_text)
    
    # ========== PIED DE PAGE ==========
    doc.add_paragraph()
    doc.add_paragraph("_" * 50)
    footer_text = f"Rapport généré par Datavizir Analytics - {date_str}"
    p = doc.add_paragraph(footer_text)
    p.alignment = 1  # Centre
    
    # ========== AJOUTER LES CRÉDITS ==========
    if CREDITS_AVAILABLE:
        doc = add_credits_to_word_report(doc)
    
    return doc
    """
    Crée un rapport Word avec l'analyse des scores nuls et des recommandations.
    
    Args:
        df_zero_scores (pd.DataFrame): DataFrame avec l'analyse des scores nuls
        t (dict): Dictionnaire de traductions
        
    Returns:
        Document: Document Word avec le rapport
    """
    doc = Document()
    
    # Titre principal
    doc.add_heading(t.get("title_zero_scores", "Zero Scores Analysis"), level=1)
    
    # Section résumé des données
    doc.add_heading(t.get("table_zero_scores", "Proportion of Students with Zero Scores"), level=2)
    
    # Créer un tableau pour les données des scores nuls
    table = doc.add_table(rows=1, cols=3)
    table.style = 'Table Grid'
    
    # Ajouter les en-têtes
    header_cells = table.rows[0].cells
    header_cells[0].text = t.get("task_column", "Task")
    header_cells[1].text = t.get("count_column", "Count of Zeros")
    header_cells[2].text = t.get("percentage_column", "Percentage of Zero Scores")
    
    # Ajouter les lignes
    for _, row in df_zero_scores.iterrows():
        row_cells = table.add_row().cells
        row_cells[0].text = row[t.get("task_column", "Task")]
        row_cells[1].text = str(row[t.get("count_column", "Count of Zeros")])
        row_cells[2].text = f"{row[t.get('percentage_column', 'Percentage of Zero Scores')]}%"
    
    # Créer des catégories pour l'interprétation
    categories = {
        "critical": {"tasks": [], "threshold": 30},
        "concerning": {"tasks": [], "threshold": 20},
        "monitor": {"tasks": [], "threshold": 10},
        "acceptable": {"tasks": [], "threshold": 0}
    }
    
    # Catégoriser les tâches selon les pourcentages de scores nuls
    for _, row in df_zero_scores.iterrows():
        percentage = row[t.get("percentage_column", "Percentage of Zero Scores")]
        task_name = row[t.get("task_column", "Task")]
        task_code = row.get("Task_Code", "")
        task_info = {"name": task_name, "code": task_code, "percentage": percentage}
        
        if percentage >= categories["critical"]["threshold"]:
            categories["critical"]["tasks"].append(task_info)
        elif percentage >= categories["concerning"]["threshold"]:
            categories["concerning"]["tasks"].append(task_info)
        elif percentage >= categories["monitor"]["threshold"]:
            categories["monitor"]["tasks"].append(task_info)
        else:
            categories["acceptable"]["tasks"].append(task_info)
    
    # Ajouter la section d'interprétation
    doc.add_heading(t.get("interpretation_title", "Educational Interpretation"), level=2)
    
    # Ajouter un paragraphe de résumé
    if categories["critical"]["tasks"]:
        summary_status = t.get("critical_status", "Critical areas requiring immediate intervention")
    elif categories["concerning"]["tasks"]:
        summary_status = t.get("concerning_status", "Areas of concern requiring attention")
    elif categories["monitor"]["tasks"]:
        summary_status = t.get("monitor_status", "Some skills need monitoring")
    else:
        summary_status = t.get("acceptable_status", "All skills are at acceptable levels")
    
    doc.add_paragraph(summary_status, style='Intense Quote')
    
    # Ajouter les résultats détaillés
    if categories["critical"]["tasks"] or categories["concerning"]["tasks"]:
        doc.add_paragraph(t.get("findings_text", "Analysis shows significant learning gaps in key reading skills:"))
        
        # Détailler les zones critiques
        if categories["critical"]["tasks"]:
            doc.add_heading(t.get("critical_areas", "Critical Areas (>{}% zero scores)").format(
                           categories["critical"]["threshold"]), level=3)
            for task in categories["critical"]["tasks"]:
                doc.add_paragraph(f"{task['name']}: {task['percentage']}% " +
                                 t.get("zero_score_text", "of students scored zero"), style='List Bullet')
        
        # Détailler les zones préoccupantes
        if categories["concerning"]["tasks"]:
            doc.add_heading(t.get("concerning_areas", "Concerning Areas (>{}% zero scores)").format(
                           categories["concerning"]["threshold"]), level=3)
            for task in categories["concerning"]["tasks"]:
                doc.add_paragraph(f"{task['name']}: {task['percentage']}% " +
                                 t.get("zero_score_text", "of students scored zero"), style='List Bullet')
    
    # Section recommandations
    doc.add_heading(t.get("recommendations_title", "Recommendations"), level=2)
    doc.add_paragraph("Consultez le rapport d'interprétation généré par l'IA pour des recommandations détaillées et personnalisées.")
    
    return doc


def show_zero_scores(df: pd.DataFrame, language: str) -> None:
    """
    Analyse et affiche la proportion de scores nuls pour les tâches d'évaluation EGRA/EGMA.
    
    Args:
        df (pd.DataFrame): Les données à analyser
        language (str): Langue sélectionnée pour les éléments de l'interface (en/fr/ar/es)
    """
    t = translations[language]
    
    # Initialiser les crédits dans la sidebar (avec langue dynamique)
    if CREDITS_AVAILABLE:
        initialize_credits(location="sidebar", language=language)
    
    # Initialiser session_state pour l'interprétation et le graphique
    if 'show_interpretation' not in st.session_state:
        st.session_state.show_interpretation = False
    if 'ai_interpretation_text' not in st.session_state:
        st.session_state.ai_interpretation_text = None
    if 'zero_scores_fig' not in st.session_state:
        st.session_state.zero_scores_fig = None
    
    # Définir les listes de colonnes EGRA et EGMA
    egra_columns = ["clpm", "phoneme", "sound_word", "cwpm", "listening", "orf", "comprehension"]
    egma_columns = ["number_id", "discrimin", "missing_number", "addition", "subtraction", "problems"]
    
    # Vérifier que le DataFrame contient au moins certaines des colonnes requises
    available_columns = [col for col in egra_columns + egma_columns if col in df.columns]
    
    if not available_columns:
        st.error(t.get("no_assessment_columns", "No assessment columns found in the data."))
        return
    
    # Sélecteurs de variables
    st.subheader(t.get("select_variables", "📊 Select Variables"))
    
    # Multiselect pour EGRA
    available_egra = [col for col in egra_columns if col in df.columns]
    selected_egra = st.multiselect(
        t.get("egra_variables", "EGRA Variables:"),
        options=available_egra,
        default=available_egra[:3] if len(available_egra) > 3 else available_egra,
        format_func=lambda x: t["columns_of_interest"].get(x, x)
    )
    
    # Multiselect pour EGMA
    available_egma = [col for col in egma_columns if col in df.columns]
    selected_egma = st.multiselect(
        t.get("egma_variables", "EGMA Variables:"),
        options=available_egma,
        default=available_egma[:3] if len(available_egma) > 3 else available_egma,
        format_func=lambda x: t["columns_of_interest"].get(x, x)
    )
    
    # Combiner les variables sélectionnées
    selected_columns = selected_egra + selected_egma
    
    if selected_columns:
        try:
            # Calculer les scores nuls
            zero_scores = (df[selected_columns] == 0).sum()
            total_students = len(df)
            percentage_zero = ((zero_scores / total_students) * 100).round(2)
            
            # Créer un DataFrame pour l'affichage et la visualisation
            df_zero_scores = pd.DataFrame({
                "Task": [t.get("columns_of_interest", {}).get(col, col) for col in selected_columns],
                "Zero_Count": zero_scores.values,
                "Percentage": percentage_zero.values,
                "Task_Code": selected_columns
            })
            
            # Tableau des résultats
            st.subheader(t.get("table_zero_scores", "📋 Proportion of Students with Zero Scores"))
            styled_df = df_zero_scores.copy()
            styled_df.columns = [
                t.get("task_column", "Task"), 
                t.get("count_column", "Count of Zeros"),
                t.get("percentage_column", "Percentage of Zero Scores"),
                "Task_Code"
            ]
            st.dataframe(styled_df[styled_df.columns[:-1]], use_container_width=True)
            
            # Graphique de visualisation (AVANT les boutons)
            st.subheader(t.get("zero_scores_chart_title", "📊 Percentage of Students with Zero Scores by Task"))
            try:
                # Préparer les données pour le graphique
                df_zero_scores_sorted = df_zero_scores.sort_values("Percentage", ascending=True).copy()
                
                # S'assurer que les colonnes sont du bon type
                df_zero_scores_sorted["Percentage"] = pd.to_numeric(df_zero_scores_sorted["Percentage"], errors='coerce')
                df_zero_scores_sorted["Task"] = df_zero_scores_sorted["Task"].astype(str)
                
                fig = px.bar(
                    df_zero_scores_sorted,
                    x="Percentage",
                    y="Task",
                    orientation="h",
                    text="Percentage",
                    color="Percentage",
                    color_continuous_scale="Viridis",
                    title=t.get("zero_scores_chart_title", "Percentage of Students with Zero Scores by Task")
                )
                
                # Personnaliser l'affichage du texte
                fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
                
                # Seuils critiques avec indication de couleur
                fig.add_vline(x=10, line_width=2, line_dash="dash", line_color="yellow", opacity=0.7)
                fig.add_vline(x=20, line_width=2, line_dash="dash", line_color="orange", opacity=0.7)
                fig.add_vline(x=30, line_width=2, line_dash="dash", line_color="red", opacity=0.7)
                
                # Annotations pour les seuils
                fig.add_annotation(
                    x=10, y=0,
                    text=t.get("acceptable_threshold", "Acceptable"),
                    showarrow=False,
                    yshift=-20,
                    font=dict(size=10, color="yellow")
                )
                fig.add_annotation(
                    x=20, y=0,
                    text=t.get("concerning_threshold", "Concerning"),
                    showarrow=False,
                    yshift=-20,
                    font=dict(size=10, color="orange")
                )
                fig.add_annotation(
                    x=30, y=0,
                    text=t.get("critical_threshold", "Critical"),
                    showarrow=False,
                    yshift=-20,
                    font=dict(size=10, color="red")
                )
                
                # Mise en page améliorée
                fig.update_layout(
                    height=400,
                    xaxis_title=t.get("percentage_column", "Percentage of Zero Scores"),
                    yaxis_title=t.get("task_column", "Task"),
                    showlegend=False
                )
                
                # Stocker le graphique dans session_state pour l'export Word
                st.session_state.zero_scores_fig = fig
                
                st.plotly_chart(fig, use_container_width=True)
            except Exception as e:
                st.error(f"Error creating visualization: {str(e)}")
            
            # Séparateur visuel
            st.divider()
            
            # Section Actions - 2 boutons côte à côte EN BAS
            st.subheader(t.get("actions_section", "📊 Actions et Exports"))
            
            # Message d'aide
            st.info("""
            **💡 Guide d'utilisation :**
            - **🔍 Interprétation IA** : Générez une analyse pédagogique détaillée avec recommandations (nécessite API Gemini)
            - **📄 Rapport Complet** : Créez un document Word professionnel incluant tableaux, graphiques et interprétation IA
            """)
            
            col_btn1, col_btn2 = st.columns(2)
            
            # Bouton 1 : Génération de l'interprétation IA
            with col_btn1:
                if GEMINI_AVAILABLE:
                    if st.button(
                        "🔍 " + t.get("generate_interpretation", "Générer l'Interprétation IA"),
                        type="primary",
                        use_container_width=True
                    ):
                        st.session_state.show_interpretation = True
                        # Générer et stocker l'interprétation
                        with st.spinner("🤖 Génération de l'interprétation..."):
                            ai_text = generate_gemini_interpretation(styled_df, t)
                            st.session_state.ai_interpretation_text = ai_text
                else:
                    st.button(
                        "🔍 " + t.get("generate_interpretation", "Générer l'Interprétation IA") + " 🔒",
                        disabled=True,
                        use_container_width=True,
                        help="Configurez votre clé API Gemini dans le fichier .env pour activer cette fonctionnalité"
                    )
            
            # Bouton 2 : Export Rapport Complet Word
            with col_btn2:
                if st.button(
                    "📄 " + t.get("export_complete_report", "Générer Rapport Complet (Word)"),
                    use_container_width=True
                ):
                    try:
                        # S'assurer que le graphique est disponible
                        if st.session_state.zero_scores_fig is not None:
                            with st.spinner("📝 Génération du rapport complet..."):
                                # Créer le rapport complet avec graphique et IA
                                doc = create_complete_word_report(
                                    styled_df,
                                    st.session_state.zero_scores_fig,
                                    t,
                                    st.session_state.ai_interpretation_text,
                                    language=language  # Passer la langue
                                )
                                
                                # Sauvegarder et télécharger
                                with tempfile.NamedTemporaryFile(delete=False, suffix='.docx') as tmp:
                                    doc.save(tmp.name)
                                    with open(tmp.name, 'rb') as f:
                                        docx_data = f.read()
                                    
                                    st.download_button(
                                        "📥 " + t.get("download_complete_report", "Télécharger le rapport"),
                                        docx_data,
                                        "rapport_complet_zero_scores.docx",
                                        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                                        key='download-complete-report',
                                        use_container_width=True
                                    )
                            st.success("✅ " + t.get("report_ready", "Rapport généré avec succès!"))
                        else:
                            st.warning("⚠️ " + t.get("wait_for_graph", "Veuillez patienter, le graphique se charge..."))
                    except Exception as e:
                        st.error(f"❌ Erreur lors de la génération du rapport: {str(e)}")
                        import traceback
                        st.error(traceback.format_exc())
            
            # Section d'interprétation IA (affichée après les boutons si générée)
            if st.session_state.show_interpretation and st.session_state.ai_interpretation_text:
                st.divider()
                # L'interprétation a déjà été affichée lors de la génération via generate_gemini_interpretation()
            
        except Exception as e:
            st.error(f"Error in zero scores analysis: {str(e)}")
    
    else:
        st.warning(t.get("warning_select_task", "Please select at least one task to analyze."))
    
    # Afficher le footer avec les crédits (avec langue dynamique)
    #if CREDITS_AVAILABLE:
    #    initialize_credits(location="footer", language=language)