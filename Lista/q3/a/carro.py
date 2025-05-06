from motor import Motor

class Carro:
    # Criei a classe motor e fiz com que a classe carro tivesse um atributo motor da classe motor
    def __init__(self, marca: str, modelo: str, motor: Motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor