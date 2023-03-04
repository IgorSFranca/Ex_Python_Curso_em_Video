# Inicio da biblioteca
import random
# Fim da biblioteca

# Inicio do código
al_01 = str(input('Informe o 01 aluno: '))
al_02 = str(input('Informe o 02 aluno: '))
al_03 = str(input('Informe o 03 aluno: '))
al_04 = str(input('Informe o 04 aluno: '))
alunos = [al_01, al_02, al_03, al_04]
random.shuffle(alunos)
print('A ordem dos alunos será: ', alunos)
# Fim do código