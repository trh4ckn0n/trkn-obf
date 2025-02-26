import requests
import re
import os

# Récupérer le token GitHub depuis les secrets
GITHUB_TOKEN = os.getenv("GH_TOKEN")  # Utilisation du secret GitHub dans l'environnement
if not GITHUB_TOKEN:
    raise ValueError("Le token GH_TOKEN n'est pas défini dans les secrets GitHub.")

BASE_URL = "https://api.github.com"

# Expression régulière pour trouver les URLs
url_pattern = r'(https?://\S+)'

# Fonction pour récupérer tous les repos publics d'un utilisateur
def get_public_repositories(username):
    repos = []
    page = 1
    while True:
        response = requests.get(
            f"{BASE_URL}/users/{username}/repos",
            params={"page": page, "per_page": 100},  # Limite de 100 repos par page
            headers={"Authorization": f"token {GITHUB_TOKEN}"}
        )
        if response.status_code != 200:
            print(f"Erreur lors de la récupération des repos: {response.status_code}")
            break

        repos_data = response.json()
        if not repos_data:
            break

        repos.extend(repos_data)
        page += 1
    return repos

# Fonction pour récupérer le contenu d'un fichier dans un repo
def get_file_content(owner, repo, file_path):
    url = f"{BASE_URL}/repos/{owner}/{repo}/contents/{file_path}"
    response = requests.get(url, headers={"Authorization": f"token {GITHUB_TOKEN}"})
    if response.status_code == 200:
        file_data = response.json()
        return requests.get(file_data["download_url"]).text
    else:
        return None

# Fonction pour analyser les fichiers dans chaque repo et rechercher les URLs
def find_urls_in_repos(username):
    repos = get_public_repositories(username)
    all_urls = {}

    for repo in repos:
        repo_name = repo["name"]
        print(f"Analyse du repo: {repo_name}")

        # Listes des fichiers dans le repo
        contents_url = repo["contents_url"].replace("{+path}", "")
        response = requests.get(contents_url, headers={"Authorization": f"token {GITHUB_TOKEN}"})

        if response.status_code != 200:
            print(f"Erreur lors de la récupération des fichiers du repo {repo_name}: {response.status_code}")
            continue

        files = response.json()
        for file in files:
            file_path = file["path"]
            if file_path.endswith(('.py', '.js', '.html', '.java')):  # Filtrer par extensions de fichiers
                print(f"  Recherche d'URLs dans {file_path}...")
                file_content = get_file_content(repo["owner"]["login"], repo_name, file_path)
                if file_content:
                    urls = re.findall(url_pattern, file_content)
                    if urls:
                        all_urls[f"{repo_name}/{file_path}"] = urls

    return all_urls

# Fonction pour afficher les résultats
def display_urls(urls_found):
    if not urls_found:
        print("Aucune URL trouvée dans les repos.")
        return

    print("URLs trouvées dans les repos publics :")
    for file_path, urls in urls_found.items():
        print(f"\nDans {file_path}:")
        for url in urls:
            print(f"  - {url}")

# Exemple d'utilisation
if __name__ == "__main__":
    username = "ton_nom_utilisateur_github"  # Remplacer par ton nom d'utilisateur GitHub
    print(f"Recherche des URLs dans les repos publics de {username}...\n")
    
    urls_found = find_urls_in_repos(username)
    display_urls(urls_found)
