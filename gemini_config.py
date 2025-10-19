# ==================================================
# File: gemini_config.py
# Gemini API Configuration Manager for ADP v3.0
# Version Complète avec Support Sidebar + Inline
# ==================================================

import os
import streamlit as st
from pathlib import Path
from typing import Optional, Tuple
from dataclasses import dataclass

try:
    import google.generativeai as genai
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False
    genai = None


@dataclass
class GeminiStatus:
    """Status de configuration Gemini"""
    configured: bool
    available: bool
    api_key_set: bool
    model_loaded: bool
    error_message: Optional[str] = None


class GeminiConfigManager:
    """Gestionnaire de configuration pour Gemini API"""
    
    ENV_FILE = Path(".env")
    SESSION_KEY = "gemini_api_key"
    MODEL_NAME = "gemini-2.5-pro"  # ✅ Modèle actuel le plus performant
    # Alternative rapide: "gemini-1.5-flash"
    
    def __init__(self):
        self.model = None
        self._initialize_from_env()
    
    def _initialize_from_env(self) -> None:
        """Charge la clé API depuis .env ou variables d'environnement"""
        # Essayer session state d'abord
        if self.SESSION_KEY in st.session_state:
            api_key = st.session_state[self.SESSION_KEY]
            if api_key:
                self._configure_genai(api_key)
                return
        
        # Essayer fichier .env
        if self.ENV_FILE.exists():
            api_key = self._load_from_env_file()
            if api_key:
                st.session_state[self.SESSION_KEY] = api_key
                self._configure_genai(api_key)
                return
        
        # Essayer variable d'environnement système
        api_key = os.getenv('GEMINI_API_KEY')
        if api_key:
            st.session_state[self.SESSION_KEY] = api_key
            self._configure_genai(api_key)
    
    def _load_from_env_file(self) -> Optional[str]:
        """Charge la clé depuis le fichier .env"""
        try:
            with open(self.ENV_FILE, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('GEMINI_API_KEY='):
                        key = line.split('=', 1)[1].strip().strip('"').strip("'")
                        return key if key else None
        except Exception:
            pass
        return None
    
    def _save_to_env_file(self, api_key: str) -> bool:
        """Sauvegarde la clé dans le fichier .env"""
        try:
            # Lire le contenu existant
            existing_lines = []
            if self.ENV_FILE.exists():
                with open(self.ENV_FILE, 'r') as f:
                    existing_lines = [line for line in f if not line.startswith('GEMINI_API_KEY=')]
            
            # Écrire avec la nouvelle clé
            with open(self.ENV_FILE, 'w') as f:
                f.write("# Africa Demographics Platform Configuration\n")
                f.write("# Auto-generated file\n\n")
                f.write(f'GEMINI_API_KEY="{api_key}"\n')
                
                # Réécrire les autres lignes
                for line in existing_lines:
                    if line.strip() and not line.startswith('#'):
                        f.write(line)
            
            return True
        except Exception:
            return False
    
    def _configure_genai(self, api_key: str) -> bool:
        """Configure l'API Gemini avec la clé fournie"""
        if not GENAI_AVAILABLE:
            return False
        
        try:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel(self.MODEL_NAME)
            return True
        except Exception:
            self.model = None
            return False
    
    def set_api_key(self, api_key: str, save_to_file: bool = True) -> Tuple[bool, str]:
        """
        Définit la clé API Gemini
        
        Returns:
            Tuple[bool, str]: (succès, message)
        """
        if not api_key or not api_key.strip():
            return False, "Clé API vide"
        
        api_key = api_key.strip()
        
        # Validation basique du format
        if not api_key.startswith('AIza'):
            return False, "Format de clé invalide (doit commencer par 'AIza')"
        
        if len(api_key) < 30:
            return False, "Clé trop courte, vérifiez votre saisie"
        
        # Tester la configuration
        if not GENAI_AVAILABLE:
            return False, "Module google-generativeai non installé"
        
        try:
            genai.configure(api_key=api_key)
            test_model = genai.GenerativeModel(self.MODEL_NAME)
            
            # Test simple avec configuration minimale
            response = test_model.generate_content(
                "Hello",
                generation_config=genai.GenerationConfig(
                    max_output_tokens=10,
                    temperature=0.1
                )
            )
            
            # Si on arrive ici, la clé est valide
            st.session_state[self.SESSION_KEY] = api_key
            self.model = test_model
            
            # Sauvegarder si demandé
            if save_to_file:
                self._save_to_env_file(api_key)
            
            return True, "✅ Clé API validée et configurée"
            
        except Exception as e:
            error_msg = str(e)
            if "API_KEY_INVALID" in error_msg or "invalid" in error_msg.lower():
                return False, "❌ Clé API invalide"
            elif "quota" in error_msg.lower() or "resource_exhausted" in error_msg.lower():
                return False, "❌ Quota API dépassé"
            elif "permission" in error_msg.lower():
                return False, "❌ Permissions insuffisantes"
            else:
                return False, f"❌ Erreur: {error_msg[:100]}"
    
    def get_status(self) -> GeminiStatus:
        """Retourne le status actuel de la configuration"""
        api_key_set = bool(st.session_state.get(self.SESSION_KEY))
        
        return GeminiStatus(
            configured=bool(self.model),
            available=GENAI_AVAILABLE,
            api_key_set=api_key_set,
            model_loaded=bool(self.model),
            error_message=None if GENAI_AVAILABLE else "Module google-generativeai non installé"
        )
    
    def clear_api_key(self) -> None:
        """Supprime la clé API"""
        if self.SESSION_KEY in st.session_state:
            del st.session_state[self.SESSION_KEY]
        self.model = None
    
    def get_model(self):
        """Retourne le modèle Gemini configuré"""
        return self.model
    
    def get_generation_config(self) -> dict:
        """
        Retourne la configuration de génération pour les requêtes Gemini
        
        Returns:
            dict: Configuration de génération
        """
        return {
            "temperature": 0.7,
            "max_output_tokens": 8000,
            "top_p": 0.95,
            "top_k": 40
        }
    
    def render_config_ui(self, ml_config) -> None:
        """
        Affiche l'interface de configuration dans le sidebar (pour main.py)
        
        Args:
            ml_config: Instance de MultilingualConfig pour traductions
        """
        is_french = ml_config.get_language() == "fr"
        status = self.get_status()
        
        # Header
        st.sidebar.markdown("## 🤖 Gemini AI")
        
        # Status indicator
        if status.configured and status.model_loaded:
            st.sidebar.success("✅ API configurée et opérationnelle" if is_french else "✅ API configured and operational")
        elif status.api_key_set and not status.model_loaded:
            st.sidebar.warning("⚠️ Clé présente mais modèle non chargé" if is_french else "⚠️ Key present but model not loaded")
        else:
            st.sidebar.info("ℹ️ Configuration requise pour rapports IA" if is_french else "ℹ️ Configuration required for AI reports")
        
        # Configuration expander
        with st.sidebar.expander("⚙️ Configuration", expanded=not status.configured):
            
            if not GENAI_AVAILABLE:
                st.error(
                    "❌ Module google-generativeai non installé\n\n"
                    "Installation: `pip install google-generativeai`"
                    if is_french else
                    "❌ google-generativeai module not installed\n\n"
                    "Install: `pip install google-generativeai`"
                )
                return
            
            # Input clé API
            current_key = st.session_state.get(self.SESSION_KEY, "")
            masked_key = current_key[:10] + "..." + current_key[-4:] if len(current_key) > 14 else ""
            
            api_key_input = st.text_input(
                "Clé API Gemini" if is_french else "Gemini API Key",
                type="password",
                value="" if status.configured else "",
                placeholder=masked_key if masked_key else "AIzaSy...",
                help="Obtenir sur: https://makersuite.google.com/app/apikey" if is_french else "Get from: https://makersuite.google.com/app/apikey",
                key="sidebar_api_key_input"
            )
            
            # Options de sauvegarde
            save_to_file = st.checkbox(
                "💾 Sauvegarder dans .env" if is_french else "💾 Save to .env file",
                value=True,
                help="Sauvegarder la clé localement pour réutilisation" if is_french else "Save key locally for reuse",
                key="sidebar_save_checkbox"
            )
            
            # Boutons d'action
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("✅ Valider" if is_french else "✅ Validate", use_container_width=True, key="sidebar_validate_btn"):
                    if api_key_input:
                        with st.spinner("Validation..." if is_french else "Validating..."):
                            success, message = self.set_api_key(api_key_input, save_to_file)
                            if success:
                                st.success(message)
                                st.rerun()
                            else:
                                st.error(message)
                    else:
                        st.warning("Veuillez saisir une clé API" if is_french else "Please enter an API key")
            
            with col2:
                if status.configured:
                    if st.button("🗑️ Effacer" if is_french else "🗑️ Clear", use_container_width=True, key="sidebar_clear_btn"):
                        self.clear_api_key()
                        st.success("Clé supprimée" if is_french else "Key removed")
                        st.rerun()
            
            # Lien d'aide
            st.markdown("---")
            st.markdown(
                "[📖 Comment obtenir une clé API](https://ai.google.dev/gemini-api/docs/api-key)" if is_french else
                "[📖 How to get an API key](https://ai.google.dev/gemini-api/docs/api-key)"
            )
            
            # Info modèle utilisé
            if status.configured:
                st.caption(f"Modèle: {self.MODEL_NAME}")
    
    def render_inline_config_ui(self, t: dict, language: str) -> None:
        """
        Affiche l'interface de configuration dans le corps de la page (pour analyse2.py)
        
        Args:
            t: Dictionnaire de traductions
            language: Code de langue (en/fr/ar/es)
        """
        is_french = language == "fr"
        status = self.get_status()
        
        if not GENAI_AVAILABLE:
            st.error(
                "❌ Module google-generativeai non installé\n\n"
                "Installation: `pip install google-generativeai`"
                if is_french else
                "❌ google-generativeai module not installed\n\n"
                "Install: `pip install google-generativeai`"
            )
            return
        
        # Input clé API
        current_key = st.session_state.get(self.SESSION_KEY, "")
        masked_key = current_key[:10] + "..." + current_key[-4:] if len(current_key) > 14 else ""
        
        api_key_input = st.text_input(
            t.get("gemini_api_key_label", "🔑 Clé API Gemini" if is_french else "🔑 Gemini API Key"),
            type="password",
            value="" if status.configured else "",
            placeholder=masked_key if masked_key else "AIzaSy...",
            help=t.get("gemini_api_help", 
                "Obtenir sur: https://makersuite.google.com/app/apikey" if is_french else 
                "Get from: https://makersuite.google.com/app/apikey"),
            key="gemini_inline_api_key"
        )
        
        # Options de sauvegarde
        save_to_file = st.checkbox(
            t.get("save_to_env", "💾 Sauvegarder dans .env" if is_french else "💾 Save to .env file"),
            value=True,
            help=t.get("save_to_env_help",
                "Sauvegarder la clé localement pour réutilisation" if is_french else 
                "Save key locally for reuse"),
            key="gemini_inline_save"
        )
        
        # Boutons d'action
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button(
                t.get("validate_button", "✅ Valider" if is_french else "✅ Validate"), 
                use_container_width=True,
                key="gemini_inline_validate"
            ):
                if api_key_input:
                    with st.spinner(t.get("validating", "Validation..." if is_french else "Validating...")):
                        success, message = self.set_api_key(api_key_input, save_to_file)
                        if success:
                            st.success(message)
                            st.rerun()
                        else:
                            st.error(message)
                else:
                    st.warning(t.get("enter_api_key", 
                        "Veuillez saisir une clé API" if is_french else "Please enter an API key"))
        
        with col2:
            if status.configured:
                if st.button(
                    t.get("clear_button", "🗑️ Effacer" if is_french else "🗑️ Clear"), 
                    use_container_width=True,
                    key="gemini_inline_clear"
                ):
                    self.clear_api_key()
                    st.success(t.get("key_removed", "Clé supprimée" if is_french else "Key removed"))
                    st.rerun()
        
        # Lien d'aide
        st.markdown(
            f"[📖 {t.get('how_to_get_api_key', 'Comment obtenir une clé API' if is_french else 'How to get an API key')}]"
            f"(https://ai.google.dev/gemini-api/docs/api-key)"
        )
        
        # Info modèle utilisé
        if status.configured:
            st.caption(f"✓ {t.get('model_label', 'Modèle')}: {self.MODEL_NAME}")


# ==================================================
# SINGLETON INSTANCE
# ==================================================

_gemini_config_instance = None

def get_gemini_config() -> GeminiConfigManager:
    """Retourne l'instance singleton du gestionnaire de config"""
    global _gemini_config_instance
    if _gemini_config_instance is None:
        _gemini_config_instance = GeminiConfigManager()
    return _gemini_config_instance