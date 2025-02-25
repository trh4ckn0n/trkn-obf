# obfuscation.py - Sécurisation et obfuscation
import os

def obfuscate_with_pyarmor():
    """Obfuscation avec PyArmor"""
    os.system("pyarmor pack -e ' --onefile' main.py")

def obfuscate_with_hyperion():
    """Obfuscation avec Hyperion (nécessite un environnement Windows)"""
    os.system("Hyperion.exe main.exe")

if __name__ == "__main__":
    obfuscate_with_pyarmor()
