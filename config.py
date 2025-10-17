# config.py
import locale
from datetime import datetime

# Available languages
AVAILABLE_LANGUAGES = {
    "en": {"name": "English", "locale": "en_US.UTF-8", "flag": "🇬🇧"},
    "fr": {"name": "Français", "locale": "fr_FR.UTF-8", "flag": "🇫🇷"},
    "ar": {"name": "العربية", "locale": "ar_MA.UTF-8", "flag": "🇲🇦"},
    # Add more languages here in the future
}

# Default language
DEFAULT_LANGUAGE = "en"

# Translation dictionary
translations = {
    "en": {
        # Application title and navigation
        "app_title": "Educational Assessment Analytics",
        "welcome": "Welcome to the Educational Assessment Analytics application",
        "language_selector": "Select Language",
        "nav_title": "Navigation",
        "select_analysis": "Select Analysis Type",
        
        # Data loading and management
        "upload_file": "Upload Data File",
        "upload_help": "Supported formats: CSV, Excel, JSON, Stata DTA",
        "upload_info": "Please upload a file to begin analysis",
        "loading_data": "Loading data...",
        "upload_success": "File loaded successfully:",
        "upload_error": "Error loading file:",
        "select_sheet": "Select sheet",
        "select_encoding": "Encoding",
        "select_separator": "Separator",
        "rows_count": "Number of rows",
        "columns_count": "Number of columns",
        "show_preview": "Show data preview",
        "show_dtypes": "Show data types",
        
        # Error messages
        "encoding_error": "Encoding error. Try another encoding.",
        "parser_error": "Reading error. Check file format.",
        "value_error": "Value error. File might be corrupted.",
        "no_data_error": "Please upload data before running analysis.",
        
        # Analysis module titles
        "analysis1_title": "Statistical Overview",
        "analysis2_title": "Zero Scores Analysis",
        "analysis3_title": "School Comparison",
        "analysis4_title": "Language Effect Analysis",
        "analysis5_title": "Correlation Analysis",
        "analysis6_title": "Test Reliability (Cronbach Alpha)",
        "analysis7_title": "School Performance Analysis",
        "analysis8_title": "Contextual Factors Analysis",
        "analysis10_title": "Gender Effect Analysis",
        "analysis12_title": "International Standards Comparison",
        "analysis13_title": "Language of Instruction Comparison",
        
        # Common UI elements
        "select_variables": "Select Variables",
        "select_indicators": "Select Indicators",
        "export_csv": "Download CSV",
        "export_excel": "Download Excel",
        "export_word": "Export to Word",
        "export_ppt": "Export to PowerPoint",
        "download_word": "Download Word Report",
        "download_ppt": "Download PowerPoint",
        "generate_report": "Generate Report",
        "warning_select_variable": "Please select at least one variable to analyze.",
        
        # Educational assessment terminology
        "score": "Score",
        "mean_score": "Mean Score",
        "median_score": "Median Score",
        "std_dev": "Standard Deviation",
        "min_score": "Minimum Score",
        "max_score": "Maximum Score",
        "percentile_25": "25th Percentile",
        "percentile_50": "50th Percentile (Median)",
        "percentile_75": "75th Percentile",
        "distribution": "Distribution",
        "histogram": "Histogram",
        "frequency": "Frequency",
        "count": "Count",
        "percentage": "Percentage",
        "correlation": "Correlation",
        "significance": "Statistical Significance",
        "p_value": "p-value",
        "significant_difference": "Significant Difference",
        "no_significant_difference": "No Significant Difference",
        "columns_of_interest":{
             # Assessment variables
        "clpm": "Correct Letters Per Minute",
        "phoneme": "Phoneme Awareness",
        "sound_word": "Correctly Read Words",
        "cwpm": "Correct Words Per Minute",
        "listening": "Listening Comprehension",
        "orf": "Oral Reading Fluency",
        "comprehension": "Reading Comprehension",
        "number_id": "Number Identification",
        "discrimin": "Number Discrimination",
        "missing_number": "Missing Number",
        "addition": "Addition",
        "subtraction": "Subtraction",
        "problems": "Problems"
        },
       
        
        # Grouping variables
        "school": "School",
        "gender": "Gender",
        "boy": "Boy",
        "girl": "Girl",
        "language_teaching": "Language of Instruction",
        "english": "English",
        "dutch": "Dutch",
        "language_home": "Home Language",
        
        # Report and visualization elements
        "report_title": "Analysis Report",
        "report_date": "Report generated on",
        "executive_summary": "Executive Summary",
        "key_findings": "Key Findings",
        "recommendations": "Recommendations",
        "methodology": "Methodology",
        "conclusion": "Conclusion",
        "appendix": "Appendix",
        "figure": "Figure",
        "table": "Table",
        "page": "Page",
        "of": "of",
        
        # Dates and numbers formatting
        "date_format": "%B %d, %Y",
        "date_format_short": "%m/%d/%Y",
        "decimal_separator": ".",
        "thousands_separator": ",",
        "percentage_format": "{:.1f}%",
        
        # Assessment levels and interpretations
        "critical_level": "Critical",
        "concerning_level": "Concerning",
        "watch_level": "Watch",
        "satisfactory_level": "Satisfactory",
        "excellent_level": "Excellent",
        
        # Zero scores interpretation
        "zero_score_critical": "Critical concern - Immediate intervention required",
        "zero_score_concerning": "Concerning - Targeted support needed",
        "zero_score_watch": "Monitor closely - Provide additional practice",
        "zero_score_satisfactory": "Satisfactory - Continue with current approach"
    },
    
    "fr": {
        # Application title and navigation
        "app_title": "Analyse d'Évaluations Éducatives",
        "welcome": "Bienvenue dans l'application d'Analyse d'Évaluations Éducatives",
        "language_selector": "Sélectionner la Langue",
        "nav_title": "Navigation",
        "select_analysis": "Sélectionner le Type d'Analyse",
        
        # Data loading and management
        "upload_file": "Télécharger un Fichier de Données",
        "upload_help": "Formats supportés : CSV, Excel, JSON, Stata DTA",
        "upload_info": "Veuillez télécharger un fichier pour commencer l'analyse",
        "loading_data": "Chargement des données...",
        "upload_success": "Fichier chargé avec succès :",
        "upload_error": "Erreur lors du chargement du fichier :",
        "select_sheet": "Sélectionner une feuille",
        "select_encoding": "Encodage",
        "select_separator": "Séparateur",
        "rows_count": "Nombre de lignes",
        "columns_count": "Nombre de colonnes",
        "show_preview": "Afficher un aperçu des données",
        "show_dtypes": "Afficher les types de données",
        
        # Error messages
        "encoding_error": "Erreur d'encodage. Essayez un autre encodage.",
        "parser_error": "Erreur de lecture. Vérifiez le format du fichier.",
        "value_error": "Erreur de valeur. Le fichier pourrait être corrompu.",
        "no_data_error": "Veuillez télécharger des données avant de lancer l'analyse.",
        
        # Analysis module titles
        "analysis1_title": "Aperçu Statistique",
        "analysis2_title": "Analyse des Scores Zéro",
        "analysis3_title": "Comparaison entre Écoles",
        "analysis4_title": "Analyse de l'Effet de la Langue",
        "analysis5_title": "Analyse des Corrélations",
        "analysis6_title": "Fiabilité des Tests (Alpha de Cronbach)",
        "analysis7_title": "Analyse de Performance par École",
        "analysis8_title": "Analyse des Facteurs Contextuels",
        "analysis10_title": "Analyse de l'Effet du Genre",
        "analysis12_title": "Comparaison aux Standards Internationaux",
        "analysis13_title": "Comparaison par Langue d'Instruction",
        
        # Common UI elements
        "select_variables": "Sélectionner les Variables",
        "select_indicators": "Sélectionner les Indicateurs",
        "export_csv": "Télécharger CSV",
        "export_excel": "Télécharger Excel",
        "export_word": "Exporter en Word",
        "export_ppt": "Exporter en PowerPoint",
        "download_word": "Télécharger le Rapport Word",
        "download_ppt": "Télécharger PowerPoint",
        "generate_report": "Générer le Rapport",
        "warning_select_variable": "Veuillez sélectionner au moins une variable à analyser.",
        
        # Educational assessment terminology
        "score": "Score",
        "mean_score": "Score Moyen",
        "median_score": "Score Médian",
        "std_dev": "Écart-Type",
        "min_score": "Score Minimum",
        "max_score": "Score Maximum",
        "percentile_25": "25ème Percentile",
        "percentile_50": "50ème Percentile (Médiane)",
        "percentile_75": "75ème Percentile",
        "distribution": "Distribution",
        "histogram": "Histogramme",
        "frequency": "Fréquence",
        "count": "Nombre",
        "percentage": "Pourcentage",
        "correlation": "Corrélation",
        "significance": "Signification Statistique",
        "p_value": "Valeur p",
        "significant_difference": "Différence Significative",
        "no_significant_difference": "Pas de Différence Significative",
        "columns_of_interest":{
            # Assessment variables
            "clpm": "Lettres Correctes Par Minute",
            "phoneme": "Conscience Phonémique",
            "sound_word": "Mots Lus Correctement",
            "cwpm": "Mots Corrects Par Minute",
            "listening": "Compréhension Orale",
            "orf": "Fluidité de Lecture Orale",
            "comprehension": "Compréhension de Lecture",
            "number_id": "Identification des Nombres",
            "discrimin": "Discrimination des Nombres",
            "missing_number": "Nombre Manquant",
            "addition": "Addition",
            "subtraction": "Soustraction",
            "problems": "Problèmes"
        },
        
        
        # Grouping variables
        "school": "École",
        "gender": "Genre",
        "boy": "Garçon",
        "girl": "Fille",
        "language_teaching": "Langue d'Enseignement",
        "english": "Anglais",
        "dutch": "Néerlandais",
        "language_home": "Langue à la Maison",
        
        # Report and visualization elements
        "report_title": "Rapport d'Analyse",
        "report_date": "Rapport généré le",
        "executive_summary": "Résumé Exécutif",
        "key_findings": "Résultats Clés",
        "recommendations": "Recommandations",
        "methodology": "Méthodologie",
        "conclusion": "Conclusion",
        "appendix": "Annexe",
        "figure": "Figure",
        "table": "Tableau",
        "page": "Page",
        "of": "sur",
        
        # Dates and numbers formatting
        "date_format": "%d %B %Y",
        "date_format_short": "%d/%m/%Y",
        "decimal_separator": ",",
        "thousands_separator": " ",
        "percentage_format": "{:.1f} %",
        
        # Assessment levels and interpretations
        "critical_level": "Critique",
        "concerning_level": "Préoccupant",
        "watch_level": "À Surveiller",
        "satisfactory_level": "Satisfaisant",
        "excellent_level": "Excellent",
        
        # Zero scores interpretation
        "zero_score_critical": "Préoccupation critique - Intervention immédiate requise",
        "zero_score_concerning": "Préoccupant - Soutien ciblé nécessaire",
        "zero_score_watch": "Surveiller de près - Fournir des exercices supplémentaires",
        "zero_score_satisfactory": "Satisfaisant - Continuer avec l'approche actuelle"
    },
    
    "ar": {
        # Application title and navigation
        "app_title": "تحليل التقييمات التربوية",
        "welcome": "مرحبًا بك في تطبيق تحليل التقييمات التربوية",
        "language_selector": "اختر اللغة",
        "nav_title": "التنقل",
        "select_analysis": "اختر نوع التحليل",
        
        # Data loading and management
        "upload_file": "تحميل ملف البيانات",
        "upload_help": "الصيغ المدعومة: CSV، Excel، JSON، Stata DTA",
        "upload_info": "يرجى تحميل ملف لبدء التحليل",
        "loading_data": "جاري تحميل البيانات...",
        "upload_success": "تم تحميل الملف بنجاح:",
        "upload_error": "خطأ في تحميل الملف:",
        "select_sheet": "اختر الورقة",
        "select_encoding": "الترميز",
        "select_separator": "الفاصل",
        "rows_count": "عدد الصفوف",
        "columns_count": "عدد الأعمدة",
        "show_preview": "عرض معاينة البيانات",
        "show_dtypes": "عرض أنواع البيانات",
        
        # Error messages
        "encoding_error": "خطأ في الترميز. جرب ترميزًا آخر.",
        "parser_error": "خطأ في القراءة. تحقق من تنسيق الملف.",
        "value_error": "خطأ في القيمة. قد يكون الملف تالفًا.",
        "no_data_error": "يرجى تحميل البيانات قبل إجراء التحليل.",
        
        # Analysis module titles
        "analysis1_title": "نظرة عامة إحصائية",
        "analysis2_title": "تحليل الدرجات الصفرية",
        "analysis3_title": "مقارنة بين المدارس",
        "analysis4_title": "تحليل تأثير اللغة",
        "analysis5_title": "تحليل الارتباط",
        "analysis6_title": "موثوقية الاختبار (ألفا كرونباخ)",
        "analysis7_title": "تحليل أداء المدرسة",
        "analysis8_title": "تحليل العوامل السياقية",
        "analysis10_title": "تحليل تأثير الجنس",
        "analysis12_title": "مقارنة بالمعايير الدولية",
        "analysis13_title": "مقارنة حسب لغة التدريس",
        
        # Common UI elements
        "select_variables": "اختر المتغيرات",
        "select_indicators": "اختر المؤشرات",
        "export_csv": "تنزيل CSV",
        "export_excel": "تنزيل Excel",
        "export_word": "تصدير إلى Word",
        "export_ppt": "تصدير إلى PowerPoint",
        "download_word": "تنزيل تقرير Word",
        "download_ppt": "تنزيل PowerPoint",
        "generate_report": "إنشاء التقرير",
        "warning_select_variable": "يرجى اختيار متغير واحد على الأقل للتحليل.",
        
        # Educational assessment terminology
        "score": "الدرجة",
        "mean_score": "متوسط الدرجة",
        "median_score": "وسيط الدرجة",
        "std_dev": "الانحراف المعياري",
        "min_score": "الحد الأدنى للدرجة",
        "max_score": "الحد الأقصى للدرجة",
        "percentile_25": "الشريحة المئوية 25",
        "percentile_50": "الشريحة المئوية 50 (الوسيط)",
        "percentile_75": "الشريحة المئوية 75",
        "distribution": "التوزيع",
        "histogram": "الرسم البياني",
        "frequency": "التكرار",
        "count": "العدد",
        "percentage": "النسبة المئوية",
        "correlation": "الارتباط",
        "significance": "الدلالة الإحصائية",
        "p_value": "قيمة p",
        "significant_difference": "فرق ذو دلالة",
        "no_significant_difference": "لا يوجد فرق ذو دلالة",
        "columns_of_interest":{
            # Assessment variables
            "clpm": "الحروف الصحيحة في الدقيقة",
            "phoneme": "الوعي الصوتي",
            "sound_word": "الكلمات المقروءة بشكل صحيح",
            "cwpm": "الكلمات الصحيحة في الدقيقة",
            "listening": "فهم الاستماع",
            "orf": "طلاقة القراءة الشفهية",
            "comprehension": "فهم القراءة",
            "number_id": "تحديد الأرقام",
            "discrimin": "تمييز الأرقام",
            "missing_number": "الرقم المفقود",
            "addition": "الجمع",
            "subtraction": "الطرح",
            "problems": "المسائل"
        },
        
        # Grouping variables
        "school": "المدرسة",
        "gender": "الجنس",
        "boy": "ولد",
        "girl": "بنت",
        "language_teaching": "لغة التدريس",
        "english": "الإنجليزية",
        "dutch": "الهولندية",
        "language_home": "لغة المنزل",
        
        # Report and visualization elements
        "report_title": "تقرير التحليل",
        "report_date": "تم إنشاء التقرير في",
        "executive_summary": "الملخص التنفيذي",
        "key_findings": "النتائج الرئيسية",
        "recommendations": "التوصيات",
        "methodology": "المنهجية",
        "conclusion": "الخاتمة",
        "appendix": "الملحق",
        "figure": "الشكل",
        "table": "الجدول",
        "page": "صفحة",
        "of": "من",
        
        # Dates and numbers formatting
        "date_format": "%d %B %Y",
        "date_format_short": "%d/%m/%Y",
        "decimal_separator": "٫",
        "thousands_separator": "٬",
        "percentage_format": "{:.1f}٪",
        
        # Assessment levels and interpretations
        "critical_level": "حرج",
        "concerning_level": "مقلق",
        "watch_level": "تحت المراقبة",
        "satisfactory_level": "مُرضٍ",
        "excellent_level": "ممتاز",
        
        # Zero scores interpretation
        "zero_score_critical": "مصدر قلق حرج - تدخل فوري مطلوب",
        "zero_score_concerning": "مقلق - دعم موجه مطلوب",
        "zero_score_watch": "مراقبة عن كثب - توفير تدريب إضافي",
        "zero_score_satisfactory": "مُرضٍ - الاستمرار بالنهج الحالي"
    }
}

