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
            print(valor, end='')
            if valor > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return f'{total}'


n = int(input('Digite um número para saber o fatorial: '))
mostrar = str(input('Quer exitir o cálculo? [S/N] ')).strip().upper()
if mostrar == 'S':
    mostrar = True
elif mostrar == 'N':
    mostrar = False
print(fatorial(n, show=mostrar))