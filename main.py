# main.py
import streamlit as st
import pandas as pd
import base64
import os
import sys
import traceback
from pathlib import Path
from io import BytesIO

# Import configuration and utility modules
from config import translations
from language_utils import setup_language_selector, get_text
from validation_utils import DataValidator, ErrorHandler
try:
    from credits import initialize_credits, add_credits_to_word_report
    CREDITS_AVAILABLE = True
except ImportError:
    CREDITS_AVAILABLE = False
    st.warning("⚠️ Module 'credits.py' non trouvé. Les crédits ne seront pas affichés.")
# Import only the analysis modules that exist in the repository
from analyse1 import show_statistical_overview
from analyse2 import show_zero_scores
from analyse5 import show_correlation
from analyse6 import show_reliability
from analyse7 import show_performance_school
from analyse10 import show_gender_effect
from analyse12 import show_international_comparison
from analyse13 import show_language_comparison

# Set page configuration
st.set_page_config(
    page_title="Datavizir Analytics",
    page_icon="📊",
    layout="wide"
)


def generate_template_excel():
    """
    Generate the template Excel file with the required structure.
    Returns bytes of the Excel file.
    """
    # Define the template columns
    columns = [
        "pupil_id", "school", "stgender", "clpm", "phoneme", "sound_word", 
        "cwpm", "listening", "orf", "comprehension", "number_id", "discrimin",
        "missing_number", "addition", "subtraction", "problems", 
        "child_reaction1", "child_reaction2", "child_reaction3",
        "st_age", "st_english_home", "st_dutch_home", "st_other_language",
        "st_other_txt", "st_daycare", "st_earlystimulation_classes",
        "st_attend_gr1gr2", "st_nb_miss_school", "st_nb_beenlate_school",
        "ses", "home_support", "language_teaching"
    ]
    
    # Create empty DataFrame with these columns
    df_template = pd.DataFrame(columns=columns)
    
    # Convert to Excel bytes
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df_template.to_excel(writer, index=False, sheet_name='Feuil1')
    
    return output.getvalue()


