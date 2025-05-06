class FuncionarioHorista(Funcionario):
    def __init__(self, valorHora, horasTrabalhadas):
        super().__init__(nome)
        self.valorHora = valorHora
        self.horasTrabalhadas = horasTrabalhadas

    def calcularSalario(self):
        return self.valorHora * self.horasTrabalhadas