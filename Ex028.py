## Início da Biblioteca
import random

## Fim da Bibliteca
## Início do Código

print('*'*30)
print('Vamos ver se você consegue advinhar o número que o computador pensou!')
num = int(input('Informe um número entre 1 e 5: '))
comp = random.randint(1,5)
if num == comp:
  print('PARABÉNS! Você acertou o número.')
else:
  print('Pois é, infelimente você não acertou!')
  print('O número que o computador pensou foi o {}.'.format(comp))
print('*'*30)
## Fim do código