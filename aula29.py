"""
Introdução ao try/except
try -> tentar executar o código
except -> aconteceu algum erro ao executar

print(123)
print(456)
int('a')
>>> Aqui o carcatere do tipo str não pode ser lido como int ou float,
por isso mostrará uma exceção (erro).

Supondo que eu peça um número ao usuário

numero = input('Vou dobrar o número que você digitar: ')
print(f'O dobro de {numero} é {numero * 2}')
# aqui a conta não sairá como quero

>>> Mas se eu quiser que retorne certinho, segue:
numero_str = input('Vou dobrar o número que você digitar: ') # sempre uma str
numero_float = float(numero)
print(f'O dobro de {numero} é {numero_float * 2}')
>>> Se eu precisar de casas decimais: {numero_float * 2:.2f}
"""

numero_str = input('Vou dobrar o número que você digitar: ') # sempre uma str

# if numero_str.isdigit(): .isdigit verifica se são números
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

# failfast
