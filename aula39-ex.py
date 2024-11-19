"""
Iterando strings com while
"""
#.........012345678......
# nome = 'Fernanda Maria'
#........-987654321......
# ACUMULAÇÃO: cria-se variável vazia e acumula valores dentro.

nome = 'Fernanda Maria'
indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)