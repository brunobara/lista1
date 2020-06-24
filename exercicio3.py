"""
Exercício 3

Escreva um programa que corre os números de 23 a 83 e imprime. Mas, quando for múltiplo
de três, imprima ‘Pum’, quando for múltiplo de 5 imprima ‘Bla’, quando for de ambos
imprima ‘PumBla’.

"""

for i in range(23,84):
    if (i % 15 == 0):
        print(f'{i} PumBla')
    elif (i % 3 == 0):
        print(f'{i} Pum')
    elif (i % 5 == 0):
        print(f'{i} Bla')
    else:
        print(i)
