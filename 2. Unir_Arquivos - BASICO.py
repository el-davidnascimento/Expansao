import os
import pandas as pd

pasta = r'C:\Users\Public\IBGE_Basico\BASICO'  # Substitua pelo caminho da pasta desejada
dados_concatenados = pd.DataFrame()
# Loop para percorrer os arquivos na pasta
for arquivo in os.listdir(pasta):
    caminho_arquivo = os.path.join(pasta, arquivo)
    if os.path.isfile(caminho_arquivo) and arquivo.endswith('.xlsx'):
        dados_planilha = pd.read_excel(caminho_arquivo)
        dados_concatenados = pd.concat([dados_concatenados, dados_planilha])

caminho_destino = r'C:\Users\Public\IBGE_Basico\BASICO\Consolidado\consolidado.xlsx'  # Substitua pelo caminho desejado
# Salvar os dados concatenados em uma única planilha no arquivo Excel no caminho especificado
dados_concatenados.to_excel(caminho_destino, sheet_name='Dados Consolidados', index=False)
