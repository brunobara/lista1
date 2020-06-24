"""
Exercício 7

Escreva um programa que, dada uma lista de números [-2, 34, 5, 10, 5, 4, 32] qualquer,
retorne: o primeiro valor, o número de valores, o último valor, a soma, a média e a mediana.
*** Obs. Para listas com tamanho ímpar, a mediana é o valor do meio, quando ordenada
(sorted()). Para listas pares, retorne os dois valores do meio.
"""

def primeiro(lst):
    print(lst[0])

def quantidade(lst):
    print(len(lst))

def ultimo(lst):
    print(lst[-1])

def soma(lst):
    print(sum(lst))

def media(lst):
    result = sum(lst)/len(lst)
    print(result)

def mediana(lst):
    sorted(lst)
    if len(lst) % 2 != 0:
        print(lista[len(lista)-int(len(lista)/2)])
    else:
        print(f'{lista[int(len(lista)/2)]}, {lista[(int(len(lista)/2)-1)]}')

if __name__ == '__main__':
    lista = [-2, 34, 5, 10, 5, 4, 32]
    print(lista)
    primeiro(lista)
    quantidade(lista)
    ultimo(lista)
    soma(lista)
    media(lista)
    mediana(lista)
