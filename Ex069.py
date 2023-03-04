sexo_m = sexo_f = maior_i = 0
while True:
    print('-------------------')
    print('CADASTRE UMA PESSOA')
    print('-------------------')
    idade = int(input('Idade: '))
    sexo = str(input('Informe o sexo [M/F]: ')).upper().strip()[0]
    while sexo not in 'MmFf':
      sexo = str(input('Sexo não identificado. Informe o sexo [M/F]: ')).upper().strip()[0]
    if idade >= 18:
       maior_i += 1
    if sexo == 'M':
       sexo_m += 1
    elif sexo == 'F' and idade < 20:
       sexo_f += 1
    continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continua == 'N':
      break
print(f'A) Total de pessoas com mais de 18 anos: {maior_i}')
print(f'B) Ao todo temos {sexo_m} homens cadastrados')
print(f'C) E temos {sexo_f} mulheres com menos de 20 anos.')