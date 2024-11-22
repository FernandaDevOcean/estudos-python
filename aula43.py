# INTRODUÇÃO AO FOR/IN - estrutura de repetições para coisas finitas
# WHILE é mais usado para coisas infinitas ;)

# Supondo que temos uma senha salva num banco de dados

"""
senha_salva = '123456'
senha_digitada = ''
repeticoes = 0

while senha_salva != senha_digitada:
    senha_digitada = input(f'Sua senha ({repeticoes}x): ')

    repeticoes += 1

print(repeticoes)
print('Aquele laço acima pode ter repetições infinitas')
"""

texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')

"""
"Para cada letra (variável) que eu estou criando em texto (iterável) exiba a letra na tela"

A variável 'letra' é criada por nós mesmos, sendo ela um iterador, colocando cada
um dos elementos da string em ordem, dentro desse iterador. O Python sabe examente
quando o for começa e quando termina, isso porque não é variável como while
"""