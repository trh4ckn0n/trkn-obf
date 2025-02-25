# scan.py - Module de reconnaissance et scan
import os
import subprocess
import shodan
import nmap
import requests
from concurrent.futures import ThreadPoolExecutor

# Charger la clé API Shodan depuis config.py
from config import SHODAN_API_KEY

class Scanner:
    def __init__(self, target):
        self.target = target
        self.shodan_api = shodan.Shodan(SHODAN_API_KEY)

    def scan_nmap(self, scan_type='-sV'):
        """Exécute un scan Nmap sur la cible"""
        nm = nmap.PortScanner()
        nm.scan(self.target, arguments=scan_type)
        return nm[self.target] if self.target in nm.all_hosts() else {}

    def scan_nuclei(self):
        """Exécute un scan Nuclei en ligne de commande"""
        command = f"nuclei -u {self.target} -silent"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout

    def scan_shodan(self):
        """Récupère les informations Shodan sur la cible"""
        try:
            return self.shodan_api.host(self.target)
        except shodan.APIError as e:
            return f"Erreur Shodan : {e}"

    def full_scan(self):
        """Effectue tous les scans en parallèle"""
        with ThreadPoolExecutor() as executor:
            results = {
                "nmap": executor.submit(self.scan_nmap),
                "nuclei": executor.submit(self.scan_nuclei),
                "shodan": executor.submit(self.scan_shodan)
            }
        return {k: v.result() for k, v in results.items()}

if __name__ == "__main__":
    target = input("Entrez l'IP ou domaine cible : ")
    scanner = Scanner(target)
    results = scanner.full_scan()
    print(results)
