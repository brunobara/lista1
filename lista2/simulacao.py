import random
from lojas import Loja
from clientes import Cliente

def gravar_arquivo(nome_arquivo, valor):
    with open(f'{nome_arquivo}.txt', 'w') as handler:
        handler.write(f'{valor}')
        return

class Simulacao:
    def __init__(self):
        self.lojas = list()
        self.clientes = list()
        self.criar_lojas()
        self.criar_clientes()
        self.deposito_inicial()
        self.run_model()
        self.media_experiencia()
        self.media_custo()
        self.media_contas_lojas()
        self.media_contas_clientes()

    def criar_lojas(self):
        for id in range(3):
            self.lojas.append(Loja(id))

    def criar_clientes(self):
        for id in range(10):
            self.clientes.append(Cliente(id))

    def deposito_inicial(self):
        for cliente in self.clientes:
            cliente.conta.deposito(random.randint(10, 20))
            #cliente.conta.deposito(30)

    def media_experiencia(self):
        experiencia_total = 0
        for cliente in self.clientes:
            experiencia_total += cliente.experiencia
        return experiencia_total / len(self.clientes)

    def media_custo(self):
        custo_total = 0
        for loja in self.lojas:
            custo_total += loja.custo
        return custo_total / len(self.lojas)

    def media_contas_clientes(self):
        saldo_contas_clientes_total = 0
        for clientes in self.clientes:
            saldo_contas_clientes_total += clientes.conta.saldo
        return saldo_contas_clientes_total / len(self.clientes)

    def media_contas_lojas(self):
        saldo_contas_lojas_total = 0
        for lojas in self.lojas:
           saldo_contas_lojas_total += lojas.conta.saldo
        return saldo_contas_lojas_total / len(self.lojas)

    def run_model(self):
        for cliente in self.clientes:
            loja = random.choice(self.lojas)
            if loja.capacidade > 1:
                loja.capacidade -= 1
                if loja.custo < cliente.conta.saldo:
                    cliente.conta.retirada(loja.custo)
                    loja.conta.deposito(loja.custo)
                    cliente.experiencia += loja.experiencia
            else:
                pass


if __name__ == '__main__':

    minha_sim = Simulacao()
    print(f'A média da experiência dos clientes é {minha_sim.media_experiencia()}\n'
          f'A média de custo é {round(minha_sim.media_custo(),2)}\n'
          f'A média do saldo de contas dos clientes é {round(minha_sim.media_contas_clientes(),2)}\n'
          f'A média do saldo de contas das lojas é {round(minha_sim.media_contas_lojas(), 2)}\n')

    gravar_arquivo('simulacao', f'A média da experiência dos clientes é {minha_sim.media_experiencia()}\n'
          f'A média de custo é {round(minha_sim.media_custo(),2)}\n'
          f'A média do saldo de contas dos clientes é {round(minha_sim.media_contas_clientes(),2)}\n'
          f'A média do saldo de contas das lojas é {round(minha_sim.media_contas_lojas(), 2)}\n')

