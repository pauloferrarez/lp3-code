from contabancaria import ContaBancaria

class ContaImposto(ContaBancaria):
    def __init__(self, numero, agencia, saldo, codigo_tipo, percentual_imposto):
        ContaBancaria.__init__(self, numero, agencia, saldo, codigo_tipo)
        self.__percentual_imposto = percentual_imposto

    def calcular_imposto(self):
        return self.saldo - (self.saldo * self.__percentual_imposto)