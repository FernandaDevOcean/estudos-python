"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero_str = input('Digite um número inteiro: ')

try:
  numero_par = int(numero_str) % 2 == 0
  if numero_par:
    print('Seu número é par ;) ')
  else:
    print('Seu número é ímpar :( ')
except:
  print('Você não digitou um número')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario_str = input('Que horas são? ')

try:
    horario = int(horario_str)
    if horario >= 0 and horario <= 11:
       print('Bom dia ^^')
    elif horario >= 12 and horario <= 17:
      print('Boa tarde ;)')
    elif horario >= 18 and horario <= 23:
      print('Boa noite *-*')
except:
   print('Não é um número inteiro')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 letras escreva "Seu nome é muito grande".
"""

nome_str = input(str('Qual é o seu nome? '))
n_letras = (len(nome_str))

if not nome_str.isdigit() and n_letras > 0:
  if n_letras >=1 and n_letras <= 4:
    print('Seu nome é curto  *-* ')
  elif n_letras >= 5 and n_letras <= 6:
    print('Seu nome é normal ^^')
  elif n_letras >= 7:
    print('Seu nome é muito grande :O ')
elif nome_str.isdigit():
  print('Você é um robô? Pq vc digitou um número :/')
else:
  print(f'Você não disse seu nome :(, tudo bem.'
        ' Podemos recomeçar >.<"')
