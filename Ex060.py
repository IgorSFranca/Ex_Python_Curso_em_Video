n = int(input('Digite um número para calcular seu fatorial: '))
mult = 1
cont = n
print('Calculando {}!'.format(n), end=' = ')
while cont > 0:
    print(cont, end='')
    print(' x ' if cont > 1 else ' = ', end='')
    mult = cont * mult
    cont -= 1
print(mult)