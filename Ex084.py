pessoas = []
temp = []
pesadas = leves = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if len(pessoas) == 0:
        pesadas = leves = temp[1]
    else:
        if temp[1] > pesadas:
            pesadas = temp[1]
        if temp[1] < leves:
            leves = temp[1]
    pessoas.append(temp[:])
    temp.clear()
    while resp not in 'SN':
        resp = str(input('Opção não encontrada. Deseja continuar? [S/N]: ')).strip().upper()
    if resp == 'N':
        break
print('-='*30)
print(f'Foram lançadas {len(pessoas)} pessoas no total')
for pessoa in pessoas:
    if pessoa[1] == pesadas:
        print(f'A pessoa mais pesada é {pessoa[0]} com {pessoa[1]} quilos')
    elif pessoa[1] == leves:
        print(f'A pessoa mais leve é a {pessoa[0]} com {pessoa[1]} quilos')