from datetime import date

def voto(ano):
    """ Função que recebe como parâmetro o ano de nascimento de uma pessoa, 
    retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO 
    nas eleições.
    """
    idade = date.today().year - ano
    print(f'Com {idade} anos: ', end='')
    if 18 <= idade < 65:
        print('VOTO OBRIGATÓRIO')
    elif idade < 18:
        print('VOTO NEGADO')
    else:
        print('VOTO OPCIONAL')

print('-'*30)
voto(int(input('Em que ano você nasceu: ')))