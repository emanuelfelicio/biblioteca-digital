import json
import os

class FileManager:
    @staticmethod
    def salvar_json(arquivo, dados):
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4)
    
    """Salva um dicionário em um arquivo JSON."""

    def carregar_json(arquivo):
        if not os.path.exists(arquivo):
            return []
        with open(arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
        
    """Carrega um dicionário de um arquivo JSON."""