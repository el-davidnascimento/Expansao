import psycopg2
import pandas as pd


################# TRAKING ###############################

# Caminho do arquivo Excel
caminho_arquivo = r'C:\Users\Public\IBGE_Basico\Consolidado\consolidado.xlsx'

# Conexão com o banco de dados PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5433,
    database="Multiverso - Expansao",
    user="postgres",
    password="Multiverso@Educa"
)

# Ler os dados do arquivo Excel
dados_excel = pd.read_excel(caminho_arquivo)

# Cursor
cur = conn.cursor()

nome_tabela = 'IBGE_PESSOA13'

# Iterar sobre as linhas do DataFrame e inserir os valores na tabela do PostgreSQL
for _, linha in dados_excel.iterrows():
    valores = tuple(linha)
    cur.execute("INSERT INTO IBGE_PESSOA13 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", valores)

# Commit e fechamento da conexão
conn.commit()
cur.close()
conn.close()