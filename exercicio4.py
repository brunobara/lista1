"""
Exercício 4

Escreva um programa que ache e imprima os números divisíveis por 13 e por 19, entre o ano
de nascimento da sua mãe e 2727.

"""

for i in range(1957,2728):
    if (i % 13 == 0):
        print(i)
    elif (i % 19 == 0):
        print(i)
    else:
        pass
