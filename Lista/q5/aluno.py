from turma import Turma

class Aluno:
    def __init__(self, nome: str, ira: float, turmas: list[Turma]):
        self.nome = nome
        self.ira = ira
        self.turmas = []
    