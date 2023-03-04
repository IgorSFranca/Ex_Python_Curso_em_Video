n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
n3 = int(input('Terceiro Valor: '))
 
# Determinando o maior 
maior = n1
if n2 > n3 and n2 > n1: 
  maior = n2
if n3 > n2 and n3 > n1: 
  maior = n3

# Determinando o menor
menor = n1
if n2 < n1 and n2 < n3: 
  menor = n2
if n3 < n1 and n3 <n2: 
  menor = n3

print ('O menor número é o {}.'.format(menor))
print ('O maior número é o {}.'.format(maior))