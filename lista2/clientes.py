from conta import Conta

class Cliente:
    def __init__(self, id):
        self.id = id
        self.conta = Conta(0)
        self.experiencia = 0

    def __repr__(self):
        return self.id

if __name__ == '__main__':
    bruno = Cliente('Bruno')
    isabela = Cliente('Isabela')
    bruno.conta.deposito(1000)
    isabela.conta.deposito(1000)
    print(f'O saldo da conta de {bruno.id} é {bruno.conta.saldo}')
    print(f'O saldo da conta de {isabela.id} é {isabela.conta.saldo}')