def show_template_section():
    """
    Display the template description section with download button.
    """
    language = st.session_state.get('language', 'en')
    t = translations[language]
    
    # Description texts for different languages
    descriptions = {
        'fr': """
        ### 📋 Guide d'utilisation de l'application
        
        Cette application d'analyse éducative (EGRA/EGMA) vous permet d'analyser les données d'évaluation 
        des élèves à travers plusieurs dimensions : performances, corrélations, fiabilité, comparaisons 
        internationales et linguistiques.
        
        **Pour utiliser cette application, vous devez :**
        1. Télécharger le template Excel ci-dessous
        2. Remplir le template avec vos données en respectant exactement la structure des colonnes
        3. Charger votre fichier complété via le menu latéral
        
        ⚠️ **Important :** Le fichier doit strictement suivre le format du template pour fonctionner correctement.
        """,
        'en': """
        ### 📋 Application User Guide
        
        This educational assessment analytics application (EGRA/EGMA) allows you to analyze student 
        evaluation data across multiple dimensions: performance, correlations, reliability, international 
        and language comparisons.
        
        **To use this application, you must:**
        1. Download the Excel template below
        2. Fill the template with your data while strictly respecting the column structure
        3. Upload your completed file via the sidebar menu
        
        ⚠️ **Important:** The file must strictly follow the template format to work correctly.
        """,
        'ar': """
		### 📋 دليل استخدام التطبيق

		يتيح لك هذا التطبيق لتحليل التقييم التعليمي (EGRA/EGMA) تحليل بيانات تقييم الطلاب 
		عبر أبعاد متعددة: الأداء، الارتباطات، الموثوقية، المقارنات الدولية واللغوية.

		**لاستخدام هذا التطبيق، يجب عليك:**
		1. تنزيل قالب Excel أدناه
		2. ملء القالب بياناتك مع احترام بنية الأعمدة بدقة
		3. تحميل ملفك المكتمل عبر القائمة الجانبية

		⚠️ **مهم:** يجب أن يتبع الملف بدقة تنسيق القالب ليعمل بشكل صحيح.
		""",
        'es': """
        ### 📋 Guía de uso de la aplicación
        
        Esta aplicación de análisis educativo (EGRA/EGMA) le permite analizar datos de evaluación 
        de estudiantes a través de múltiples dimensiones: rendimiento, correlaciones, confiabilidad, 
        comparaciones internacionales y lingüísticas.
        
        **Para usar esta aplicación, debe:**
        1. Descargar la plantilla Excel a continuación
        2. Completar la plantilla con sus datos respetando exactamente la estructura de columnas
        3. Cargar su archivo completado mediante el menú lateral
        
        ⚠️ **Importante:** El archivo debe seguir estrictamente el formato de la plantilla para funcionar correctamente.
        """
    }
    
    # Display description
    description = descriptions.get(language, descriptions['en'])
    st.markdown(description)
    
    # Generate template
    template_bytes = generate_template_excel()
    
    # Create columns for layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("#### 📊 Structure du Template / Template Structure")
        
        # Display template structure as a table
        columns_info = {
            "Colonne / Column": [
                "pupil_id", "school", "stgender", "clpm", "phoneme", "sound_word",
                "cwpm", "listening", "orf", "comprehension", "number_id", "discrimin",
                "missing_number", "addition", "subtraction", "problems",
                "child_reaction1", "child_reaction2", "child_reaction3",
                "st_age", "st_english_home", "st_dutch_home", "st_other_language",
                "st_other_txt", "st_daycare", "st_earlystimulation_classes",
                "st_attend_gr1gr2", "st_nb_miss_school", "st_nb_beenlate_school",
                "ses", "home_support", "language_teaching"
            ],
            "Type": ["ID", "Categorical", "Categorical"] + ["Numeric"] * 29
        }
        
        df_display = pd.DataFrame(columns_info)
        st.dataframe(df_display, use_container_width=True, height=400)
    
    with col2:
        st.markdown("#### ⬇️ Télécharger / Download")
        
        # Download button
        button_text = {
            'fr': "📥 Télécharger le Template Excel",
            'en': "📥 Download Excel Template",
            'es': "📥 Descargar Plantilla Excel"
        }
        
        st.download_button(
            label=button_text.get(language, button_text['en']),
            data=template_bytes,
            file_name="EGRA_EGMA_template_datavizir.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            help="Téléchargez ce template et remplissez-le avec vos données"
        )
        
        # Additional info
        info_text = {
            'fr': """
            **Colonnes principales :**
            - **pupil_id** : Identifiant unique
            - **school** : École
            - **stgender** : Genre
            - **clpm, phoneme, sound_word...** : Scores d'évaluation
            - **st_age, ses...** : Variables démographiques
            """,
            'en': """
            **Main columns:**
            - **pupil_id** : Unique identifier
            - **school** : School
            - **stgender** : Gender
            - **clpm, phoneme, sound_word...** : Assessment scores
            - **st_age, ses...** : Demographic variables
            """,
            'ar': """
			**الأعمدة الرئيسية:**
			- **pupil_id** : المعرف الفريد
			- **school** : المدرسة
			- **stgender** : الجنس
			- **clpm, phoneme, sound_word...** : درجات التقييم
			- **st_age, ses...** : المتغيرات الديموغرافية
			""",
            'es': """
            **Columnas principales:**
            - **pupil_id** : Identificador único
            - **school** : Escuela
            - **stgender** : Género
            - **clpm, phoneme, sound_word...** : Puntuaciones de evaluación
            - **st_age, ses...** : Variables demográficas
            """
        }
        
        st.info(info_text.get(language, info_text['en']))
    
    st.divider()


