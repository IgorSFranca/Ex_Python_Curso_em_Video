## Início das bibliotecas 
import math

## Fim das bibliotecas 

## Início do código
print('Vamos calcular o valor da hipotenusa.')
cat_op = float(input('Informe o valor do cateto oposto: '))
cat_ad = float(input('Agora informe o valor do cateto adjacente: '))
hip = (cat_op**2 + cat_ad**2)**(1/2)
print('A hipotenusa dos catetos informados é {:.2f}.'.format(hip))

## Fim do código