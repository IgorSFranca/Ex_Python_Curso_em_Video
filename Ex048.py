print('''Cálculo da soma entre todos os números ímpares, que são múltiplos de 3,  
que estão no intervalo entre 1 até 500''')
soma = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        soma += c
print(soma)
