import requests 
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

def calcular_gastos(id):
    url_gastos = f"https://dadosabertos.camara.leg.br/api/v2/deputados/{id}/despesas?ordem=ASC&ordenarPor=ano"

    response_gastos = requests.get(url=url_gastos).json()

    gasto_total = 0.0
    for gasto in response_gastos['dados']:
        gasto_total += gasto['valorLiquido']

    return  locale.currency(gasto_total, grouping=True)



url = 'https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome'

response = requests.get(url=url).json()

for deputado in response['dados']:
    if deputado['siglaUf'] == 'SP':
        print('---------------------------')
        print(f"{deputado['nome']}({deputado['siglaPartido']}) {deputado['siglaUf']}",)
        print(f"Gastos Totais: {calcular_gastos(deputado['id'])}")
        




