from animal import Animal

class Cachorro(Animal):

    def __init__(self, nome, cor, porte):
        super().__init__(nome, cor)
        self._porte = porte