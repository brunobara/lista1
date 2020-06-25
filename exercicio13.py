"""
13. Escreva um programa que substitua ‘,’ por ‘.’ e ‘.’ por ‘,’ em uma string. Exemplo: 1,000.54
por 1.000,54.
"""

def substitui(str):
    substitui = str.translate({ord(','): '.', ord('.'): ','})
    return substitui

if __name__ == '__main__':

    entrada = str(input('Digite um número em formato "1,000.54": '))
    resultado = substitui(entrada)
    print(resultado)
