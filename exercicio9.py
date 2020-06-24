"""
9. Escreva uma função que faz um loop sobre as keys de um dicionário. Se as keys forem
vogais, eleve o valor ao quadrado. Caso contrário, set o valor para 0. Use if k in ‘aeiou’.
"""

def loopdicio(dicionario):
  for k in dicionario:
    if k in 'aeiou':
      dicionario[k] = dicionario[k] ** 2
    else:
      dicionario[k] = 0

if __name__ == '__main__':
    dicio = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9}
    loopdicio(dicio)
    print(dicio)
