class Pessoa:
    def __init__(self, nome):
        self.nome = nome


class Empresa:
    def __init__(self, nome, funcionario):
        self.nome = nome
        self.funcionario = funcionario


p1 = Pessoa("Ana")
e1 = Empresa("TechCorp", p1)

"""
    O código apresentado na lista não define o atributo funcionario, o qual é requerido para a inicialização de um objeto da classe Empresa. Inicializando o funcionário, o problema é rápidamente resolvido.
"""