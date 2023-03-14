nome_peso = []
dados = []
resp = ''
tot_pessoas = mais_pesadas = menos_pesadas = 0
while True: 
    while resp in 'S':
          #início das Perguntas
      dados.append(str(input('Nome: ')))
      dados.append(float(input('Peso: ')))
      resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()
          #Fim das perguntas
      tot_pessoas += 1
      nome_peso.append(dados[:])
      dados.clear()
      while resp not in 'SN':
         resp = str(input('Opção não identificada. Deseja Continuar? [S/N]: ')).strip().upper()
    if resp == 'N':
      break
print(f'Foram cadastradas {tot_pessoas} pessoas.')