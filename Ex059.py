from time import sleep

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
print('='*20)
opcao = 0
while opcao != 5:
    print('''O que deseja fazer?
[1] Somar os valores
[2] Multiplicar os valores
[3] Saber qual é o maior
[4] Informar novos números
[5] Sair do programa''')
    opcao = int(input('Qual a sua opção? '))
    if opcao == 1:
      soma = n1 + n2
      print('A soma entre {} e {} é igual a {}.'.format(n1, n2, soma))
      print('-'*15)
    elif opcao == 2:
      mult = n1 * n2
      print('A multiplicação entre {} e {} é igual a {}.'.format(n1, n2, mult))
      print('-'*15)
    elif opcao == 3: 
      if n1 > n2:
        print('Entre os números apresentados, o maior é {}.'.format(n1))
        print('-'*15)
      else:
        print('Entre os números apresentados, o maior é {}.'.format(n2))
        print('-'*15)
    elif opcao == 4: 
      print('Informe novamente os números')
      n1 = int(input('Informe o primeiro número: '))
      n2 = int(input('Infrome o segundo número: '))
      print('-'*15)
    elif opcao == 5:
      break
print('Finalizando...')
sleep (2)
print('='*20)
print('Fim da análise númerica')