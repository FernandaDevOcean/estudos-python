# Resolução do Exercício 1 [feita pelo prof]:

entrada = input('Digite um número: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_str = 'ímpar'

    if par_impar:
        par_impar_str = 'par'

    print(f'O número {entrada_int} é {par_impar_str}')
else:
    print('Você não digitou um número inteiro')