import requests
import datetime


#chave para acessar
api_key = '7d345b55e9fbcf6989728ab565b60c59'
cidade = 'Mairiporã'
# lat = ' -23.19.07'
# lon = '46.35.12'
# excl = ''
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br"

#requisição get, necessário para acessar o conteúdo
requisicao = requests.get(link)
requisicao_js = requisicao.json()

requisicao_js['clouds']['probabilidade_de_chuva'] = requisicao_js['clouds'].pop('all')

#parametrizando a chave da informação que iremos receber
descricao = requisicao_js['weather'][0]['description']
temperatura = requisicao_js['main']['temp'] - 273.15
data = requisicao_js['dt']
prob = requisicao_js['clouds']

#passando o timestamp, para parametrizar de uma forma mais clean
timestamp = data
data_legivel = datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

print(f"Cidade: {cidade}, descição: {descricao}, Temperatura: {temperatura}ºC, data e hora: {data_legivel}")

timestamp = datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y%m%d%H%M%S')
nome_arquivo = f'tempo_mairipora_{timestamp}.txt'
local = '/workspaces/api-temp/dados/'
destino = local + nome_arquivo

try:
    with open(destino, 'w') as arq:
        print("INFO DO TEMPO", file=arq)
        print("-------------", file=arq)
        print(f"Cidade: {cidade}", file=arq)
        print(f"descição: {descricao}", file=arq)
        print(f"Temperatura: {temperatura}ºC", file=arq)
        print(f"data e hora: {data_legivel}", file=arq)
        print(f'Chuva: {prob}', file=arq)
        print("------------", file=arq)
        print("            ", file=arq)
        for j in requisicao_js.items():
            print(f'Informações base: {j}', file=arq)
        print("------------", file=arq)
        # print(f"Informação base: {requisicao_js}\n", file=arq)
        # print(f"Cidade: {cidade}, descição: {descricao}, Temperatura: {temperatura}ºC, data e hora: {data_legivel}",file=arq)
        print('Arquivo salvo!')
        
except FileNotFoundError as error:
    print(f'Erro: {error}')