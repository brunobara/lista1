"""
14. Escreva um programa que verifica se todas as letras do alfabeto constam no mínimo uma
vez do parágrafo fornecido pelo usuário.
"""

def letras_alfabeto(texto):
    sim = []
    for i in texto:
        if i in "abcdefghijklmnopqrstuvwxyz":
            if i in sim:
                pass
            else:
                sim.append(i)
        else:
            pass
    sim.sort()
    print(f'Em sua frase constam as letras: {sim}')
    return

if __name__ == '__main__':
    frase = str(input("Digite uma frase: "))
    letras_alfabeto(frase)
