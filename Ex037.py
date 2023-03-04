num = int(input('Informe um número: '))
print('Informe qual a base de conversão')
opcao = int(input('''[ 1 ] binário 
[ 2 ] octal 
[ 3 ] hexadecimal
[   ] Sua opção: '''))
if opcao == 1:
  print('O número {} em Binário é {}.'.format(num, bin(num)[2:]))
elif opcao == 2: 
  print('O número {} em Octal é {}.'.format(num, oct(num)[2:]))
elif opcao == 3: 
  print('O número {} em Hexadecimal é {}.'.format(num, hex(num)[2:]))
else: 
  print('Opção não encontrada, tente novamente.')