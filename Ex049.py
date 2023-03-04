# Refaça o desafio 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando o laço for.

import math

num = int(input('Informe o número que deseja a tabuada: '))
mult = int(input('Informe até onde sua tabuada será apresentada: '))
for c in range (1, mult+1, 1):
    print('{} x {} = {}'.format(num, c, num*c))
