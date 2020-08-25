import random
from turmas import Turma
from alunos import Aluno

#Parametros
n_alunos = 5000
n_turmas = 60
sazonalidade_1 = 5
sazonalidade_2 = 3
sazonalidade_3 = 7
ano = 2020

class Simulacao:
    def __init__(self):
        self.alunos = list()
        self.turmas = list()
        self.criar_aluno()
        self.criar_turmas()
        self.matricula()
        self.sazonalidade()
        self.antiguidade()
        self.run_model()

    def criar_aluno(self):
        for i in range(n_alunos):
            self.alunos.append(Aluno(id))
    
    def criar_turmas(self):
        for i in range(n_turmas):
            self.turmas.append(Turma(id))

    def matricula(self):
        for a in self.alunos:
            a.turma = random.choice(self.turmas)
            a.diasenturmado += random.randint(10, 50)

    def sazonalidade(self):
        for a in self.alunos:
            if a.turma.oferta == 'jan-fev':
                a.diasenturmado -= sazonalidade_1
                a.interesse -= sazonalidade_1
            elif a.turma.oferta == 'jul-ago':
                a.diasenturmado -= sazonalidade_2
                a.interesse -= sazonalidade_2
            elif a.turma.oferta == 'nov-dez':
                a.diasenturmado -= sazonalidade_3
                a.interesse -= sazonalidade_3
            else:
                pass

    def antiguidade(self):
        for a in self.alunos:
            a.interesse -= (ano-a.turma.curso.ano_lancamento)

    def run_model(self):
        for a in self.alunos:
            if a.turma.curso.carga_horaria < a.diasenturmado * a.tempodeestudodiario:
                a.situacao = 1
                if a.interesse >= 85:
                    a.resultado = 1
            else:
                pass

    def alunos_evadidos(self):
        evadidos = 0
        for a in self.alunos:
            if a.situacao == 0:
                evadidos += 1
        return evadidos

    def alunos_aprovados(self):
        aprovados = 0
        for a in self.alunos:
            if a.resultado == 1:
                aprovados +=1
        return aprovados

    def alunos_reprovados(self):
        reprovados = 0
        for a in self.alunos:
            if a.situacao != 0:
                if a.resultado == 0:
                    reprovados +=1
        return reprovados



if __name__ == '__main__':
    minha_sim = Simulacao()
    print(f'De alunos {n_alunos} matriculados em {n_turmas} turmas no ano de {ano}:\n'
          f'{minha_sim.alunos_aprovados()} foram aprovados.\n'
          f'{minha_sim.alunos_reprovados()} foram reprovados.\n'
          f'{minha_sim.alunos_evadidos()} não completaram o curso.\n')
    print(f'Taxa de aprovação = {minha_sim.alunos_aprovados()/n_alunos * 100}%\n'
          f'Taxa de evasão = {minha_sim.alunos_evadidos()/n_alunos * 100}%')