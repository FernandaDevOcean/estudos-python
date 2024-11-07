# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5 6 7
#  F e r n a n d a
# -8-7-6-5-4-3-2-1

# nome = 'Fernanda'
# print(nome[3])
# print(nome[-6])
# print('d' in nome)
# print('ver' in nome)
# print(10 * '-')
# print('vio' not in nome)
# print('tom' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar:')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
