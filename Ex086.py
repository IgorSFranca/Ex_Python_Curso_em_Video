matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range (0, 3):
  for coluna in range (0, 3): 
    matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('-='*30)
print(matriz[0])
print(matriz[1])
print(matriz[2])