# 📚 Biblioteca Digital

Este é um projeto de Biblioteca Digital desenvolvido em Python. O sistema permite gerenciar um acervo de livros diretamente pelo terminal, utilizando um arquivo JSON para armazenamento dos dados. 

## Funcionalidades

- **📋 Menu**: Listagem de opções do programa.
- **➕ Criar**: Adicionar novos livros ao acervo.
- **🔍 Ler**: Listar e visualizar detalhes dos livros cadastrados.
- **✏️ Atualizar**: Editar informações de um livro existente.
- **❌ Deletar**: Remover um livro do acervo.

## Características dos Livros

- 🆔 ID (número único para identificação)
- 📘 Título
- ✍️ Autor
- 📅 Ano de publicação
- 📚 Categoria
- 🏢 Editora

## Estrutura do Projeto

```
biblioteca-digital/
├── controllers/
│   └── library_controller.py
├── data/
│   └── books.json
├── models/
│   └── class_book.py
├── utils/
│   ├── ansi_colors.py
│   └── file_manager.py
├── views/
│   └── menu.py
└── main.py
```

## Como Executar

1. Clone o repositório para a sua máquina local:
    ```sh
    git clone https://github.com/emanuelfelicio/biblioteca-digital.git
    ```

2. Navegue até o diretório do projeto:
    ```sh
    cd biblioteca-digital
    ```

3. Execute o programa:
    ```sh
    python main.py
    ```

## Exemplo de Uso

Ao executar o programa, você verá um menu com as opções disponíveis:

```
--- Bem-Vindo a Biblioteca Digital ---

[1] ➕ Adicionar novos livros ao acervo.
[2] 🔍 Listar livros cadastrados.
[3] ✏️ Editar informações de um livro existente.
[4] ❌ Remover um livro do acervo.
[5] Sair
```

Escolha uma opção digitando o número correspondente e siga as instruções fornecidas.

## Contribuições

Contribuições são bem-vindas! Se você deseja contribuir com este projeto, siga os passos abaixo:

1. Fork o repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas alterações (`git commit -m 'Adiciona nova feature'`).
4. Faça o push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## Licença

Este projeto no momento não possui licença.
