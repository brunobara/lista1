#import random
class Conta:

    def __init__(self, id):
        self.id = id
        self.saldo = 0
        #self.saldo = random.randint(0,5000)

    def deposito(self, quantia):
        self.saldo += quantia
        return quantia

    def retirada(self, quantia):
        self.saldo -= quantia
        return quantia


if __name__ == '__main__':
    bruno = Conta(16843592872)
    bruno.deposito(1000)
    bruno.retirada(150)
    print(f'O saldo da conta {bruno.id} é {bruno.saldo}')