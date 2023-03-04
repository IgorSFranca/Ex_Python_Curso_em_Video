sexo = str(input('Informe o seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'FfMm':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo [M/F]: ')).upper().strip()[0]
print('Sexo {} gravado com sucesso.'.format(sexo))