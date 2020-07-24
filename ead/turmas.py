import random
from cursos import Curso

class Turma():
    def __init__(self, id):
        self.id = id
        self.oferta = random.choice(['jan-fev', 'mar-abr', 'mai-jun', 'jul-ago', 'set-out', 'nov-dez'])
        self.curso = Curso(id)

if __name__ == '__main__':
    t1 = Turma(1)
    t2 = Turma(2)