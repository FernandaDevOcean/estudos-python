# if / elif       / else
# se / se não se / se não

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = False

# O interpretador segue a linha de achar o primeiro "True" e
# não executar as demais condiçoes, mesmo que sejam "True" também.

if condicao1:
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita.')

print('Fora do if')