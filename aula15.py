# nome = input('Qual é o seu nome?' )
# print(f'O seu nome é{nome}')

# numero_1 = input('Digite um número: ')
# numero_2 = input('Digite outro número: ')

# print(f'A soma dos número é: {numero_1 + numero_2}')

# Acontece que se o usuário colocar uma variável do tipo str o sistema
# quebra. Com isso, acabamos pensando em converter já a variável pro tipo
# int, mas isso pode gerar transtornos futuros, pois não seria possível
# visualizar o que foi inserido pelo usuário.

# Exemplo:
# numero_1 = int(input('Digite um número: '))
# numero_2 = int(input('Digite outro número: '))
# print(f'A soma dos número é: {numero_1 + numero_2}')

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2) 
print(f'A soma dos número é: {int_numero_1 + int_numero_2}')