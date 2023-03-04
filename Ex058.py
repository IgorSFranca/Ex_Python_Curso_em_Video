from random import randint

print('*'*60)
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue advinhar qual foi?''')
comp = randint(0,11)
palp = 0
tent = 0
while palp != comp:
    palp = int(input('Qual é o seu palpite? '))
    tent += 1
    if palp < comp:
        print('Mais... Tente mais uma vez.')
    elif palp > comp: 
        print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(tent))
print('*'*60)