class LanguageManager:
    """
    Manager for handling translations and localization in the application.
    """
    
    def __init__(self, initial_language=DEFAULT_LANGUAGE):
        """
        Initialize the language manager with a default language.
        
        Args:
            initial_language (str): Initial language code (default: from DEFAULT_LANGUAGE)
        """
        self.current_language = initial_language if initial_language in AVAILABLE_LANGUAGES else DEFAULT_LANGUAGE
        self._set_locale()
    
    def _set_locale(self):
        """Set the system locale based on the current language."""
        try:
            locale.setlocale(locale.LC_ALL, AVAILABLE_LANGUAGES[self.current_language]["locale"])
        except locale.Error:
            # Fall back to basic locale if specific one not available
            try:
                basic_locale = self.current_language + ".UTF-8"
                locale.setlocale(locale.LC_ALL, basic_locale)
            except locale.Error:
                # If all else fails, use system default
                locale.setlocale(locale.LC_ALL, '')
    
    def get_text(self, key, default=""):
        """
        Get translated text for a specific key.
        
        Args:
            key (str): Translation key
            default (str): Default value if key not found
            
        Returns:
            str: Translated text
        """
        return translations.get(self.current_language, {}).get(key, default)
    
    def get_all_texts(self):
        """
        Get all translations for the current language.
        
        Returns:
            dict: All translations for current language
        """
        return translations.get(self.current_language, {})
    
    def change_language(self, language_code):
        """
        Change the current language.
        
        Args:
            language_code (str): Language code to switch to
            
        Returns:
            bool: True if language was changed, False if language code was invalid
        """
        if language_code in AVAILABLE_LANGUAGES:
            self.current_language = language_code
            self._set_locale()
            return True
        return False
    
    def get_available_languages(self):
        """
        Get list of available languages.
        
        Returns:
            dict: Available languages with metadata
        """
        return AVAILABLE_LANGUAGES
    
    def format_number(self, number, decimal_places=2):
        """
        Format a number according to locale conventions.
        
        Args:
            number (float): Number to format
            decimal_places (int): Number of decimal places
            
        Returns:
            str: Formatted number
        """
        # Get separators from translation dictionary
        decimal_sep = self.get_text("decimal_separator", ".")
        thousands_sep = self.get_text("thousands_separator", ",")
        
        # Format with locale settings
        try:
            if decimal_places == 0:
                return locale.format_string("%d", number, grouping=True)
            else:
                locale_format = f"%.{decimal_places}f"
                formatted = locale.format_string(locale_format, number, grouping=True)
                
                # Replace with custom separators if they don't match locale
                if locale.localeconv()['decimal_point'] != decimal_sep:
                    formatted = formatted.replace(locale.localeconv()['decimal_point'], decimal_sep)
                
                if locale.localeconv()['thousands_sep'] != thousands_sep:
                    formatted = formatted.replace(locale.localeconv()['thousands_sep'], thousands_sep)
                
                return formatted
        except:
            # Fallback method if locale formatting fails
            if decimal_places == 0:
                return format(int(number), ",").replace(",", thousands_sep)
            else:
                return format(round(number, decimal_places), f",.{decimal_places}f").replace(",", thousands_sep).replace(".", decimal_sep)
    
    def format_percentage(self, value):
        """
        Format a value as a percentage according to locale conventions.
        
        Args:
            value (float): Value to format as percentage (0.1 = 10%)
            
        Returns:
            str: Formatted percentage
        """
        percentage_format = self.get_text("percentage_format", "{:.1f}%")
        return percentage_format.format(value * 100)
    
    def format_date(self, date, short=False):
        """
        Format a date according to locale conventions.
        
        Args:
            date (datetime): Date to format
            short (bool): Whether to use short date format
            
        Returns:
            str: Formatted date
        """
        if short:
            date_format = self.get_text("date_format_short", "%m/%d/%Y")
        else:
            date_format = self.get_text("date_format", "%B %d, %Y")
        
        if isinstance(date, datetime):
            return date.strftime(date_format)
        else:
            return date


