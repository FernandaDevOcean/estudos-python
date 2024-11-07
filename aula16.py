# if / elif       / else
# se / se não se / se não
entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':  # condicionante independente
    print('Você entrou no sistema')
elif entrada == 'sair': # condicionante que depende do if
    print('Você saiu do sistema')
else:                   # sempre a última condicionante, podendo vir seguido de if
    print('Você não digitou nem entrar e nem sair.')