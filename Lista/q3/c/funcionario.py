from aluno import Pessoa

class Funcionario(Pessoa):
    def __init__(self, codigo: int, cargo: str):
        super().__init__(nome, cpf)
        self.codigo = codigo
        self.cargo = cargo
    