# import shutil
# from datetime import datetime
# import time
# from zipfile import ZipFile 

import zipfile
import os

filename = '/workspaces/api-temp/dados/dados_United_States_20231226.zip'
extract_folder = '/workspaces/api-temp/teste_extract/'  # Onde você quer extrair o conteúdo

try:
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        # Obtém o nome do primeiro arquivo dentro do ZIP
        first_file = zip_ref.namelist()[0]
        
        # Extrai apenas esse arquivo para o diretório de extração
        zip_ref.extract(first_file, path=extract_folder)
        
        print('Arquivo descompactado!')
    
except zipfile.BadZipFile:
    print('Not a zip file or a corrupted zip file')











# filename = '/workspaces/api-temp/dados/dados_United_States_20231226.zip'

# try:
#     with zipfile.ZipFile(filename, 'r') as zip_ref:
#         zip_ref.extractall()
#         print('Arquivo descompactado!')
    
# except zipfile.BadZipFile:
#     print('Not a zip file or a corrupted zip file')

# import zipfile
# import os




# timestamp = datetime.now().strftime('%Y%m%d')

# filename = '/workspaces/api-temp/teste_extract/dados_United_States_20231226.zip'
# extract_dir = '/workspaces/api-temp/teste_extract/'
# archive_format = "zip"

# shutil.unpack_archive(filename, extract_dir)
# # shutil.unpack_archive("archive.zip", "destination")
# print("Arquivo descompactado com sucesso!")