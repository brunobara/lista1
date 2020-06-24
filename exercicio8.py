"""
Dicionários. Dado o dicionário: d = {‘a’: 0}: faça programas que
8.1 acrescente um par (chave, valor) {‘b’: 1}, ao dicionário;
8.2 verifique se a key ‘c’ está presente?
8.3 Concatene um dicionário a um outro dicionário: e = {z : 23}. Use o método
‘update’!
"""

# Dado o dicionário: d = {‘a’: 0}
d = {'a': 0}
print(d)

# 8.1 acrescente um par (chave, valor) {‘b’: 1}, ao dicionário
d['b'] = 1
print(d)
#8.2 verifique se a key ‘c’ está presente?
d.get('c')
print(d.get('c'))

#8.3 Concatene um dicionário a um outro dicionário: e = {z : 23}. Use o método ‘update’
z1 = {'z': 23}
d.update(z1)
print(d)