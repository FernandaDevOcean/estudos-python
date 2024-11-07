# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
conta_1 = 1 + 1 ** 5 + 5   # 7
print(conta_1)


# Observar a precedência:
# Os primeiros cálculos a serem executados serão os de dentro de parêntesis (n + n)
# [sendo que parêntesis internos são executados primeiros];
# seguido da potenciação/exponenciação (**); multiplicação (*), divisão (/),
# divisão inteira (//), módulo (%); e por fim a soma (+) e subtração (-).
# Se houver operadores de mesma procedência no código, serão executados
# de dentro pra fora, da esquerda para a direita, de cima pra baixo.

conta_2 = (1 + 1) ** (5 + 5)  # 1024
print(conta_2)

conta_3 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_3)
