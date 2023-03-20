pessoas = {}
individuo = []

while True: 
    nome = str(input('Nome: '))
    individuo.append(nome)
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    individuo.append(sexo)
    while sexo not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        sexo = str(input('Sexo [M/F]: ')).strip().upper()
        individuo.append(sexo)
    idade = int(input('Idade: '))
    individuo.append(idade)
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
    while resp not in 'SsNn':
        print('ERRO! Responda apenas S ou N.')
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if resp == 'N':
        break

print('-'*30)
print(pessoas)