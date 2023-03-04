# Um programa que leia 6 números inteiros e mostre apenas a soma que forem pares. 
# Se o valor digitado for impar, desconsidere-o.

soma = 0
for c in range (0, 6):
  num = int(input('Informe o {} número: '.format(c+1)))
  if num % 2 == 0: 
    soma += num
print ('A soma dos valores pares informados é de {}.'. format(soma))