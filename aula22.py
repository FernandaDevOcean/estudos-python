# Operadores lógicos
# and (e), or (ou), not (não)
# and - Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira sera avaliada naquele valor.
# São considerados falsy (que você já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor.

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

# if True
# if entrada == 'E' or entrada == 'e' and senha_digitada == senha_permitida:
#    print('Entrar')

# Sempre que tiver or e and no mesmo código, a expressão pode ficar ambígua.
# Quanto mais condições tiver no if, mais complicado fica.
# Nesse caso, usar os parêntesis ajudará o Python a avaliar primeiro.

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')
# Massa! Aqui deu certo ;)

# AVALIAÇÃO DE CURTO CIRCUITO
print(True and False or 0 and 'abc' or True)

senha = input ('Senha: ') or 'Sem senha'
print(senha)