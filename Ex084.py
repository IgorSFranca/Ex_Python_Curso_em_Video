nome_peso = []
mais_peso = []
menos_peso = []
dados = []
resp = ''
tot_pessoas = 0
while True: 
    while resp in 'S':
      dados.append(str(input('Nome: ')))
      dados.append(float(input('Peso: ')))
      resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()
      tot_pessoas += 1
      nome_peso.append(dados[:])
      dados.clear()
      while resp not in 'SN':
         resp = str(input('Opção não identificada. Deseja Continuar? [S/N]: ')).strip().upper()
    if resp == 'N':
      break
print(f'Foram cadastradas {tot_pessoas} pessoas.')