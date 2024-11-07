"""
Fatiamento de strings
 012345678910111213
 Tá legal, né?
-1413121110987654321
Fatiamento [i:f:p] [::]
i = início
f = final
p = passo   >> de quantos em quantos carateres ele vai pular
: = pedido de fatiamento
Obs.: a função len retorna a quantidade
de caracteres da str (a partir de 1). Diferente de índice, len conta
de fato a quantidade.
"""
variavel = 'Tá legal, né?'
print(variavel[4:])
# Se eu quiser ver até o final, posso omitir como o exemplo acima,
# mas caso eu queira que seja mostrado até o penúltimo índice devo
# inserir o número do último carcatere. Assim
print(variavel[4:7])
print(len(variavel))
print(variavel[0:len(variavel)])
print(variavel[0:9:2])
# Se caso eu colocar o passo com número negativo, a ordem será invertida.
print(variavel[::-1])