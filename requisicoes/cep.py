import requests

cep = '17347456'

res = requests.get(url=f'https://viacep.com.br/ws/{cep}/json/')

if res:
    print(f'status: {res.status_code}\n')
    dados_cep = res.json()
    print('Dados do CEP:')

    for chave, valor in dados_cep.items():
        print(chave, ':', valor)
else:
    print('Erro na requisição!')