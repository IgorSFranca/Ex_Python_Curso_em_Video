print('---'*30)
print('---'*30)
frase = str(input('Digite a frase: '))
print('Quantos caracteres:', len(frase))
print('Quantas letras A tem na frase: ', frase.count('a'))
print('Em que posição inicia a palavra "França" no texto: ', frase.find('França'))
print('Existe a palavra "Gonçalves" na frase?: ', end='')
if 'Gonçalves' in frase == True:
    print('Sim')
else:
    print('Não')
print('Alterando o sobrenome "França" para "Gonçalves": ', frase.replace('França', 'Gonçalves'))
print('Deixando toda a frase em Maiúscula: ', frase.upper())
print('Deixando toda a frase em Minúscula: ', frase.lower())
print('Capitalizando toda a frase: ', frase.capitalize())
print('Deixando todas as letras inicias maíusculas: ',frase.title())
print('Tirando o espaço inútil do início e do fim: ', frase.strip())
frase_strip = frase.strip()
print('Depois do "Strip" a frase fica com {} caracteres.'.format(len(frase_strip)))
print('Tirando o espaço inútil da direita do texto: ', frase.rstrip())
print('Tirando o espaço inútil da esquerda do texto: ', frase.lstrip())
print('Dividindo a frase em Lista: ', frase.split())
# não funcionou# print('Juntando a frase que foi dividida em lista: ', ''.join(frase))
print('---'*30)
print('---'*30)