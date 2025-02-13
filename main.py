import crud
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
    print("Bem-Vindo a Biblioteca\n")
    while exit == False:
        print("1.Adicionar novos livros ao acervo.")
        print("2.Listar e visualizar detalhes dos livros cadastrados.")
        print("3.Editar informações de um livro existente.")
        print("4.Remover um livro do acervo.")
        print("5.Sair")
        option = input("Escolha uma opção: ")
        clear_screen()
        match option:
            case "1":
               crud.adicionar_livro()
            case "2":
                crud.listar_livros()
            case "3":
                crud.editar_livro()
            case "4":
                crud.remover_livro()
            case "5":
                print("Saindo do programa...")
                exit = True
            case _ :
                print("Tente novamente, digite uma opção válida por favor!\n")

menu()
