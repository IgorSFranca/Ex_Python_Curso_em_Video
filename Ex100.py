from random import randint
from time import sleep

def sorteador(*num):
    print('Sorteando 5 valores da lista: ', end='')
    for valor in numeros:
        print(valor, end=' ', flush=True)
        sleep(0.5)
    print('- PRONTO!')

def somapar(*num):
    par = 0
    for valor in numeros:
        if valor % 2 == 0:
            par += valor
    print(f'Somando os valores pares de {numeros}, temos {par}')

numeros = [randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)]
sorteador(numeros)
somapar(numeros)