# Create a global instance of the language manager
language_manager = LanguageManager()

# Export commonly used assessment variables
egra_columns = ["clpm", "phoneme", "sound_word", "cwpm", "listening", "orf", "comprehension"]
egma_columns = ["number_id", "discrimin", "missing_number", "addition", "subtraction", "problems"]

# ============================================================
# AJOUTEZ CES LIGNES DANS VOTRE FICHIER config.py
# À ajouter dans chaque dictionnaire de langue (en, fr, ar)
# ============================================================

# Pour la langue ANGLAISE (en)
translations["en"].update({
    # Credits - Sidebar and Footer
    "credits_designed_by": "Designed by",
    "credits_managed_by": "Managed by",
    "credits_open_source": "Open Source",
    "credits_development": "Development",
    "credits_organization": "Organization",
    "credits_platform_description": "Educational Assessment Analytics Platform EGRA/EGMA",
    "credits_version": "Version",
    "credits_license": "License",
    "credits_all_rights": "All rights reserved",
    
    # Credits - Full Page
    "credits_page_title": "Credits and Legal Information",
    "credits_conception_dev": "Conception and Development",
    "credits_dev_description": """
This application was designed and developed by **{author}**.

- 🌐 Website: [{website}](https://{website})
- 📧 Contact: {contact}
- 💼 Services: Data Analytics, Business Intelligence, Educational Technology

**Ben Data Insights** specializes in creating data analysis solutions 
for the education sector and social impact organizations.
    """,
    "credits_management_deployment": "Management and Deployment",
    "credits_org_description": """
This platform is managed and deployed by **{organization}**.

- 🌐 Website: [{org_website}](https://{org_website})
- 🎯 Mission: Improve education through data analysis
- 🌍 Impact: Support educational systems in developing countries

ONG Meridie is committed to promoting the use of evidence-based data 
to improve children's educational outcomes.
    """,
    "credits_license_section": "Open Source License",
    "credits_license_intro": "**{project_name}** is distributed under **{license}**.",
    "credits_terms_of_use": "Terms of Use",
    "credits_you_can": "You CAN",
    "credits_permissions_list": """
- Use this software for free
- Modify the source code
- Distribute copies
- Use for commercial purposes
    """,
    "credits_you_must": "You MUST",
    "credits_conditions_list": """
- **Keep original credits** ({author} & {organization})
- Mention modifications made
- Include MIT license in any distribution
- Cite source in academic publications
    """,
    "credits_you_cannot": "You CANNOT",
    "credits_limitations_list": """
- Remove or modify author attributions
- Claim you created this software
- Use creators' names to promote derivatives without permission
    """,
    "credits_academic_citation": "Academic Citation",
    "credits_citation_format": """
**To cite this application in your academic work:**

Benhoumad, Z. ({year}). *{project_name}: Educational Assessment 
Analytics Platform EGRA/EGMA* (Version {version}) [Software]. 
ONG Meridie. https://{org_website}
    """,
    "credits_technologies": "Technologies Used",
    "credits_tech_list": """
This application uses the following open source technologies:

- **Streamlit** - Web application framework
- **Pandas** - Data manipulation and analysis
- **Plotly** - Interactive visualizations
- **Python-docx** - Word report generation
- **Google Gemini AI** - Educational interpretations
- **Scikit-learn** - Statistical analysis

Thank you to all open source communities that make this project possible! 🙏
    """,
    "credits_contact_support": "Contact and Support",
    "credits_contact_info": """
For questions, suggestions or collaboration:

- 📧 Email: {contact}
- 🌐 Web: [{website}](https://{website})
- 💼 LinkedIn: Zakaria Benhoumad
- 🐙 GitHub: [Datavizir Analytics]({github})
    """,
    
    # Credits - Word Document
    "credits_word_title": "Credits and Information",
    "credits_developed_by": "Developed by",
    "credits_website": "Website",
    "credits_email": "Email",
    "credits_note": "Note",
    "credits_attribution_note": "This report was generated with Datavizir Analytics. Use, modification or distribution of this software requires maintaining this attribution in accordance with the MIT license.",
    "credits_attribution_warning": """⚠️ **Attribution Required**

This software is open source but requires attribution to original authors.""",
})

