num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 
       'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 
       'doze', 'treze', 'quatorze', 'quinze', 'desesseis', 
       'desessete', 'dezoito', 'dezenove', 'vinte')
escolha = int(input('Digite um número entre 0 e 20: '))
while True:
  if escolha <= 20:
    print(f'O número digitado por extenso é "{(num[escolha])}"')
    break
  else: 
    print(f'Número não identificado.')
    escolha = int(input('Digite um número entre 0 e 20: '))
print('Fim da execução')