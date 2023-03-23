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

maior(randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior(randint(1, 10), randint(1, 10), randint(1, 10))
maior(randint(1, 10), randint(1, 10))
maior(randint(1, 10))
maior()