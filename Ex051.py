# Um programa que leia o primeiro termo e a razão de uma PA
# No final mostre os 10 primeiros termos dessa progressão. 

prim = int(input('Informe o primeiro termo da PA: '))
raz = int(input('Informe a razão da PA: '))
soma = prim
for c in range (1, 10):
    soma += raz
    print(soma, end=' → ')