individuo = {}
pessoas = []
c_pessoas = s_idade = mulheres = 0

while True: 
    individuo.clear()
    individuo ['nome'] = str(input('Nome: '))
    individuo ['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    while individuo ['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        individuo ['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    individuo ['idade'] = int(input('Idade: '))
    s_idade += individuo['idade']
    pessoas.append(individuo.copy())
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
    c_pessoas += 1
    while resp not in 'SsNn':
        print('ERRO! Responda apenas S ou N.')
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if resp == 'N':
        break
media = s_idade/c_pessoas

print('-'*30)
print(f'A) Ao todo temos {c_pessoas} pessoas cadastradas.')
print(f'B) A média de idade é {media} anos')
print('C) As mulheres cadastradas foram', end='')
for pessoa in pessoas:
    if pessoa['sexo'] == 'F':
        print(f' {pessoa["nome"]}', end='')
print('D) A lista de pessoas que estão acima da média:')
for posicao in pessoas:
    if posicao['idade'] > media: 
        print(f'Nome = {posicao["nome"]}; Sexo = {posicao["sexo"]}; Idade = {posicao["idade"]}. ')

print('-'*30)
print('ENCERRADO')
