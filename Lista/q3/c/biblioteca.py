from livro import Livro
from funcionario import Funcionario

class Biblioteca:
    # Criei as classes funcionario e livros e fiz com que a classe biblioteca tivesse atributos referentes a essas classes
    def __init__(self, nome: str, endereco: str, livros: list[Livro], funcionarios: list[Funcionario]):
        self.nome = nome
        self.endereco = endereco
        self.livros = []
        self.funcionarios = []