glossario = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO',
            'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO',
            'PROGRAMADOR', 'FUTURO')
for palavra in glossario: 
  print(f'\n Na palavra {palavra} temos ', end=' ')
  for letra in palavra:
    if letra in 'AEIOU':
      print(letra, end=' ')
 