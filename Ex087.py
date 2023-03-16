matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = coluna_3 = maior = 0
for linha in range (0, 3):
    for coluna in range (0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [linha {linha+1}, coluna {coluna+1}]: '))
        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna]
        if matriz[linha][2]: 
            coluna_3 += matriz[linha][2]
        if matriz[1][coluna] == 0:
            maior = matriz[1][coluna]
        else: 
            if matriz[1][coluna] > maior:
                maior = matriz[1][coluna]
print('-='*30)
print(matriz[0])
print(matriz[1])
print(matriz[2])
print('-='*30)
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {coluna_3}')
print(f'O maior valor da segunda linha é {maior}')