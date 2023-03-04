## Início das bibliotecas
import math

## Fim das Bibliotecas 

## Início do Código
nome = str(input('Informe o seu nome: '))
nome = nome.strip()
print('Seu nome todo em maiúsculo é: ', nome.upper())
print('Seu nome todo em minúsculo é: ', nome.lower())
nome = nome.split()
QTD = len(nome [0])+len(nome [1])+len(nome [2])+len(nome [3])
print('Seu nome possui {} letras ao todo sem espaços.'.format(QTD))
print('Seu primeiro nome possui {} letras.'.format(len(nome [0])))

## Fim do código