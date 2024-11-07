"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool.
"""
string = 'Fernanda Maria'
print(string[3])

# Se fosse necessário trocar alguma string, não poderia
# ser feito:

string = 'Fernanda Maria'
string[3] = 'ABC'
print(string[3])

# Nesse caso, criaria uma nova variável.
# Vou pegar o trecho que eu quero (ln 20), que nesse caso é de 0 a 3 (:3),
# pq eu quero eliminar o restante.

string = 'Fernanda Maria'
outra_variavel = f'{string[:3]}'
print(outra_variavel)

# Gerando uma nova variável (ln 29) fora das chaves pq quero a str 'ABC', depois
# quero que dê continuidade a minha string montando uma nova abrindo chaves
# e contando a partir de onde deve inciar e até onde findará.
# Com isso, temos:

string = 'Fernanda Maria'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(string)
print(outra_variavel)

"""
str, int, float, bool são objetos, o que significa que
existem ações que podem ser executadas dentro deles.
No caso de str, há inúmeros métodos. Por exemplo, se eu precisasse
que o texto retornasse com a primeira letra maiúscula e as demais minúsculas,
poderia usar o método .capitalize().

Codando fica assim:
"""

string = 'fernanda Maria'
print(string.capitalize()) # esse método precisa () na frente pra ser executado
