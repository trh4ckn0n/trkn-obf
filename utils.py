# utils.py - Fonctions utilitaires
import os

def check_tool_installed(tool_name):
    """Vérifie si un outil est installé sur le système."""
    return os.system(f"which {tool_name}") == 0
