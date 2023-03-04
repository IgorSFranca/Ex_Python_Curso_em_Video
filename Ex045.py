import random
from time import sleep

print ('Vamos jogar JOKENPÔ')
print ('Informe a sua opção')
itens = ('Pedra','Papel','Tesoura')
opcao = int(input('''[1] Pedra
[2] Papel
[3] Tesoura
[ ] Sua opção: '''))

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ')
sleep(0.5)

comp = random.randint (0, 2)
print ('O computador escolheu {}.'.format(itens[comp]))
if opcao == 1 and comp == 0 or opcao == 2 and comp == 1 or opcao == 3 and comp == 2:
  print ('Houve um empate!')
elif opcao == 1 and comp == 1 or opcao == 3 and comp == 0 or opcao == 2 and comp == 2: 
  print ('Você PERDEU!')
else:
  print ('Você GANHOU!')