# Pour la langue FRANÇAISE (fr)
translations["fr"].update({
    # Crédits - Sidebar et Footer
    "credits_designed_by": "Conçu par",
    "credits_managed_by": "Géré par",
    "credits_open_source": "Open Source",
    "credits_development": "Développement",
    "credits_organization": "Organisation",
    "credits_platform_description": "Plateforme d'Analyse d'Évaluations Éducatives EGRA/EGMA",
    "credits_version": "Version",
    "credits_license": "Licence",
    "credits_all_rights": "Tous droits réservés",
    
    # Crédits - Page complète
    "credits_page_title": "Crédits et Informations Légales",
    "credits_conception_dev": "Conception et Développement",
    "credits_dev_description": """
Cette application a été conçue et développée par **{author}**.

- 🌐 Site web : [{website}](https://{website})
- 📧 Contact : {contact}
- 💼 Services : Analyse de Données, Business Intelligence, Technologies Éducatives

**Ben Data Insights** est spécialisé dans la création de solutions d'analyse de données 
pour le secteur éducatif et les organisations à impact social.
    """,
    "credits_management_deployment": "Gestion et Déploiement",
    "credits_org_description": """
Cette plateforme est gérée et déployée par **{organization}**.

- 🌐 Site web : [{org_website}](https://{org_website})
- 🎯 Mission : Améliorer l'éducation à travers l'analyse de données
- 🌍 Impact : Soutien aux systèmes éducatifs dans les pays en développement

L'ONG Meridie s'engage à promouvoir l'utilisation de données probantes 
pour améliorer les résultats éducatifs des enfants.
    """,
    "credits_license_section": "Licence Open Source",
    "credits_license_intro": "**{project_name}** est distribué sous **{license}**.",
    "credits_terms_of_use": "Conditions d'Utilisation",
    "credits_you_can": "Vous POUVEZ",
    "credits_permissions_list": """
- Utiliser ce logiciel gratuitement
- Modifier le code source
- Distribuer des copies
- Utiliser à des fins commerciales
    """,
    "credits_you_must": "Vous DEVEZ",
    "credits_conditions_list": """
- **Conserver les crédits d'origine** ({author} & {organization})
- Mentionner les modifications apportées
- Inclure la licence MIT dans toute distribution
- Citer la source dans vos publications académiques
    """,
    "credits_you_cannot": "Vous NE POUVEZ PAS",
    "credits_limitations_list": """
- Supprimer ou modifier les attributions d'auteur
- Prétendre avoir créé ce logiciel
- Utiliser les noms des créateurs pour promouvoir des dérivés sans permission
    """,
    "credits_academic_citation": "Citation Académique",
    "credits_citation_format": """
**Pour citer cette application dans vos travaux académiques :**

Benhoumad, Z. ({year}). *{project_name} : Plateforme d'analyse 
des évaluations éducatives EGRA/EGMA* (Version {version}) [Logiciel]. 
ONG Meridie. https://{org_website}
    """,
    "credits_technologies": "Technologies Utilisées",
    "credits_tech_list": """
Cette application utilise les technologies open source suivantes :

- **Streamlit** - Framework d'application web
- **Pandas** - Manipulation et analyse de données
- **Plotly** - Visualisations interactives
- **Python-docx** - Génération de rapports Word
- **Google Gemini AI** - Interprétations pédagogiques
- **Scikit-learn** - Analyses statistiques

Merci à toutes les communautés open source qui rendent ce projet possible ! 🙏
    """,
    "credits_contact_support": "Contact et Support",
    "credits_contact_info": """
Pour toute question, suggestion ou collaboration :

- 📧 Email : {contact}
- 🌐 Web : [{website}](https://{website})
- 💼 LinkedIn : Zakaria Benhoumad
- 🐙 GitHub : [Datavizir Analytics]({github})
    """,
    
    # Crédits - Document Word
    "credits_word_title": "Crédits et Informations",
    "credits_developed_by": "Développé par",
    "credits_website": "Site web",
    "credits_email": "Email",
    "credits_note": "Note",
    "credits_attribution_note": "Ce rapport a été généré avec Datavizir Analytics. L'utilisation, la modification ou la distribution de ce logiciel nécessite le maintien de cette attribution conformément à la licence MIT.",
    "credits_attribution_warning": """⚠️ **Attribution Requise**

Ce logiciel est open source mais nécessite une attribution aux auteurs originaux.""",
})

