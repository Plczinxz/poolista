class ContaCorrente:
    def __init__(self, cliente: str, saldo: float):
        self.cliente = cliente
        self.saldo = saldo
    
    def depositar(self, valor: float) -> None:
        self.saldo += valor
    
    def saquePossivel(self, valor):
        if (self.saldo < valor):
            return False
        return True

    def sacar(self, valor: float) -> None:
        if (saquePossivel(self.saldo, valor)):
            self.saldo -= valor