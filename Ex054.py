from datetime import date

maiores = 0
menores = 0
for c in range (0, 7):
    ano = int(input('Informe o ano de nascimento: '))
    if (date.today().year - ano) >= 18:
        maiores += 1
    else: 
        menores += 1
print('Temos {} pessoas maiores de idade.'.format(maiores))
print('Temos {} menores de idade.'.format(menores))