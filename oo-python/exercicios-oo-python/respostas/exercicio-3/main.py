from ingresso import Ingresso
from ingressoVIP import IngressoVIP

ingresso_normal = Ingresso(10)
ingresso_vip = IngressoVIP(10, 5)

print("Preço do ingresso normal: ", end='')
ingresso_normal.imprimir_valor()

print("Preço do ingresso VIP: ", end='')
ingresso_vip.imprimir_valor()
