from abc import ABC, abstractclassmethod

class Funcionario(ABC):
    def __init__(self, nome):
        self.nome = nome
    
    @abstractclassmethod
    def calcularSalario():
        pass