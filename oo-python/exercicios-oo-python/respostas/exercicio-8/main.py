from cartaomensagem import CartaoMensagem
from mensagemaniversario import MensagemAniversario
from mensagemdiadosnamorados import MensagemDiaDosNamorados
from mensagemnatal import MensagemNatal

msgs = []
msg1 = MensagemAniversario("Pai")
msgs.append(msg1)
msgs.append(MensagemAniversario("Mãe"))
msgs.append(MensagemDiaDosNamorados("Ana"))
msgs.append(MensagemNatal("Ana"))

for msg in msgs:
    print(msg.retornar_mensagem("Diego"))