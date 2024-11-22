"""" while/else """
# recurso peculiar no Python #
""""
*É comum usar i como variável de índice.

Como é possível ou para que serve um else dentro de um while?

Suponhamos que estamos procurando algo dentro de uma string,
pode ser um espaço, por exemplo. Se caso houver, o laço será executado
e o else não, somente o que estiver fora dele.
Mas se caso não houver, o código será executado até o else, pois
procurou o espaço, não achou e assim printou o else pela condição
de não ter achado o que procurava.

Exemplo:
string = 'Valorqualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break
        
    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
print('Fora do while')
"""

string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]
    
    print(letra)
    i += 1
else:
    print('O else foi executado.')
print('Fora do while.')