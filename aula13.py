nome = 'Fernanda Maria'
altura = 1.64
peso = 63
imc = peso / (altura * altura)


# Adicionar 'f' ("f-strings) é uma das formas de formatação de strings, o que habilita usar textos
# para usar variáveis, basta envolver em chaves {}; para formatar casas decimais adiciono
# .2f (exemplo de quantidade de casas decimais, mas pode ser de 1 a infinito)
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
