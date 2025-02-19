import json
from models.class_book import Livro

class FileManager:
    
    def __init__(self, file_path):
        self.file_path = file_path

    def carregar_livros(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                books_data = json.load(file)
                return [Livro(**livro) for livro in books_data]
        except FileNotFoundError:
            with open(self.file_path, 'w') as file:
                json.dump([], file)
            return []

    def salvar_livros(self, livros):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump([livro.to_dict() for livro in livros], file, indent=4, ensure_ascii=False)