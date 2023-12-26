import requests
import json
from datetime import datetime
import time
import pandas as pd
import os
import zipfile



name = 'USA'
link = f'https://restcountries.com/v3.1/name/{name}'

requisicao = requests.get(link)
requisicao_js = requisicao.json()

pais = requisicao_js[0]['name']['common']
capital = requisicao_js[0]['capital']
idioma = requisicao_js[0]['languages']
moeda = requisicao_js[0]['currencies']
populacao = requisicao_js[0]['population']
regiao = requisicao_js[0]['region']
timezones = requisicao_js[0]['timezones']
area = requisicao_js[0]['area']

timestamp = datetime.now().strftime('%Y%m%d')
upg_pais = pais.replace(" ", "_")
new_file = f'dados_{upg_pais}_{timestamp}.txt'
print(new_file)


timestamp = datetime.now().strftime('%Y%m%d')
path = '/workspaces/api-temp/dados/'

destino = path + new_file

try:
    with open(destino, 'w') as arq:
        print("INFO DO PAIS", file=arq)
        print("-------------", file=arq)
        print(f"Pais: {pais}", file=arq)
        print(f"Capital: {capital}", file=arq)
        print(f"Idioma: {idioma}", file=arq)
        print(f"Moeda: {moeda}", file=arq)
        print(f'População: {populacao}', file=arq)
        print(f'Região: {regiao}', file=arq)
        print(f'Time Zones: {timezones}', file=arq)
        print(f'Area: {area}', file=arq)
        print("            ", file=arq)
        print("------------", file=arq)
        print('Arquivo salvo!')
        
except FileNotFoundError as error:
    print(f'Erro: {error}')
    

time.sleep(5)
print('Iniciando processo para compactar!')

timestamp_original = timestamp
diretorio = '/workspaces/api-temp/dados/'
palavra_chave = 'United'  

ultimo_timestamp = None
caminho_arquivo = None

print('Iniciando a iteração dos dados!')

for root, dirs, files in os.walk(diretorio):
    for nome_arquivo in files:
        if palavra_chave in nome_arquivo:
            caminho_completo = os.path.join(root, nome_arquivo)
            timestamp = os.path.getmtime(caminho_completo)
            if ultimo_timestamp is None or timestamp > ultimo_timestamp:
                ultimo_timestamp = timestamp
                caminho_arquivo = caminho_completo

if caminho_arquivo:
    print(f'Arquivo encontrado: {caminho_arquivo}')

    nome_arquivo = os.path.basename(caminho_arquivo)  # Obtém somente o nome do arquivo, sem o caminho completo
    nome_sem_extensao = os.path.splitext(nome_arquivo)[0]  # Remove a extensão do nome do arquivo

    zip_file_name = f'/workspaces/api-temp/dados/{nome_sem_extensao}.zip'  # Nome do arquivo ZIP sem a extensão
    
    try:
        with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(caminho_arquivo, arcname=nome_arquivo)  # Usa o nome do arquivo original para arcname
        print('Arquivo zipado com sucesso!')
    except FileNotFoundError:
        print('Arquivo não encontrado!')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')


else:
    print(f'Nenhum arquivo correspondente à palavra-chave "{palavra_chave}" foi encontrado no diretório {diretorio}.')