"""
10. Escreva uma função que retorna os máximos e mínimos de um dicionário.
"""

def maximo(dicionario):
    maximo = max(dicionario.values())
    return maximo

def minimo(dicionario):
    minimo = min(dicionario.values())
    return minimo

if __name__ == '__main__':
    dict = {'a': 11, 'b': 2, 'c': 23, 'd': 14, 'e': 35, 'f': 6, 'g': 57, 'h': 28, 'i': 19}
    print(dict)
    print(f'O maior valor do dicionário é {maximo(dict)}')
    print(f'O menor valor do dicionário é {minimo(dict)}')



