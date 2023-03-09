expressao = str(input('Digite a expressão matemática: '))
pilha = []
for linha in expressao: 
    if linha == '(':
      pilha.append('(')
    elif linha == ')':
        if len(pilha) > 0:
           pilha.pop()
        else: 
           pilha.append(')')
           break
if len(pilha) == 0:
  print('Essa expressão está correta')
else: 
   print('Essa expressão está errada')