#alguns desses exercicios tive auxiliação do meu colega de classe yuri teixeira

from funcionario import Funcionario

novoFuncionario = Funcionario("Luís", "12345678910", 25.50)

novoFuncionario.incrementarHoras(8)
print(novoFuncionario.nome, novoFuncionario.horasTrabalhadas)

novoFuncionario.incrementarHoras(4)
print(novoFuncionario.nome, novoFuncionario.horasTrabalhadas)

print(novoFuncionario.calcularSalario())