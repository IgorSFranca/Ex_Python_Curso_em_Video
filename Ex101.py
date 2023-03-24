def voto(ano):
    """ Função que recebe como parâmetro o ano de nascimento de uma pessoa, 
    retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO 
    nas eleições.
    """
    from datetime import date
    idade = date.today().year - ano
    if 16 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    elif idade < 16:
        return f'com {idade} anos: VOTO NEGADO'
    else:
        return f'com {idade} anos: VOTO OPCIONAL'

print('-'*30)
print(voto(int(input('Em que ano você nasceu: '))))