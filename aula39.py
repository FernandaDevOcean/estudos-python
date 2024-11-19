"""
Iterando strings com while
"""
#.........012345678......
# nome = 'Fernanda Maria'
#........-987654321......

# nome = 'Fernanda Maria'
# nome_mod = f'{nome[0:]}*{nome[:14]}'
# contador = 0
# letra = len(nome)
# print(nome)
# print(nome_mod)
# print(letra)

nome = 'Fernanda Maria'
tamanho_nome = len(nome)
contador = 0
nome_mod = ''

while tamanho_nome > contador:
    letra = nome[contador]
    nome_mod += f'*{letra}'
    contador += 1

nome_mod += '*'
print(nome_mod)