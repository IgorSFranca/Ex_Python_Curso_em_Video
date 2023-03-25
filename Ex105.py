def notas(*num, sit=False):
    notas = {}
    total_notas = len(num)
    maior = menor = media = 0
    notas['total'] = total_notas
    for valor in range (0, len(num)-1):
        if valor == 0:
            maior = num[valor]
            menor = num[valor]
        else:
            if num[valor] > maior:
                maior = num[valor]
            elif num[valor] < menor:
                menor = num[valor]
    return notas

resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)