cont = soma = maior = menor = 0
resp = 'S'
while resp in 'Ss':
  n = int(input('Digite um número: '))
  resp = str(input('Quer Continuar? [S/N]: ')).strip().upper()[0]
  cont += 1
  soma += n
  if n == 1:
    maior = menor = n
  else:
    if n > maior:
      maior = n
    if n < menor:
      menor = n
media = (soma / cont)
print('Você digitou {} números e a média foi {:.2f}.'.format(cont, media))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior, menor))
