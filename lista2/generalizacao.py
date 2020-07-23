from simulacao import Simulacao
from simulacao import gravar_arquivo

def generalizacao(x):
    med_exp = []
    #med_custo = []
    #med_saldo_cliente = []
    #med_saldo_loja = []
    for i in range(x):
        minha_sim = Simulacao()
        print(minha_sim)


if __name__ == '__main__':

    num_vezes = 2
    generalizacao(num_vezes)
    #print(f'A média da experiência simulada {num_vezes} vezes é: {med_exp/num_vezes}')
