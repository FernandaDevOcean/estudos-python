a = 'A'
b = 'B'
c = 1.1

# Outra forma seria
# string = 'a={} b={} c={}'
# formato = string..format(a, b, c)

formato = 'a={} b={} c={:.2f}'.format(a, b, c)
# As variáveis dentro desses parêntesis são argumentos: valores.
# Caso eu queria ver casas decimais, adiciono ':.2f', exemplo.
# Se eu codar algo e aparecer o erro 'out of range', lembrar que estou buscando algo
# que já encerrou. Mas se eu precisar repetir um número, os códigos funcionam por
# índice, que sempre inicia de 0 e vai até o infinito. Portanto, para repetir
# basta que eu referencie as variáveis por seus indíces.
# Exemplo:
# formato = 'a={0} b={1} c={2:.2f}'.format(a, b, c)

# Apesar disso, indíces podem não ser confiáveis e eu posso querer nomear.
# Se chamando 'parâmetro nomeável', que é quando eu dou nome pras coisas dentro das funções.
# formato = string.format(nome1=a, b, c)  --> preciso nomear os seguintes
# formato = string.format(a, b, nome3=c)  --> não preciso nomear os demais.

print(formato)
