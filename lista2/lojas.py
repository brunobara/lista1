import random
from lista2.conta import Conta

class Loja:
    def __init__(self, id):
        self.id = id
        self.conta = Conta(0)
        self.capacidade = random.randint(10, 250)
        self.experiencia = random.randint(0, 10)
        self.custo = round(random.random() * 15, 2)

    def visita_clientes(self):
        if self.capacidade >= 0:
            self.capacidade -= 1
            return True
        else:
            return False

    def experiencia(self):
        if self.capacidade <= 5:
            self.experiencia -= 10
            return self.experiencia
        elif self.capacidade < 100:
            return self.experiencia
        else:
            self.experiencia += 10
            return self.experiencia
        return self.experiencia

    def __repr__(self):
        return self.id

if __name__ == '__main__':
    cafeteria = Loja('Cafeteria')
    pizzaria = Loja('Pizzaria')
    mercado = Loja('Mercado')

    # Transações
    mercado.conta.deposito(1000)
    cafeteria.conta.deposito(mercado.conta.retirada(500))
    print(f'O saldo da conta de {cafeteria.id} é {cafeteria.conta.saldo}')
    print(f'O saldo da conta de {pizzaria.id} é {pizzaria.conta.saldo}')
    print(f'O saldo da conta de {mercado.id} é {mercado.conta.saldo}')

    # Capacidade
    print(f'A capacidade da {cafeteria.id} é de {cafeteria.capacidade} pessoas')