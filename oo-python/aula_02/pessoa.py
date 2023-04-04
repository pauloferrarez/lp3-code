class Pessoa:

    def __init__(self, nome: str, idade: int, cpf: str) -> None:
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf

    def __apresentar_documento(self) -> str:
        return self.__cpf

    def beber(self, bebida: str) -> None:
        if bebida == 'cerveja' and self.idade >= 18:
            print(self.__apresentar_documento())
        print('Bebendo', bebida)

    def correr(self) -> None:
        print('Correndo')

p = Pessoa(nome='João', idade=18, cpf='123456789')

print(p.nome)
print(p.idade)

p.beber(bebida='refrigerante')
p.beber(bebida='cerveja')
p.correr()