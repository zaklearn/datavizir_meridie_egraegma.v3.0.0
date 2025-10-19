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
        "zero_score_satisfactory": "Satisfactory - Continue with current approach",
            "task_column": "Task",
    "count_column": "Count of Zeros",
    "percentage_column": "Percentage of Zero Scores",
    "zero_scores_chart_title": "📊 Percentage of Students with Zero Scores by Task",
    "acceptable_threshold": "Acceptable",
    "concerning_threshold": "Concerning",
    "critical_threshold": "Critical",
    "egra_variables": "EGRA Variables:",
    "egma_variables": "EGMA Variables:",
    "warning_select_task": "Please select at least one task to analyze.",
    "interpretation_title": "📝 Educational Interpretation",
    
    # Section Actions and Exports
    "actions_section": "📊 Actions and Exports",
    "usage_guide_title": "💡 User Guide:",
    "usage_guide_ai": "**🔍 AI Interpretation**: Generate detailed pedagogical analysis with recommendations (requires Gemini API)",
    "usage_guide_report": "**📄 Complete Report**: Create a professional Word document including tables, charts and AI interpretation",
    
    # Buttons
    "generate_interpretation": "Generate AI Interpretation",
    "export_complete_report": "Generate Complete Report (Word)",
    "download_complete_report": "Download Report",
    "api_locked": "🔒",
    "api_locked_help": "Configure your Gemini API key in .env file to enable this feature",
    
    # Status messages
    "generating_interpretation": "🤖 Generating interpretation...",
    "generating_report": "📝 Generating complete report...",
    "report_ready": "✅ Report generated successfully!",
    "wait_for_graph": "⚠️ Please wait, the chart is loading...",
    
    # Error messages
    "api_not_configured": "❌ **Gemini API not configured**",
    "api_activation_steps": """
    **To activate AI interpretation, follow these steps:**

    1. Create a `.env` file at the root of your project
    2. Add your Gemini API key in this file:
       ```
       GEMINI_API_KEY=your_api_key_here
       ```
    3. Get a free API key on [Google AI Studio](https://aistudio.google.com)
    4. Restart the application

    **In the meantime**, you can consult the tables and charts above which already provide detailed information on performance.
        """,
        "quota_exceeded": "❌ **Gemini API quota exceeded**",
        "quota_solutions": """
    **Possible solutions:**
    1. 🕐 Wait a few minutes before trying again
    2. 🔑 Check your Gemini API plan on [Google AI Studio](https://aistudio.google.com)
    3. 💳 Consider upgrading to a paid plan for higher quotas
    4. 📊 For now, you can consult the tables and charts above

    **Free tier limits:**
    - 2 requests per minute
    - 1,500 requests per day

    [Learn more about quotas](https://ai.google.dev/gemini-api/docs/rate-limits)
        """,
        "retry_message": "⏳ Retrying ({attempt}/{max_retries}) in {delay} seconds...",
        "quota_retry": "⚠️ API quota limit reached. Automatic retry in {delay} seconds...",
        "error_generating_report": "❌ Error generating report: {error}",
        "verification_suggestions": """
    **Suggested verifications:**
    - ✅ Your API key is correct in the `.env` file
    - ✅ You have an active internet connection
    - ✅ The Gemini API is accessible from your region
        """

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
    # Zero Scores Analysis - Additional keys
    "task_column": "Task",
    "count_column": "Count of Zeros",
    "percentage_column": "Percentage of Zero Scores",
    "zero_scores_chart_title": "📊 Percentage of Students with Zero Scores by Task",
    "acceptable_threshold": "Acceptable",
    "concerning_threshold": "Concerning",
    "critical_threshold": "Critical",
    "egra_variables": "EGRA Variables:",
    "egma_variables": "EGMA Variables:",
    "warning_select_task": "Please select at least one task to analyze.",
    "interpretation_title": "📝 Educational Interpretation",
    
    # Section Actions and Exports
    "actions_section": "📊 Actions and Exports",
    "usage_guide_title": "💡 User Guide:",
    "usage_guide_ai": "**🔍 AI Interpretation**: Generate detailed pedagogical analysis with recommendations (requires Gemini API)",
    "usage_guide_report": "**📄 Complete Report**: Create a professional Word document including tables, charts and AI interpretation",
    
    # Buttons
    "generate_interpretation": "Generate AI Interpretation",
    "export_complete_report": "Generate Complete Report (Word)",
    "download_complete_report": "Download Report",
    "api_locked": "🔒",
    "api_locked_help": "Configure your Gemini API key in .env file to enable this feature",
    
    # Status messages
    "generating_interpretation": "🤖 Generating interpretation...",
    "generating_report": "📝 Generating complete report...",
    "report_ready": "✅ Report generated successfully!",
    "wait_for_graph": "⚠️ Please wait, the chart is loading...",
    
    # Error messages
    "api_not_configured": "❌ **Gemini API not configured**",
    "api_activation_steps": """
**To activate AI interpretation, follow these steps:**

1. Create a `.env` file at the root of your project
2. Add your Gemini API key in this file:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```
3. Get a free API key on [Google AI Studio](https://aistudio.google.com)
4. Restart the application

**In the meantime**, you can consult the tables and charts above which already provide detailed information on performance.
    """,
    "quota_exceeded": "❌ **Gemini API quota exceeded**",
    "quota_solutions": """
**Possible solutions:**
1. 🕐 Wait a few minutes before trying again
2. 🔑 Check your Gemini API plan on [Google AI Studio](https://aistudio.google.com)
3. 💳 Consider upgrading to a paid plan for higher quotas
4. 📊 For now, you can consult the tables and charts above

**Free tier limits:**
- 2 requests per minute
- 1,500 requests per day

[Learn more about quotas](https://ai.google.dev/gemini-api/docs/rate-limits)
    """,
    "retry_message": "⏳ Retrying ({attempt}/{max_retries}) in {delay} seconds...",
    "quota_retry": "⚠️ API quota limit reached. Automatic retry in {delay} seconds...",
    "error_generating_report": "❌ Error generating report: {error}",
    "verification_suggestions": """
**Suggested verifications:**
- ✅ Your API key is correct in the `.env` file
- ✅ You have an active internet connection
- ✅ The Gemini API is accessible from your region
    """,
        # Word Report - Executive Summary
    "report_intro_text": "This report analyzes zero scores obtained by students on {total_tasks} assessment tasks.",
    "key_stats_title": "Key Statistics:",
    "avg_zero_percentage": "Average percentage of zero scores: {avg_percentage:.1f}%",
    "critical_tasks_count": "Critical tasks (>30% zeros): {critical_count}",
    "concerning_tasks_count": "Concerning tasks (20-30% zeros): {concerning_count}",
    "zero_score_meaning": "A zero score indicates a complete absence of mastery of the assessed skill and requires particular attention.",
    
    # Word Report - Recommendations section
    "critical_areas_title": "🔴 Critical Areas (>30% zero scores)",
    "critical_areas_description": "These skills require immediate intervention with intensive and targeted teaching programs.",
    "concerning_areas_title": "🟠 Concerning Areas (20-30% zero scores)",
    "concerning_areas_description": "These skills require significant reinforcement within regular instruction.",
    "general_strategies_title": "General Intervention Strategies",
    "strategy_1": "Differentiated instruction in small groups",
    "strategy_2": "In-depth diagnostic assessment to identify specific gaps",
    "strategy_3": "Early and intensive intervention for struggling students",
    "strategy_4": "Regular progress monitoring (every 2-3 weeks)",
    "strategy_5": "Collaboration with families for home support",
    
    # Word Report - Methodology section
    "methodology_title": "Methodological Notes",
    "methodology_intro": "This report analyzes zero scores in EGRA/EGMA assessments according to the following criteria:",
    "interpretation_thresholds": "Interpretation Thresholds:",
    "threshold_acceptable": "Acceptable: < 10% zero scores",
    "threshold_monitor": "To monitor: 10-20% zero scores",
    "threshold_concerning": "Concerning: 20-30% zero scores",
    "threshold_critical": "Critical: > 30% zero scores",
    "methodology_explanation": "A high percentage of zero scores indicates that many students have not acquired the fundamental skills being assessed. These gaps can compromise future learning and require immediate attention.",
    "methodology_basis": "Recommendations are based on best practices in teaching primary reading and mathematics, as documented by educational research.",
    
    # Word Report - Footer
    "report_generated_by": "Report generated by Datavizir Analytics",
    "ai_interpretation_notice": "🤖 This interpretation was generated by artificial intelligence (Gemini)",

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
    # Analyse des scores nuls - Clés supplémentaires
    "task_column": "Tâche",
    "count_column": "Nombre de Zéros",
    "percentage_column": "Pourcentage de Scores Nuls",
    "zero_scores_chart_title": "📊 Pourcentage d'Élèves avec des Scores Nuls par Tâche",
    "acceptable_threshold": "Acceptable",
    "concerning_threshold": "Préoccupant",
    "critical_threshold": "Critique",
    "egra_variables": "Variables EGRA:",
    "egma_variables": "Variables EGMA:",
    "warning_select_task": "Veuillez sélectionner au moins une tâche à analyser.",
    "interpretation_title": "📝 Interprétation Pédagogique",
    
    # Section Actions et Exports
    "actions_section": "📊 Actions et Exports",
    "usage_guide_title": "💡 Guide d'utilisation :",
    "usage_guide_ai": "**🔍 Interprétation IA** : Générez une analyse pédagogique détaillée avec recommandations (nécessite API Gemini)",
    "usage_guide_report": "**📄 Rapport Complet** : Créez un document Word professionnel incluant tableaux, graphiques et interprétation IA",
    
    # Boutons
    "generate_interpretation": "Générer l'Interprétation IA",
    "export_complete_report": "Générer Rapport Complet (Word)",
    "download_complete_report": "Télécharger le rapport",
    "api_locked": "🔒",
    "api_locked_help": "Configurez votre clé API Gemini dans le fichier .env pour activer cette fonctionnalité",
    
    # Messages de statut
    "generating_interpretation": "🤖 Génération de l'interprétation...",
    "generating_report": "📝 Génération du rapport complet...",
    "report_ready": "✅ Rapport généré avec succès!",
    "wait_for_graph": "⚠️ Veuillez patienter, le graphique se charge...",
    
    # Messages d'erreur
    "api_not_configured": "❌ **API Gemini non configurée**",
    "api_activation_steps": """
**Pour activer l'interprétation par IA, suivez ces étapes :**

1. Créez un fichier `.env` à la racine de votre projet
2. Ajoutez votre clé API Gemini dans ce fichier :
   ```
   GEMINI_API_KEY=votre_clé_api_ici
   ```
3. Obtenez une clé API gratuite sur [Google AI Studio](https://aistudio.google.com)
4. Redémarrez l'application

**En attendant**, vous pouvez consulter les tableaux et graphiques ci-dessus qui fournissent déjà des informations détaillées sur les performances.
    """,
    "quota_exceeded": "❌ **Quota API Gemini dépassé**",
    "quota_solutions": """
**Solutions possibles :**
1. 🕐 Attendez quelques minutes avant de réessayer
2. 🔑 Vérifiez votre plan API Gemini sur [Google AI Studio](https://aistudio.google.com)
3. 💳 Considérez passer à un plan payant pour des quotas plus élevés
4. 📊 Pour le moment, vous pouvez consulter les tableaux et graphiques ci-dessus

**Limites du niveau gratuit :**
- 2 requêtes par minute
- 1 500 requêtes par jour

[En savoir plus sur les quotas](https://ai.google.dev/gemini-api/docs/rate-limits)
    """,
    "retry_message": "⏳ Nouvelle tentative ({attempt}/{max_retries}) dans {delay} secondes...",
    "quota_retry": "⚠️ Limite de quota API atteinte. Nouvelle tentative automatique dans {delay} secondes...",
    "error_generating_report": "❌ Erreur lors de la génération du rapport: {error}",
    "verification_suggestions": """
**Vérifications suggérées :**
- ✅ Votre clé API est correcte dans le fichier `.env`
- ✅ Vous avez une connexion internet active
- ✅ L'API Gemini est accessible depuis votre région
    """,
        # Rapport Word - Résumé exécutif
    "report_intro_text": "Ce rapport analyse les scores nuls (zéro) obtenus par les élèves sur {total_tasks} tâches d'évaluation.",
    "key_stats_title": "Statistiques clés :",
    "avg_zero_percentage": "Pourcentage moyen de scores nuls : {avg_percentage:.1f}%",
    "critical_tasks_count": "Tâches critiques (>30% de zéros) : {critical_count}",
    "concerning_tasks_count": "Tâches préoccupantes (20-30% de zéros) : {concerning_count}",
    "zero_score_meaning": "Un score de zéro indique une absence totale de maîtrise de la compétence évaluée et nécessite une attention particulière.",
    
    # Rapport Word - Section recommandations
    "critical_areas_title": "🔴 Zones Critiques (>30% de scores nuls)",
    "critical_areas_description": "Ces compétences nécessitent une intervention immédiate avec des programmes d'enseignement intensif et ciblé.",
    "concerning_areas_title": "🟠 Zones Préoccupantes (20-30% de scores nuls)",
    "concerning_areas_description": "Ces compétences nécessitent un renforcement significatif dans le cadre de l'enseignement régulier.",
    "general_strategies_title": "Stratégies d'Intervention Générales",
    "strategy_1": "Enseignement différencié en petits groupes",
    "strategy_2": "Évaluation diagnostique approfondie pour identifier les lacunes spécifiques",
    "strategy_3": "Intervention précoce et intensive pour les élèves en difficulté",
    "strategy_4": "Suivi régulier des progrès (toutes les 2-3 semaines)",
    "strategy_5": "Collaboration avec les familles pour le soutien à domicile",
    
    # Rapport Word - Section méthodologie
    "methodology_title": "Notes Méthodologiques",
    "methodology_intro": "Ce rapport analyse les scores nuls (zéro) dans les évaluations EGRA/EGMA selon les critères suivants :",
    "interpretation_thresholds": "Seuils d'Interprétation :",
    "threshold_acceptable": "Acceptable : < 10% de scores nuls",
    "threshold_monitor": "À surveiller : 10-20% de scores nuls",
    "threshold_concerning": "Préoccupant : 20-30% de scores nuls",
    "threshold_critical": "Critique : > 30% de scores nuls",
    "methodology_explanation": "Un pourcentage élevé de scores nuls indique que de nombreux élèves n'ont pas acquis les compétences fondamentales évaluées. Ces lacunes peuvent compromettre les apprentissages futurs et nécessitent une attention immédiate.",
    "methodology_basis": "Les recommandations sont basées sur les meilleures pratiques en matière d'enseignement de la lecture et des mathématiques au primaire, telles que documentées par la recherche en sciences de l'éducation.",
    
    # Rapport Word - Pied de page
    "report_generated_by": "Rapport généré par Datavizir Analytics",
    "ai_interpretation_notice": "🤖 Cette interprétation a été générée par intelligence artificielle (Gemini)",

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
    # تحليل النتائج الصفرية - مفاتيح إضافية
    "task_column": "المهمة",
    "count_column": "عدد الأصفار",
    "percentage_column": "نسبة النتائج الصفرية",
    "zero_scores_chart_title": "📊 نسبة الطلاب ذوي النتائج الصفرية حسب المهمة",
    "acceptable_threshold": "مقبول",
    "concerning_threshold": "مثير للقلق",
    "critical_threshold": "حرج",
    "egra_variables": "متغيرات EGRA:",
    "egma_variables": "متغيرات EGMA:",
    "warning_select_task": "الرجاء تحديد مهمة واحدة على الأقل للتحليل.",
    "interpretation_title": "📝 التفسير التربوي",
    
    # قسم الإجراءات والتصديرات
    "actions_section": "📊 الإجراءات والتصديرات",
    "usage_guide_title": "💡 دليل الاستخدام:",
    "usage_guide_ai": "**🔍 التفسير بالذكاء الاصطناعي**: إنشاء تحليل تربوي مفصل مع التوصيات (يتطلب Gemini API)",
    "usage_guide_report": "**📄 التقرير الكامل**: إنشاء مستند Word احترافي يتضمن الجداول والرسوم البيانية والتفسير بالذكاء الاصطناعي",
    
    # الأزرار
    "generate_interpretation": "إنشاء التفسير بالذكاء الاصطناعي",
    "export_complete_report": "إنشاء تقرير كامل (Word)",
    "download_complete_report": "تنزيل التقرير",
    "api_locked": "🔒",
    "api_locked_help": "قم بتكوين مفتاح Gemini API الخاص بك في ملف .env لتفعيل هذه الميزة",
    
    # رسائل الحالة
    "generating_interpretation": "🤖 جاري إنشاء التفسير...",
    "generating_report": "📝 جاري إنشاء التقرير الكامل...",
    "report_ready": "✅ تم إنشاء التقرير بنجاح!",
    "wait_for_graph": "⚠️ يرجى الانتظار، جاري تحميل الرسم البياني...",
    
    # رسائل الخطأ
    "api_not_configured": "❌ **لم يتم تكوين Gemini API**",
    "api_activation_steps": """
**لتفعيل التفسير بالذكاء الاصطناعي، اتبع هذه الخطوات:**

1. أنشئ ملف `.env` في جذر مشروعك
2. أضف مفتاح Gemini API الخاص بك في هذا الملف:
   ```
   GEMINI_API_KEY=مفتاح_api_الخاص_بك
   ```
3. احصل على مفتاح API مجاني من [Google AI Studio](https://aistudio.google.com)
4. أعد تشغيل التطبيق

**في الوقت الحالي**، يمكنك الاطلاع على الجداول والرسوم البيانية أعلاه التي توفر بالفعل معلومات تفصيلية عن الأداء.
    """,
    "quota_exceeded": "❌ **تم تجاوز حصة Gemini API**",
    "quota_solutions": """
**الحلول الممكنة:**
1. 🕐 انتظر بضع دقائق قبل المحاولة مرة أخرى
2. 🔑 تحقق من خطة Gemini API الخاصة بك على [Google AI Studio](https://aistudio.google.com)
3. 💳 فكر في الترقية إلى خطة مدفوعة للحصول على حصص أعلى
4. 📊 في الوقت الحالي، يمكنك الاطلاع على الجداول والرسوم البيانية أعلاه

**حدود المستوى المجاني:**
- طلبان في الدقيقة
- 1500 طلب في اليوم

[معرفة المزيد عن الحصص](https://ai.google.dev/gemini-api/docs/rate-limits)
    """,
    "retry_message": "⏳ إعادة المحاولة ({attempt}/{max_retries}) في {delay} ثانية...",
    "quota_retry": "⚠️ تم الوصول إلى حد حصة API. إعادة المحاولة تلقائيًا في {delay} ثانية...",
    "error_generating_report": "❌ خطأ في إنشاء التقرير: {error}",
    "verification_suggestions": """
**التحقق المقترح:**
- ✅ مفتاح API الخاص بك صحيح في ملف `.env`
- ✅ لديك اتصال إنترنت نشط
- ✅ Gemini API متاح من منطقتك
    """,
        # تقرير Word - الملخص التنفيذي
    "report_intro_text": "يحلل هذا التقرير النتائج الصفرية التي حصل عليها الطلاب في {total_tasks} مهام تقييم.",
    "key_stats_title": "الإحصائيات الرئيسية:",
    "avg_zero_percentage": "متوسط نسبة النتائج الصفرية: {avg_percentage:.1f}%",
    "critical_tasks_count": "المهام الحرجة (>30% أصفار): {critical_count}",
    "concerning_tasks_count": "المهام المقلقة (20-30% أصفار): {concerning_count}",
    "zero_score_meaning": "تشير النتيجة الصفرية إلى غياب تام لإتقان المهارة المقيمة وتتطلب اهتمامًا خاصًا.",
    
    # تقرير Word - قسم التوصيات
    "critical_areas_title": "🔴 المناطق الحرجة (>30% نتائج صفرية)",
    "critical_areas_description": "تتطلب هذه المهارات تدخلاً فوريًا ببرامج تعليمية مكثفة ومستهدفة.",
    "concerning_areas_title": "🟠 المناطق المقلقة (20-30% نتائج صفرية)",
    "concerning_areas_description": "تتطلب هذه المهارات تعزيزًا كبيرًا في إطار التعليم المنتظم.",
    "general_strategies_title": "استراتيجيات التدخل العامة",
    "strategy_1": "التعليم المتمايز في مجموعات صغيرة",
    "strategy_2": "التقييم التشخيصي المتعمق لتحديد الثغرات المحددة",
    "strategy_3": "التدخل المبكر والمكثف للطلاب المتعثرين",
    "strategy_4": "المتابعة المنتظمة للتقدم (كل 2-3 أسابيع)",
    "strategy_5": "التعاون مع الأسر للدعم المنزلي",
    
    # تقرير Word - قسم المنهجية
    "methodology_title": "ملاحظات منهجية",
    "methodology_intro": "يحلل هذا التقرير النتائج الصفرية في تقييمات EGRA/EGMA وفقًا للمعايير التالية:",
    "interpretation_thresholds": "عتبات التفسير:",
    "threshold_acceptable": "مقبول: < 10% نتائج صفرية",
    "threshold_monitor": "للمراقبة: 10-20% نتائج صفرية",
    "threshold_concerning": "مقلق: 20-30% نتائج صفرية",
    "threshold_critical": "حرج: > 30% نتائج صفرية",
    "methodology_explanation": "تشير النسبة العالية من النتائج الصفرية إلى أن العديد من الطلاب لم يكتسبوا المهارات الأساسية المقيمة. يمكن أن تعرض هذه الثغرات التعلم المستقبلي للخطر وتتطلب اهتمامًا فوريًا.",
    "methodology_basis": "تستند التوصيات إلى أفضل الممارسات في تعليم القراءة والرياضيات الابتدائية، كما هو موثق من قبل البحث التربوي.",
    
    # تقرير Word - التذييل
    "report_generated_by": "تم إنشاء التقرير بواسطة Datavizir Analytics",
    "ai_interpretation_notice": "🤖 تم إنشاء هذا التفسير بواسطة الذكاء الاصطناعي (Gemini)",

})

