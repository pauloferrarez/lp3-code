class Calculadora:

    def calcular(self, op, num1, num2):
        if op == '+':
            resultado = self.__adicionar(num1, num2)
            print(resultado)
        elif op == '-':
            resultado = self.__subtrair(num1, num2)
            print(resultado)
        else:
            print('Operação inválida')
    
    def __adicionar(self, num1, num2):
        return num1 + num2

    def __subtrair(self, num1, num2):
        return num1 - num2

calc = Calculadora()
calc.calcular('+', 10, 20)
calc.calcular('-', 10, 20)