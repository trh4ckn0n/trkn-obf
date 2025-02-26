import os
import re

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
    return urls_found

# Fonction pour mettre à jour le README.md avec les résultats
def update_readme_with_urls(urls_found):
    readme_path = "README.md"
    try:
        with open(readme_path, 'a', encoding='utf-8') as readme:
            readme.write("\n## URLs et Endpoints Sensibles Trouvés\n")
            for file_path, urls in urls_found.items():
                readme.write(f"### Fichier: {file_path}\n")
                for url in urls:
                    readme.write(f"- {url}\n")
            readme.write("\n")
    except Exception as e:
        print(f"Erreur lors de l'écriture dans le fichier README.md: {e}")

if __name__ == "__main__":
    # Dossier à scanner (vous pouvez spécifier un dossier particulier ou tout le repo)
    directory_to_scan = "./"
    urls_found = scan_directory_for_urls(directory_to_scan)
    if urls_found:
        update_readme_with_urls(urls_found)
    else:
        print("Aucune URL trouvée.")
