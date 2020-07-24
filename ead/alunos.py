import random

class Aluno():
    def __init__(self, id):
        self.id = id
        self.idade = round(random.uniform(18, 60), 0)
        self.genero = random.choice(['feminino', 'masculino'])
        self.uf = random.randint(0, 26)
        self.escolaridade = random.choice(['basico', 'medio', 'superior', 'especializacao'])


if __name__ == '__main__':
    bruno = Aluno(1)
    leticia = Aluno(2)
    isabela = Aluno(3)
    gustavo = Aluno(4)
