# payload.py - Génération de payloads IA
import openai
import random
from config import OPENAI_API_KEY

class PayloadGenerator:
    def __init__(self):
        self.api_key = OPENAI_API_KEY
        openai.api_key = self.api_key

    def generate_payload(self, attack_type):
        """Génère un payload basé sur le type d'attaque spécifié"""
        prompts = {
            "SQLi": "Génère un payload SQLi avancé contournant les protections WAF.",
            "XSS": "Génère un payload XSS efficace en JavaScript.",
            "LFI": "Génère un payload LFI permettant de lire des fichiers sensibles.",
            "RCE": "Génère un payload RCE permettant d'exécuter des commandes système."
        }
        if attack_type not in prompts:
            return "Type d'attaque non reconnu."

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompts[attack_type]}],
            temperature=0.7
        )
        return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    generator = PayloadGenerator()
    attack = input("Type d'attaque (SQLi, XSS, LFI, RCE) : ")
    print(generator.generate_payload(attack))
