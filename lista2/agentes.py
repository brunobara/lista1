from lista2.conta import Conta

class Agente:
    def __init__(self, id):
        self.id = id
        self.conta = Conta(0)
        self.experiencia = 0

if __name__ == '__main__':
    bruno = Agente(0)
    isabela = Agente(1)
    bruno.conta.deposito(1000)
    isabela.conta.deposito(1000)
    print(f'O saldo da conta de {bruno.id} é {bruno.conta.saldo}')
    print(f'O saldo da conta de {isabela.id} é {isabela.conta.saldo}')