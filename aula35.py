"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
# Se a condição for False, nada será executado.
# 'Enquanto' a condição for falsa, não haverá nada executado.

contador = 0

while contador < 10:
    contador = contador + 1
    print(contador)

print('Acabou')

# Nesse caso, o contador irá iniciar de 1 e irá incluir o 10. Mas caso
# eu queira incluir desde o 0 devo inverter a ordem. Veja:

contador = 0

while contador < 10:
    print(contador)
    contador = contador + 1

print('Acabou')

# Porém, para que o 10 não seja excluído, basta inserir o símbolo de <=.

contador = 0

while contador <= 10:
    print(contador)
    contador = contador + 1

print('Acabou')