# ============ ANGLAIS (en) ============
translations["en"].update({
    "gemini_prompt_template": """**Context:** You are an internationally renowned expert in educational sciences, specialized in the analysis of large-scale assessments such as EGRA. Your analysis must be rigorous, evidence-based, and your recommendations must be practical for teachers.

**Raw Data to Analyze:** The table below shows the percentage of students who obtained a zero score for several fundamental assessment tasks. A zero score represents a complete absence of the measured skill.

```markdown
{data_as_markdown}
```

**Your Mission:** Write a comprehensive diagnostic analysis report in English. Your response must be structured in three distinct sections in Markdown format.

## 1. Pedagogical Interpretation

**Summary:** Begin with a 2-3 sentence synthesis of the general state of skills, identifying critical areas of strength and weakness.

**Concerning Areas:** Identify the most alarming skills (those with the highest percentages). Explain in detail why these deficits are critical for the student's future development. Create causal links between skills.

**Stability Points:** Briefly mention the skills that seem acquired (those with the lowest percentages).

## 2. Actionable Recommendations

**Priority Recommendations:** Propose very concrete and targeted intervention strategies for the weakest skills.

**Implementation Strategies:** Provide advice on how to integrate these recommendations (differentiation, small groups, etc.).

**Assessment Recommendations:** Suggest a follow-up plan to measure progress.

## 3. Reliable Sources and References

To give credibility to your analysis, cite at least two recognized academic or institutional sources that support your recommendations. List them clearly at the end.""",
})

