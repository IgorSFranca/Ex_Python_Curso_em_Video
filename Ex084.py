galera = []
dados = []
for pessoa in range (0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
for pessoa in galera:
    if pessoa[1] >= 18:
        print(f'{pessoa[0]} é maior de idade')
    else:
        print(f'{pessoa[0]} é menor de idade')