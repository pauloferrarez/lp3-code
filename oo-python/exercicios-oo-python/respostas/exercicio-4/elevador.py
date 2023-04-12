class Elevador:
    def __init__(self, andares_predio=0, andar_atual=0, capacidade_maxima=0, pessoas_dentro=0):
        self.__andares_predio = andares_predio
        self.__andar_atual = andar_atual
        self.__capacidade_maxima = capacidade_maxima
        self.__pessoas_dentro = pessoas_dentro

    def inicializar(self, andares_predio, capacidade_maxima):
        self.__init__(andares_predio, 0, capacidade_maxima, 0)

    def entrar(self):
        if (self.__pessoas_dentro < self.__capacidade_maxima):
            self.__pessoas_dentro += 1
        else:
            print("Capacidade maxima do elevador excedida")

    def sair(self):
        if (self.__pessoas_dentro > 0):
            self.__pessoas_dentro -= 1
        else:
            print("Não há ninguem no elevador")

    def subir(self):
        if (self.__andar_atual < self.__andares_predio):
            self.__andar_atual += 1
        else:
            print("O elevador já se encontra no último andar, não é possível subir")

    def descer(self):
        if (self.__andar_atual > 0):
            self.__andar_atual -= 1
        else:
            print("O elevador já se encontra no térreo, não é possível descer")

    @property
    def andares_predio(self):
        return self.__andares_predio

    @andares_predio.setter
    def andares_predio(self, andares_predio):
        self.__andares_predio = andares_predio

    @property
    def andar_atual(self):
        return self.__andar_atual

    @andar_atual.setter
    def andar_atual(self, andar_atual):
        self.__andar_atual = andar_atual

    @property
    def capacidade_maxima(self):
        return self.__capacidade_maxima

    @capacidade_maxima.setter
    def capacidade_maxima(self, capacidade_maxima):
        self.__capacidade_maxima = capacidade_maxima

    @property
    def pessoas_dentro(self):
        return self.__pessoas_dentro

    @pessoas_dentro.setter
    def pessoas_dentro(self, pessoas_dentro):
        self.__pessoas_dentro = pessoas_dentro