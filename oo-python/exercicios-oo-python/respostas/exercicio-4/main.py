from elevador import Elevador
from pprint import pprint

elevador = Elevador()
elevador.inicializar(7,8)

elevador.entrar()
pprint(vars(elevador))
print()

elevador.entrar()
pprint(vars(elevador))
print()

elevador.entrar()
pprint(vars(elevador))
print()

elevador.subir()
pprint(vars(elevador))
print()

elevador.subir()
pprint(vars(elevador))
print()

elevador.sair()
pprint(vars(elevador))
print()

elevador.entrar()
pprint(vars(elevador))
print()

elevador.entrar()
pprint(vars(elevador))