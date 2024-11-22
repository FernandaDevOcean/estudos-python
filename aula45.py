"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo
iter -> me entregue o seu iterador
"""
texto = iter('Fernanda') # __iter__()

print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
# Dessa forma será mostrado um erro.

# for letra in texto
texto = iter('Fernanda') # iterável
iterador = iter(texto) # Iterator

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break
"""
Pode ser tbm
    try:
        letra = next(iterador)
        print(letra)


No geral, é isso aqui que o for faz por "debaixo dos panos". ;)
"""