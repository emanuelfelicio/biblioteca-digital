from controllers import library_controller
from utils.Ansi_colors import RESET, RED, GREEN, YELLOW, BLUE, CYAN, WHITE
import os

def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

def menu():
    exit = False
    print(CYAN + "--- Bem-Vindo a Biblioteca Digital ---\n" + RESET)
    while exit == False:

        print(GREEN + "[1] Adicionar novos livros ao acervo." + RESET)
        print(YELLOW + "[2] Listar e visualizar detalhes dos livros cadastrados." + RESET)
        print(BLUE + "[3] Editar informações de um livro existente." + RESET)
        print(RED + "[4] Remover um livro do acervo."+ RESET)
        print(WHITE + "[5] Sair" + RESET)

        option = input("Escolha uma opção: ")

        clear_screen()
        match option:
            case "1":
               library_controller.adicionar_livro()
            case "2":
                library_controller.listar_livros()
            case "3":
                library_controller.editar_livro()
            case "4":
                library_controller.remover_livro()
            case "5":
                print("Saindo do programa...")
                exit = True
            case _ :
                print("Tente novamente, digite uma opção válida por favor!\n")
menu()
