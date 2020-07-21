from lista2.simulacao import Simulacao
from lista2.simulacao import gravar_arquivo

if __name__ == '__main__':
    num_vezes = 100
    media_total = 0
    for i in range(num_vezes):
        sim = Simulacao()
        media_total += sim.run_model()

    print(f'A média da experiência simulada {num_vezes} vezes é: {media_total/num_vezes}')
    gravar_arquivo('generalizacao', f'A média da experiência simulada {num_vezes} vezes é: {media_total/num_vezes}')