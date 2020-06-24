"""
Exercício 6

Escreva um programa que conte o número de letras de uma string e retorne e imprima o valor multiplicado por 10.
"""

def comando(palavra):
    contagem = len(palavra)
    print(contagem * 10)

if __name__ == '__main__':

    entrada = str(input('Digite uma palavra: '))
    comando(entrada)
