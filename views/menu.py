from utils.ansi_colors import RESET, RED, GREEN, YELLOW, BLUE, CYAN, WHITE
from controllers.library_controller import LibraryController
import os


def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

class Menu:
    def __init__(self, controller):
        self.controller = controller

    def mostrar_menu(self):
        print(CYAN + "--- Bem-Vindo a Biblioteca Digital ---\n" + RESET)
        print(GREEN + "[1] Adicionar novos livros ao acervo." + RESET)
        print(YELLOW + "[2] Listar e visualizar detalhes dos livros cadastrados." + RESET)
        print(BLUE + "[3] Editar informações de um livro existente." + RESET)
        print(RED + "[4] Remover um livro do acervo." + RESET)
        print(WHITE + "[5] Sair" + RESET)

    def run(self):
        exit = False
        while not exit:
            self.mostrar_menu()
            option = input("Escolha uma opção: ")

            clear_screen()
            match option:
                case "1":
                    self.adicionar_livro()
                case "2":
                    self.listar_livros()
                case "3":
                    self.editar_livro()
                case "4":
                    self.remover_livro()
                case "5":
                    print("Saindo do programa...")
                    exit = True
                case _:
                    print("Tente novamente, digite uma opção válida por favor!\n")

    def adicionar_livro(self):
        titulo = input("Título: ")
        autor = input("Autor: ")
        ano_publicacao = input("Ano de Publicação: ")
        categoria = input("Categoria: ")
        editora = input("Editora: ")
        self.controller.cadastrar_livro(titulo, autor, ano_publicacao, categoria, editora)

    def listar_livros(self):
        self.controller.listar_livros()

    def editar_livro(self):
        id_livro = (input("ID do livro a ser editado: ")) 
        titulo = input("Novo Título (pressione Enter para manter o atual): ")
        autor = input("Novo Autor (pressione Enter para manter o atual): ")
        ano_publicacao = input("Novo Ano de Publicação (pressione Enter para manter o atual): ")
        categoria = input("Nova Categoria (pressione Enter para manter o atual): ")
        editora = input("Nova Editora (pressione Enter para manter o atual): ")
        self.controller.editar_livro(id_livro, titulo, autor, ano_publicacao, categoria, editora)

    def remover_livro(self):
        id_livro = int(input("ID do livro a ser removido: "))
        self.controller.remover_livro(id_livro)