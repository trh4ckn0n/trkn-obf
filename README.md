# PentestAI - Outil de Pentesting avec IA

## Fonctionnalités :
- Scan et reconnaissance : Nmap, Nuclei, Shodan
- Génération de payloads IA : SQLi, XSS, LFI, RCE
- Interface CLI interactive
- Obfuscation avancée et compilation en C

## Installation :
1. Installer les dépendances :  
   ```bash
   pip install -r requirements.txt
   ```

2. Executer l'outil :
   ```bash
   python main.py
   ```

## Obfuscation :
   ```bash
   python obfuscation.py 
   ```

## Compilation :
   ```bash
   python compile.py
   ```

## 📌 Utilisation
 
### 1️⃣ **Scanner une cible**
 
Lancez un scan sur une IP ou un domaine :

 `python main.py ` 
 
Sélectionnez **"Scan"**, entrez l'adresse cible, puis laissez l'outil analyser les vulnérabilités avec Nmap, Nuclei et Shodan.
  
### 2️⃣ **Générer un payload d'attaque**
 
Lancez le mode génération de payloads IA :

 `python main.py ` 
 
Sélectionnez **"Générer un Payload"**, puis choisissez une attaque parmi :
 
 
- **SQLi** : Injection SQL
 
- **XSS** : Cross-Site Scripting
 
- **LFI** : Local File Inclusion
 
- **RCE** : Remote Code Execution
  
### 3️⃣ **Obfuscation et protection du code**
 
Utilisez `PyArmor` et `Hyperion` pour empêcher la rétro-ingénierie :

 `python obfuscation.py ` 
 
- **Mode PyArmor** : Protection légère contre le reverse engineering
 
- **Mode Hyperion** : Chiffrement avancé du binaire (Windows uniquement)
 

  
### 4️⃣ **Compilation en C pour plus de sécurité**
 
Convertissez le script en binaire natif avec **Nuitka** :

 `python compile.py ` 
 
Cela empêche l’accès direct au code source Python.
  
## 🔧 Personnalisation
 
Vous pouvez modifier le fichier 
`config.py` pour :
 
 
- Ajouter vos propres clés API (`SHODAN_API_KEY`, `OPENAI_API_KEY`)
 
- Changer le chemin de `Nuclei`
 
- Modifier le comportement des scans
 

  
## 🚀 Améliorations futures
 
 
- **Ajout de nouvelles attaques IA** : SSRF, XXE, Command Injection
 
- **Interface Web** : Dashboard interactif
 
- **Automatisation** : Lancement automatique sur plusieurs cibles
 

  
## ❓ Dépannage
 
**Problème : "shodan.APIError: Invalid API Key"** ➡ Vérifiez votre clé dans `config.py` et assurez-vous qu'elle est valide.
 
**Problème : "nuclei: command not found"** ➡ Assurez-vous que `nuclei` est bien installé et que son chemin est défini dans `config.py`.
 
**Problème : "Erreur lors de la compilation Nuitka"** ➡ Vérifiez que `gcc` et `Nuitka` sont bien installés :

 `sudo apt install gcc pip install nuitka `  
  
## 👨‍💻 Dev
 
Développé par **Trhacknon* Contributions bienvenues ! Ouvrez une **issue** ou un **pull request** sur GitHub.







## URLs et Endpoints Sensibles Trouvés
### Fichier: ./cli.py
- https://trkn.com/eell.php

