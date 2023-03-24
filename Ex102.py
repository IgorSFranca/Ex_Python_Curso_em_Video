def fatorial(n, show):
    """
    Calcula o Fatorial de um número. 
    param n: O número a ser calculado 
    param show: (opcional) Mostrar ou não a conta
    return: O valor do Fatorial de um número n
    """
    total = 1
    for valor in range (n, 0, -1):
        total *= valor
        if show == True:
            print(valor, end=' x ')
    return f'= {total}'


print(fatorial(5, show=True))
help(fatorial)