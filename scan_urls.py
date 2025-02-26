import os
import re
import subprocess

# Fonction pour trouver les URLs dans un fichier
def find_urls_in_file(file_path):
    urls = []
    url_pattern = r'(https?://\S+)'  # Expression régulière pour trouver les URLs
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            urls = re.findall(url_pattern, content)
    except Exception as e:
        print(f"Erreur lors de l'ouverture du fichier {file_path}: {e}")
    return urls

# Fonction pour analyser un répertoire et trouver des URLs
def scan_directory_for_urls(directory):
    urls_found = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.py', '.js', '.html', '.java')):  # Types de fichiers à scanner
                file_path = os.path.join(root, file)
                urls = find_urls_in_file(file_path)
                if urls:
                    urls_found[file_path] = urls
                    print(f"URLs trouvées dans {file_path}: {urls}")  # Debug: affiche les URLs trouvées
    return urls_found

# Fonction pour mettre à jour le README.md avec les résultats
def update_readme_with_urls(urls_found):
    readme_path = "README.md"
    print(f"Ouverture du fichier README.md à {readme_path}")  # Debug: vérifie que le fichier est ouvert
    try:
        # Lire le contenu actuel du README
        with open(readme_path, 'r', encoding='utf-8') as readme:
            content = readme.read()

        # Remplacer l'ancienne section des URLs si elle existe
        content = re.sub(r'## URLs et Endpoints Sensibles Trouvés.*?##', '', content, flags=re.DOTALL)

        # Ajouter la nouvelle section avec les URLs trouvées
        new_content = content + "\n## URLs et Endpoints Sensibles Trouvés\n"
        for file_path, urls in urls_found.items():
            new_content += f"### Fichier: {file_path}\n"
            for url in urls:
                new_content += f"- {url}\n"
        new_content += "\n"

        # Écrire le contenu mis à jour dans le README.md
        with open(readme_path, 'w', encoding='utf-8') as readme:
            readme.write(new_content)

        print("Modifications apportées au README.md")  # Debug: vérifie que le fichier est bien modifié

    except Exception as e:
        print(f"Erreur lors de l'écriture dans le fichier README.md: {e}")

# Fonction pour ajouter, commiter et pousser les changements dans Git
def commit_and_push_changes():
    try:
        # Vérifie l'état des fichiers dans Git
        subprocess.run(["git", "status"], check=True)
        
        # Récupère les dernières modifications du dépôt distant avant de pousser
        subprocess.run(["git", "pull", "--rebase", "origin", "main"], check=True)  # Utilisation de rebase pour garder l'historique propre
        
        # Ajouter les changements
        subprocess.run(["git", "add", "README.md"], check=True)
        
        # Committer les changements
        subprocess.run(['git', 'commit', '-m', 'Mise à jour des URLs dans README.md'], check=True)  # Correction du message de commit
        
        # Pousser les changements
        subprocess.run(['git', 'push', 'origin', 'main'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution des commandes Git : {e}")

if __name__ == "__main__":
    # Dossier à scanner (vous pouvez spécifier un dossier particulier ou tout le repo)
    directory_to_scan = "./"
    urls_found = scan_directory_for_urls(directory_to_scan)
    if urls_found:
        update_readme_with_urls(urls_found)
        commit_and_push_changes()
    else:
        print("Aucune URL trouvée.")
