lista = []
for valor in range (0, 5):
    n = int(input('Digite um valor: '))
    if valor == 0 or valor >= lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista.')
    else: 
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionao a posição {pos} da lista.')
                break
            pos += 1
print('*'*35)
print(f'Os valores digitados foram {lista}.')

#Não consegui fazer esse caralho. Tive que colar. 