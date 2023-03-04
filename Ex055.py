import math

soma_idade = 0
idade_maior = 0
nome_velho = 0
mulher_menor = 0

for c in range (0, 4):
    nome = str(input('Informe o nome: '))
    idade = int(input('Informe a idade: '))
    if idade >= 0:
        soma_idade += idade
    sexo = str(input('Informe o sexo: '))
    if sexo == 'M' or sexo == 'm':
        if idade_maior < idade:
            idade_maior = idade
            nome_velho = nome
    elif sexo == 'F' or sexo == 'f':
        if idade < 20:
            mulher_menor += 1
    print('-'*20)

media_idade = (soma_idade / 4)
print('A média de idade é de {} anos.'.format(media_idade))
print('O homem mais velho do grupo é o {}.'.format(nome_velho))
print('Existem {} mulheres com menos de 20 anos.'.format(mulher_menor))