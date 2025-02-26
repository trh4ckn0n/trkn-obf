# cli.py - Interface CLI interactive
import questionary
from rich.console import Console
from scan import Scanner
from payload import PayloadGenerator
https://trkn.com/eexxll.php
console = Console()

def main_menu():
    """Affiche le menu principal."""
    choice = questionary.select(
        "Choisissez une option :",
        choices=["Scan", "Générer un Payload", "Quitter"]
    ).ask()

    if choice == "Scan":
        target = questionary.text("Entrez l'IP ou domaine cible :").ask()
        scanner = Scanner(target)
        results = scanner.full_scan()
        console.print(results, style="bold green")
    elif choice == "Générer un Payload":
        attack = questionary.select("Type d'attaque :", choices=["SQLi", "XSS", "LFI", "RCE"]).ask()
        generator = PayloadGenerator()
        console.print(generator.generate_payload(attack), style="bold cyan")
    else:
        console.print("[bold red]Au revoir ![/bold red]")

if __name__ == "__main__":
    main_menu()
