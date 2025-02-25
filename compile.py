# compile.py - Compilation avec Nuitka
import os

def compile_with_nuitka():
    """Compile le projet avec Nuitka"""
    os.system("nuitka --onefile --follow-imports main.py")

if __name__ == "__main__":
    compile_with_nuitka()
