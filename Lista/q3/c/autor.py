from aluno import Pessoa
from livro import Livro

class Autor(Pessoa):
    def __init__(self, codigo: int, livros: Livro):
        super().__init__(nome, cpf)
        self.codigo = codigo
        self.livros: list[Livro] = []