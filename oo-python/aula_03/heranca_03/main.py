from funcionario import Funcionario
from gerente import Gerente

f = Funcionario('Joao', '111111', 2000)
print('Funcionario:', f.calcular_bonificacao())

g = Gerente('Jose', '1122222', 5000)
print('Funcionario:', g.calcular_bonificacao())