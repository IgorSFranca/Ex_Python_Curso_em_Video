def notas(*num, sit=False):
    notas = {}
    total_notas = len(num)
    maior = menor = soma = media = 0
    notas['total'] = total_notas
    for valor in range (0, len(num)):
        if valor == 0:
            maior = num[valor]
            menor = num[valor]
        else:
            if num[valor] > maior:
                maior = num[valor]
            elif num[valor] < menor:
                menor = num[valor]
        soma += num[valor]
    notas['maior'] = maior
    notas['menor'] = menor
    media = soma / total_notas
    notas['media'] = media
    if sit == True:
        if media < 3:
            notas['situação'] = 'RUIM'
        elif 3 <= media < 6:
            notas['situação'] = 'REGULAR'
        elif 6 <= media < 8:
            notas['situação'] = 'BOA'
        else:
            notas['situação'] = 'EXCELENTE'
    return notas

resp = notas(5.0, 8.5, 10, sit=True)
print(resp)