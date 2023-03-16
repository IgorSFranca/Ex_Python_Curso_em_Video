alunos = []
medias = []
temp = []
resp = 'S'
while True:
    #
    # Recebimento de dados
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Nota 01: ')))
    temp.append(float(input('Nota 02: ')))
    alunos.append(temp[:])
    media = (temp[1]+temp[2])/2
    medias.append(media)
    temp.clear()
    #
    ## Pergunta de encerramento do programa
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while resp not in 'SN':
        resp = str(input('Opção não encontrada. Deseja Continuar? [S/N]: ')).strip().upper()
    if resp == 'N':
        break
#
# Análise dos dados
print('-'*18)
print('No. Nome     Média')
for indice in range (0, len(alunos)):
    print('{:<4}'.format(indice), end='')
    print('{:<9}'.format(alunos[indice][0]), end='')
    print('{:<5.2f}'.format(medias[indice]))
print('-'*18)
#
# Segunda parte, solicitação das informações registradas do aluno
while True:
  indice = int(input('Mostrar nota de qual aluno? [999 interrompe]: '))
  if indice != 999: 
      print(f'As notas de {alunos[indice][0]} são {alunos[indice][1]} e {alunos[indice][2]}')
  if indice == 999:
      break
print('-'*18)
print('{:^18}'.format('FINALIZADO'))
print('-'*18)