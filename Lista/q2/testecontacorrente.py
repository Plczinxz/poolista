from contacorrente import ContaCorrente

novaConta = ContaCorrente("Paulo", 1000)

print(novaConta.saldo)
novaConta.sacar(500)

print(novaConta.cliente, novaConta.saldo)

novaConta.sacar(500)

print(novaConta.saldo)

novaConta.depositar(50)

print(novaConta.saldo)

novaConta.sacar(500)

print(novaConta.cliente, novaConta.saldo)