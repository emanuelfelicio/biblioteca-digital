from datetime import datetime
from utils.ansi_colors import RED,RESET

def validar_ano_publicacao(ano_publicacao):

    """
    Valida se o ano de publicação não está vazio, se está no formato correto e dentro do intervalo permitido.

    """
    
    # verfica se está vazio
    if ano_publicacao:
        try:
            ano_int = int(ano_publicacao)
        except ValueError:
            raise ValueError(RED+"Erro: O ano de publicação deve conter apenas números."+RESET)
        
        # Verifica se o ano está dentro do intervalo permitido
        ano_atual = datetime.now().year  
        if ano_int < 1400 or ano_int > ano_atual:
            raise ValueError(RED+f"Erro: O ano de publicação deve estar entre 1400 e {ano_atual}."+RESET)
    else:
        raise ValueError (RED+"Erro: O ano de publicação não pode estar vazio."+RESET)

    return ano_publicacao

def validar_id_livro(id_livro):

    if not id_livro:  # verifica se id é vazio
        raise ValueError(RED+"Erro: O id não pode ser vazio"+RESET)
    
    try:
        id_int = int(id_livro)
    except ValueError:
        raise ValueError(RED+"Erro: O id deve conter apenas números."+RESET)
    
    if id_int<0:
        raise ValueError(RED+"Erro: O id não pode ser negativo."+RESET)
    
    return id_int

def validar_campo_nao_vazio(value,nome_campo):
     
    """
    Valida se o campo não está vazio.
    Descrição:
    Esta função verifica se o valor fornecido está vazio ou contém apenas espaços em branco.
    Se o campo estiver vazio, solicita ao usuário que insira um valor válido até que um valor não vazio seja fornecido.

    """
    while not value or len(value.strip()) == 0:
         print(RED + f"O campo {nome_campo} não pode estar vazio. Por favor, escreva novamente"+ RESET)
         value = input(f"{nome_campo}: ")
    return value
   