from aluno import Aluno

class Turma:
    def __init__(self, materia: str, professor: str, alunos: list[Aluno]):
        self.materia = materia
        self.professor = professor
        self.alunos = []
    