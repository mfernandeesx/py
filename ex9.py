#desafio 01 

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de {valor} realizado com sucesso")
        else:
            print("Saldo insuficiente")

    def exibir_info(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: {self.saldo}")

if __name__ == "__main__":
    conta1 = ContaBancaria("João", 1000)
    conta1.depositar(0)
    conta1.sacar(200)
    conta1.exibir_info()

