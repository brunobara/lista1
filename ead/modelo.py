import random
from cursos import Curso
from turmas import Turma
from alunos import Aluno

#Parametros
n_alunos = 50
n_turmas = 5

class Simulacao:
    def __init__(self):
        self.alunos = list()
        self.turmas = list()
        self.criar_aluno()
        self.criar_turmas()
        #self.inscrever_alunos = list()

    def criar_aluno(self):
        for i in range(n_alunos):
            self.alunos.append(Aluno(id))
    
    def criar_turmas(self):
        for i in range(n_turmas):
            self.turmas.append(Turma(id))

    def run_model(self):
        pass

if __name__ == '__main__':
    minha_sim = Simulacao()