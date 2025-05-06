class Funcionario:
    def __init__(self, nome: str, cpf: str, valorPorHora: float, horasTrabalhadas: int = 0):
        self.nome = nome
        self.cpf = cpf
        self.valorPorHora = valorPorHora
        self.horasTrabalhadas = horasTrabalhadas
    
    def calcularSalario(self) -> float:
        return self.valorPorHora * self.horasTrabalhadas

    def incrementarHoras(self, horas: int) -> None:
        self.horasTrabalhadas += horas