# ============ FRANÇAIS (fr) ============
translations["fr"].update({
    "gemini_prompt_template": """**Contexte :** Vous êtes un expert de renommée internationale en sciences de l'éducation, spécialisé dans l'analyse des évaluations à grande échelle comme l'EGRA. Votre analyse doit être rigoureuse, basée sur des données probantes, et vos recommandations doivent être pratiques pour les enseignants.

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

Pour crédibiliser votre analyse, citez au moins deux sources académiques ou institutionnelles reconnues qui soutiennent vos recommandations. Listez-les clairement à la fin.""",
})

# ============ ARABE (ar) ============
translations["ar"].update({
    "gemini_prompt_template": """**السياق:** أنت خبير مشهور دوليًا في علوم التربية، متخصص في تحليل التقييمات واسعة النطاق مثل EGRA. يجب أن يكون تحليلك صارمًا ومستندًا إلى الأدلة، ويجب أن تكون توصياتك عملية للمعلمين.

**البيانات الأولية للتحليل:** يعرض الجدول أدناه نسبة الطلاب الذين حصلوا على درجة صفر لعدة مهام تقييم أساسية. تمثل الدرجة الصفرية غيابًا تامًا للمهارة المقاسة.

```markdown
{data_as_markdown}
```

**مهمتك:** اكتب تقرير تحليل تشخيصي شامل باللغة العربية. يجب أن تكون إجابتك منظمة في ثلاثة أقسام متميزة بتنسيق Markdown.

## 1. التفسير التربوي

**الملخص:** ابدأ بتوليف من 2-3 جمل حول الحالة العامة للمهارات، مع تحديد المجالات الحرجة للقوة والضعف.

**المناطق المثيرة للقلق:** حدد المهارات الأكثر إثارة للقلق (تلك التي لديها أعلى النسب المئوية). اشرح بالتفصيل لماذا هذه العجز حرجة لتطور الطالب المستقبلي. أنشئ روابط سببية بين المهارات.

**نقاط الاستقرار:** اذكر بإيجاز المهارات التي تبدو مكتسبة (تلك التي لديها أدنى النسب المئوية).

## 2. التوصيات القابلة للتنفيذ

**التوصيات ذات الأولوية:** اقترح استراتيجيات تدخل محددة وموجهة جدًا للمهارات الأضعف.

**استراتيجيات التنفيذ:** قدم نصائح حول كيفية دمج هذه التوصيات (التمايز، المجموعات الصغيرة، إلخ).

**توصيات التقييم:** اقترح خطة متابعة لقياس التقدم.

## 3. مصادر ومراجع موثوقة

لإضفاء المصداقية على تحليلك، استشهد بمصدرين أكاديميين أو مؤسسيين معترف بهما على الأقل يدعمان توصياتك. اذكرهما بوضوح في النهاية.""",
})