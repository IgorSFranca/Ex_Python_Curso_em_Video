## inicio da biblioteca
import random
## fim da biblioteca 

## inicio do codigo 
al_01 = input('Informe o nome do 1 aluno: ')
al_02 = input('Informe o nome do 2 aluno: ')
al_03 = input('Informe o nome do 3 aluno: ')
al_04 = input('Informe o nome do 4 aluno: ')
alunos = [al_01, al_02, al_03, al_04]
escolhido = random.choice(alunos)
print('O aluno escolhido foi o {}.'.format(escolhido))

## fim do codigo 