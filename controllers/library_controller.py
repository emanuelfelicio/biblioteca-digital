from models.class_book import Livro
from utils.ansi_colors import RESET, RED, GREEN, YELLOW, BLUE, CYAN, WHITE
from utils.file_manager import FileManager

class LibraryController:
    def __init__(self):
        self.file_manager = FileManager('data/books.json')
        self.livros = self.file_manager.carregar_livros()

    def cadastrar_livro(self, titulo, autor, ano_publicacao, categoria, editora):  # 1. Adicionar novos livros ao acervo

        '''Criando um objeto da classe Livro'''
        livro = Livro(len(self.livros) + 1, titulo, autor, ano_publicacao, categoria, editora)

        '''Adiciona o livro à lista e salva no JSON'''
        self.livros.append(livro)
        self.file_manager.salvar_livros(self.livros)

        print(GREEN + "\n--- ✅ Livro cadastrado com sucesso! --- \n" + RESET)

    def listar_livros(self):  # 2. Listar e visualizar detalhes dos livros cadastrados
        """Lista todos os livros cadastrados no acervo."""
        if not self.livros:
            print(RED + "📚 Nenhum livro cadastrado no momento." + RESET)
            return

        print(BLUE + "\n📖 Lista de Livros Cadastrados:" + RESET)
        for livro in self.livros:
            print(f"""
            🆔 ID: {livro.id}
            📘 Título: {livro.titulo}
            ✍ Autor: {livro.autor}
            📅 Ano de Publicação: {livro.ano_publicacao}
            📚 Categoria: {livro.categoria}
            🏢 Editora: {livro.editora}
            """)

    def editar_livro():  # 3. Editar informações de um livro existente
        pass

    def remover_livro(self, id_livro):  # 4. Remover um livro do acervo
        for livro in self.livros:
            if livro.id == id_livro:
                self.livros.remove(livro)
                self.file_manager.salvar_livros(self.livros)
                print(GREEN + f"\n--- ✅ Livro '{livro.titulo}' removido com sucesso! ---" + RESET)
                return
        print(RED + "Livro não encontrado." + RESET)
