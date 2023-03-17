# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) 
# em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de 
# contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se 
# aposentar.

from datetime import date

trabalhador = {}
trabalhador['Nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de Nascimento: '))
idade = ((date.today().year) - ano_nasc)
trabalhador['Idade'] = idade
trabalhador['CTPS'] = int(input('Num. da CTPS (0 não tem): '))
if trabalhador['CTPS'] != 0:
    trabalhador['Contratação'] = int(input('Ano de Contratação: '))
    trabalhador['Salário'] = float(input('Salário: '))
    idade_aposentadoria = (((trabalhador['Contratação']) + 35) - date.today().year) + idade 
    trabalhador['Aposentadoria'] = idade_aposentadoria
print('-'*25)
for k, v in trabalhador.items():
    print(f'   - {k} tem o valor {v}')