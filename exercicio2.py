"""
Exercício 2

Altere o programa acima para que o usuário possa entrar com o número máximo de estrelas.

"""
def patern(size=5):
    for i in range(1,size):
        print('* ' * i)
    for i in reversed(range(1,(size-1))):
        print('* ' * i)
    return patern

if __name__ == '__main__':
    maximo = int(input('Por favor digite o número máximo de estrelas: '))
    patern(maximo)
