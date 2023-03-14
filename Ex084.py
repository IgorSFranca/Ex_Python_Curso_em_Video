galera = []
dados = []
for pessoa in range (0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
for pessoa in galera:
    print(pessoa[0])