def load_data():
    """
    Loads data from various file formats (Excel, JSON, CSV, Stata DTA).
    Returns:
        pandas.DataFrame or None: The loaded DataFrame or None if error
    """
    # Initialize error handler
    error_handler = ErrorHandler(language=st.session_state.get('language', 'en'))

    try:
        # Supported formats
        supported_formats = {
            "xlsx": "Excel",
            "xls": "Excel",
            "json": "JSON",
            "csv": "CSV",
            "dta": "Stata"
        }

        # Load translations
        language = st.session_state.get('language', 'en')
        t = translations[language]

        # File uploader in sidebar
        uploaded_file = st.sidebar.file_uploader(
            t["upload_file"],
            type=list(supported_formats.keys()),
            help=t["upload_help"]
        )

        if uploaded_file is None:
            st.sidebar.info(t["upload_info"])
            return None

        # Wrap all loaded-data UI in a sidebar expander
        exp = st.sidebar.expander(
            t.get("loaded_data_section", "Données chargées"),
            expanded=True
        )
        with exp:
            # Determine file extension
            ext = uploaded_file.name.split('.')[-1].lower()

            # Loading spinner
            with st.spinner(t["loading_data"]):
                if ext in ("xlsx", "xls"):
                    xls = pd.ExcelFile(uploaded_file)
                    sheet = (
                        xls.sheet_names[0]
                        if len(xls.sheet_names) == 1
                        else st.selectbox(t["select_sheet"], xls.sheet_names)
                    )
                    df = pd.read_excel(uploaded_file, sheet_name=sheet)

                elif ext == "json":
                    try:
                        df = pd.read_json(uploaded_file)
                    except ValueError:
                        df = pd.read_json(uploaded_file, orient="records")

                elif ext == "csv":
                    encodings = ["utf-8", "latin1", "iso-8859-1", "cp1252"]
                    separators = [",", ";", "\t", "|"]
                    col1, col2 = st.columns(2)
                    with col1:
                        encoding = st.selectbox(t["select_encoding"], encodings)
                    with col2:
                        separator = st.selectbox(t["select_separator"], separators)
                    df = pd.read_csv(uploaded_file, encoding=encoding, sep=separator, engine="python")

                else:  # dta
                    df = pd.read_stata(uploaded_file)

            # Validate dataframe
            validator = DataValidator(language=language)
            validation = validator.validate_dataframe(df, analysis_type="general")
            for warning in validation.warnings:
                st.warning(warning)

            # Success message
            st.success(f"{t['upload_success']} {uploaded_file.name}")
            st.write(f"{t.get('rows_count', 'Rows')}: {df.shape[0]}")
            st.write(f"{t.get('columns_count', 'Columns')}: {df.shape[1]}")

            # Data preview
            if st.checkbox(t.get("show_preview", "Afficher un aperçu")):
                st.dataframe(df.head(), use_container_width=True)

            # Column data types
            if st.checkbox(t.get("show_dtypes", "Types de colonnes")):
                st.write(df.dtypes)

            # Missing values analysis
            if st.checkbox(t.get("show_missing_values", "Analyse des valeurs manquantes")):
                missing_report = validator.get_missing_value_report(df)
                st.dataframe(missing_report)

                if st.checkbox(t.get("visualize_missing", "Visualiser les valeurs manquantes")):
                    missing_fig = validator.plot_missing_values(df)
                    st.pyplot(missing_fig)

                if st.checkbox(t.get("handle_missing", "Gérer les valeurs manquantes")):
                    method = st.selectbox(
                        t.get("missing_method", "Méthode :"),
                        ["drop_rows", "fill_mean", "fill_median", "fill_mode"]
                    )
                    df = validator.handle_missing_values(df, method=method)
                    st.success(t.get("missing_handled", "Valeurs manquantes traitées avec succès"))

        return df

    except Exception as e:
        error_handler.display_streamlit_error(e, "file_read_error")
        return None


def main():
    """Main function to run the Streamlit application."""
    
    # Set up language selector using language_utils
    selected_language = setup_language_selector()
    
    # Store language in session state
    st.session_state['language'] = selected_language
    t = translations[selected_language]
    
    # Main title
    st.title(t["app_title"])
    
    # Sidebar for navigation
    st.sidebar.title(t["nav_title"])
    
    # Dictionary of available analyses with proper function references
    # Only include modules that exist in the repository
    ANALYSES = {
        t["analysis1_title"]: show_statistical_overview,
        t["analysis2_title"]: show_zero_scores,
        t["analysis5_title"]: show_correlation,
        t["analysis6_title"]: show_reliability,
        t["analysis7_title"]: show_performance_school,
        t["analysis10_title"]: show_gender_effect,
        t["analysis12_title"]: show_international_comparison,
        t["analysis13_title"]: show_language_comparison
    }
    
    # Analysis selection
    analysis = st.sidebar.radio(
        t["select_analysis"],
        options=list(ANALYSES.keys()),
        key="analysis_selector"
    )
    
    # Load data
    df = load_data()
    
    # Show template section ONLY if no data is loaded
    if df is None:
        show_template_section()
    
    # Run selected analysis if data is loaded
    if df is not None:
        # Display analysis title
        st.header(analysis)
        st.divider()
        
        # Get the selected analysis function
        selected_function = ANALYSES[analysis]
        
        # Wrap the analysis function with error handling
        error_handler = ErrorHandler(language=selected_language)
        error_handler.wrap_analysis_function(selected_function, df, selected_language)

        # ========== FOOTER FIXE (AJOUTER ICI) ==========
    from credits import show_credits_fixed_footer
    show_credits_fixed_footer(language=selected_language)
    
if __name__ == "__main__":
    main()
