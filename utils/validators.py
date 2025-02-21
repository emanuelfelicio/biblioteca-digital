from datetime import datetime

def validar_ano_publicacao(ano_publicacao):

    """
    Valida se o ano de publicação está no formato correto e dentro do intervalo permitido.

    """
    # Tenta converter para inteiro para validar o intervalo
    try:
        ano_int = int(ano_publicacao)
    except ValueError:
        raise ValueError("O ano de publicação deve conter apenas números.")

    # Verifica se o ano está dentro do intervalo permitido
    ano_atual = datetime.now().year  
    if ano_int < 1400 or ano_int > ano_atual:
        raise ValueError(f"O ano de publicação deve estar entre 1400 e {ano_atual}.")

    
    return ano_publicacao

def validar_id_livro(id_livro):

    if not id_livro:  # verifica se id é vazio
        raise ValueError("O id não pode ser vazio")
    
    try:
        id_int = int(id_livro)
    except ValueError:
        raise ValueError("O id deve conter apenas números.")
    
    if id_int<0:
        raise ValueError("O id não pode ser negativo.")
    
    return id_int

def validar_campo_nao_vazio(value,nome_campo):
    if not value:
        raise ValueError(f"o campo {nome_campo} não pode estar vazio")
    return value