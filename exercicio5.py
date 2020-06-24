"""
Exercício 5

Escreva um programa que recebe uma letra e identifica se ela é consoante.
"""


def letra(l):
    if l in "aeiouAEIOU":
        print('A letra digitada é uma vogal.')
    elif l in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
        print('A letra digitada é uma consoante.')
    else:
        print('Você não digitou uma letra ou digitou uma letra com acento.')

if __name__ == '__main__':

    a = str(input('Digite uma letra: '))
    letra(a)