# Pour la langue ARABE (ar)
translations["ar"].update({
    # الاعتمادات - الشريط الجانبي والتذييل
    "credits_designed_by": "مصمم من قبل",
    "credits_managed_by": "يديره",
    "credits_open_source": "مفتوح المصدر",
    "credits_development": "التطوير",
    "credits_organization": "المنظمة",
    "credits_platform_description": "منصة تحليل التقييمات التعليمية EGRA/EGMA",
    "credits_version": "الإصدار",
    "credits_license": "الترخيص",
    "credits_all_rights": "جميع الحقوق محفوظة",
    
    # الاعتمادات - الصفحة الكاملة
    "credits_page_title": "الاعتمادات والمعلومات القانونية",
    "credits_conception_dev": "التصميم والتطوير",
    "credits_dev_description": """
تم تصميم وتطوير هذا التطبيق بواسطة **{author}**.

- 🌐 الموقع الإلكتروني: [{website}](https://{website})
- 📧 البريد الإلكتروني: {contact}
- 💼 الخدمات: تحليل البيانات، ذكاء الأعمال، التكنولوجيا التعليمية

**Ben Data Insights** متخصص في إنشاء حلول تحليل البيانات 
للقطاع التعليمي والمنظمات ذات الأثر الاجتماعي.
    """,
    "credits_management_deployment": "الإدارة والنشر",
    "credits_org_description": """
تدار هذه المنصة ويتم نشرها بواسطة **{organization}**.

- 🌐 الموقع الإلكتروني: [{org_website}](https://{org_website})
- 🎯 المهمة: تحسين التعليم من خلال تحليل البيانات
- 🌍 التأثير: دعم الأنظمة التعليمية في البلدان النامية

تلتزم منظمة Meridie بتعزيز استخدام البيانات القائمة على الأدلة 
لتحسين النتائج التعليمية للأطفال.
    """,
    "credits_license_section": "ترخيص مفتوح المصدر",
    "credits_license_intro": "يتم توزيع **{project_name}** بموجب **{license}**.",
    "credits_terms_of_use": "شروط الاستخدام",
    "credits_you_can": "يمكنك",
    "credits_permissions_list": """
- استخدام هذا البرنامج مجانًا
- تعديل الكود المصدري
- توزيع النسخ
- الاستخدام لأغراض تجارية
    """,
    "credits_you_must": "يجب عليك",
    "credits_conditions_list": """
- **الاحتفاظ بالاعتمادات الأصلية** ({author} و {organization})
- ذكر التعديلات التي تم إجراؤها
- تضمين ترخيص MIT في أي توزيع
- الاستشهاد بالمصدر في المنشورات الأكاديمية
    """,
    "credits_you_cannot": "لا يمكنك",
    "credits_limitations_list": """
- إزالة أو تعديل إسناد المؤلف
- الادعاء بأنك أنشأت هذا البرنامج
- استخدام أسماء المبدعين للترويج للمشتقات دون إذن
    """,
    "credits_academic_citation": "الاستشهاد الأكاديمي",
    "credits_citation_format": """
**للاستشهاد بهذا التطبيق في عملك الأكاديمي:**

Benhoumad, Z. ({year}). *{project_name}: منصة تحليل 
التقييمات التعليمية EGRA/EGMA* (الإصدار {version}) [برنامج]. 
ONG Meridie. https://{org_website}
    """,
    "credits_technologies": "التقنيات المستخدمة",
    "credits_tech_list": """
يستخدم هذا التطبيق التقنيات مفتوحة المصدر التالية:

- **Streamlit** - إطار عمل تطبيقات الويب
- **Pandas** - معالجة وتحليل البيانات
- **Plotly** - التصورات التفاعلية
- **Python-docx** - إنشاء تقارير Word
- **Google Gemini AI** - التفسيرات التربوية
- **Scikit-learn** - التحليل الإحصائي

شكرًا لجميع مجتمعات المصادر المفتوحة التي تجعل هذا المشروع ممكنًا! 🙏
    """,
    "credits_contact_support": "الاتصال والدعم",
    "credits_contact_info": """
للأسئلة أو الاقتراحات أو التعاون:

- 📧 البريد الإلكتروني: {contact}
- 🌐 الويب: [{website}](https://{website})
- 💼 LinkedIn: Zakaria Benhoumad
- 🐙 GitHub: [Datavizir Analytics]({github})
    """,
    
    # الاعتمادات - مستند Word
    "credits_word_title": "الاعتمادات والمعلومات",
    "credits_developed_by": "تم التطوير بواسطة",
    "credits_website": "الموقع الإلكتروني",
    "credits_email": "البريد الإلكتروني",
    "credits_note": "ملاحظة",
    "credits_attribution_note": "تم إنشاء هذا التقرير باستخدام Datavizir Analytics. يتطلب الاستخدام أو التعديل أو التوزيع لهذا البرنامج الحفاظ على هذا الإسناد وفقًا لترخيص MIT.",
    "credits_attribution_warning": """⚠️ **الإسناد مطلوب**

هذا البرنامج مفتوح المصدر ولكنه يتطلب الإسناد إلى المؤلفين الأصليين.""",
})