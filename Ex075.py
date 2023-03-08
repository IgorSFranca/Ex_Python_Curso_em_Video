num = (int(input('Digite o 1 número: ')),
       int(input('Digite o 2 número: ')),
       int(input('Digite o 3 número: ')),
       int(input('Digite o 4 número: ')))
print(num)
print(f'O número 9 apareceu {num.count(9)} vezes.')
print(f'O primeiro valor 3 foi digitado na posição {num.index(3)}.')
print(f'Os números pares foram:', end=' ')
for n in num: 
    if n % 2 == 0: 
      print(n, end=' ')