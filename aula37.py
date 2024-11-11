"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
# Se a condição for False, nada será executado.
# 'Enquanto' a condição for falsa, não haverá nada executado.

contador = 0

while contador <= 10:
    contador += 1
    print(contador)

print('Acabou')

# Caso eu queira que o laço seja terminado em 4, por exemplo,
# deve ser inserido if e break abaixo do print(). Veja:

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6')
        continue

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 40:
        break
    
print('Acabou')