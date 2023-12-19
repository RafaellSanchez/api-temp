import requests
import json

paises = ["USA", "Brazil"]
dados_paises = {}

for pais in paises:
    link = f'https://restcountries.com/v3.1/name/{pais}'
    requisicao = requests.get(link)
    
    if requisicao.status_code == 200:
        requisicao_js = requisicao.json()
        if isinstance(requisicao_js, list) and len(requisicao_js) > 0:
            dados_paises[pais] = requisicao_js
            print(f"Dados de {pais} obtidos com sucesso.")
        else:
            print(f"Dados não encontrados para {pais}")
    else:
        print(f"Erro ao buscar dados para {pais}. Código de status: {requisicao.status_code}")

local = '/workspaces/api-temp/dados/'
nome = 'dados_paises.txt'

nome_arquivo = local + nome
for pais, dados in dados_paises.items():
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dados_paises, arquivo, indent=4)
        print(f"{pais}:")
        print(dados)