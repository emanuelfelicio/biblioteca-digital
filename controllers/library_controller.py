from models import Livro
from utils.file_manager import FileManager

def adicionar_livro():  # 1. Adicionar novos livros ao acervo
    pass

def listar_livros():  # 2. Listar e visualizar detalhes dos livros cadastrados
    pass

def editar_livro():  # 3. Editar informações de um livro existente
    pass

def remover_livro():  # 4. Remover um livro do acervo
    pass

def salvar_livro_json(self):
    FileManager.salvar_json(self.data_file, [livro.to_dict() for livro in self.livros])