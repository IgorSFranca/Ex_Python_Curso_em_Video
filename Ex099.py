from time import sleep
from random import randint

def maior(*num):
    print('='*30)
    print('Analisando os valores passados')
    pos = cont = maior = 0
    for valor in range (0, len(num)):
        print(num[pos], end=' ', flush=True)
        if num[pos] > maior:
            maior = num[pos]
        pos += 1
        cont += 1
        sleep(0.5)
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')    

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()