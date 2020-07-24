import random

class Curso():
    def __init__(self, id):
        self.id = id
        self.carga_horaria = round(random.choice([8, 16, 24, 36, 40]))
        self.area_tema = random.choice(['assistencia_social', 'bolsa_familia', 'cadastro_unico', 'crianca_feliz'])
        self.ano_lancamento = random.randint(2012, 2020)


if __name__ == '__main__':
    curso1 = Curso(1)
    curso2 = Curso(2)