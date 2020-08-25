import random

class Aluno():
    def __init__(self, id):
        self.id = id
        self.idade = random.randint(18, 65)
        #self.idade = 50
        self.genero = random.choice(['feminino', 'masculino'])
        self.uf = random.randint(0, 26)
        self.escolaridade = random.choice(['basico', 'medio', 'superior', 'especializacao'])
        self.tempodeestudodiario = round(random.randint (0, 6)/2, 2)
        self.diasenturmado = 0
        self.interesse = 100
        self.situacao = 0
        self.resultado = 0
        self.sociodemografico()
        self.turma()

    def sociodemografico(self):
        if self.uf >= 13:
            self.interesse -= 10
        else:
            self.interesse += 10
        if self.escolaridade == 'especializacao':
            self.interesse -= 3
        elif self.escolaridade == 'medio':
            self.interesse += 3
        if self.idade >= 50:
            self.interesse -= 5
        if self.genero == 'feminino':
            self.interesse += 10


    def turma(self):
        self.turma = random.randint(0, 2)


if __name__ == '__main__':
    bruno = Aluno(1)
    leticia = Aluno(2)
    isabela = Aluno(3)
    gustavo = Aluno(4)
