num = []
for valor in range(0,5):
    num.append(int(input(f'Digite um valor para a posição {valor}: ')))
print('*'*35)
print(f'Você digitou os valores {num}')
print(f'O maior valor digitado foi {max(num)} na posição', end=' ')
for indice, valor in enumerate(num): 
    if valor == max(num): 
        print(indice)
print(f'O menor valor digitado por {min(num)} na posição', end=' ')
for indice, valor in enumerate(num):
    if valor == min(num):
        print(indice)