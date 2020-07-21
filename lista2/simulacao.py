import random
from lista2.lojas import Loja
from lista2.clientes import Cliente

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

    def criar_lojas(self):
        for id in range(3):
            self.lojas.append(Loja(id))

    def criar_clientes(self):
        for id in range(10):
            self.clientes.append(Cliente(id))

    def deposito_inicial(self):
        for cliente in self.clientes:
            cliente.conta.deposito(random.randint(10, 20))

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

    def media_contas(self):
        saldo_contas_clientes_total = 0
        for clientes in self.clientes:
            saldo_contas_clientes_total += clientes.conta.saldo
        saldo_contas_lojas_total = 0
        for lojas in self.lojas:
           saldo_contas_lojas_total += lojas.conta.saldo
        return ((saldo_contas_clientes_total + saldo_contas_lojas_total) / len(self.clientes + self.lojas))

    def run_model(self):
        for cliente in self.clientes:
            loja_escolhida = random.choice(self.lojas)
            if cliente.conta.saldo >= 0:
                liberado = loja_escolhida.visita_clientes()
                if liberado == True:
                    loja_escolhida.conta.deposito(cliente.conta.retirada(loja_escolhida.custo))
                    cliente.experiencia += loja_escolhida.experiencia
                    return cliente.experiencia
                else:
                    return False
            else:
                return False
        return self.media_experiencia(), self.media_custo()


if __name__ == '__main__':
    minha_sim = Simulacao()
    media = minha_sim.run_model()
    media_experiencia = minha_sim.media_experiencia()
    media_custo = minha_sim.media_custo()
    media_contas = minha_sim.media_contas()
    gravar_arquivo('simulação', f'A média geral da simulação é {media}\n'
                   f'A média de experiência é {media_experiencia}\n'
                   f'A média de custo é {media_custo}\n'
                   f'A média de contas é {media_contas}')
