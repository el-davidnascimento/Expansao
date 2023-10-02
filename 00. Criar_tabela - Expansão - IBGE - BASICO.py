import psycopg2


# Conexão com o banco de dados PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5433,
    database="Multiverso - Expansao",
    user="postgres",
    password="Multiverso@Educa"
)

# Cursor
cur = conn.cursor()

################# Traking ###############################


# Se a tabela não existe, cria
cur.execute('''CREATE TABLE IBGE_BASICO (
               Cod_setor VARCHAR(1000),
               Cod_Grandes_Regioes VARCHAR(100),
               Nome_Grande_Regiao VARCHAR(1000),
               Cod_UF VARCHAR(100),
               Nome_da_UF  VARCHAR(1000),
               Cod_meso VARCHAR(100),
               Nome_da_meso VARCHAR(2000),
               Cod_micro VARCHAR(100),
               Nome_da_micro VARCHAR(1000),
               Cod_RM VARCHAR(100),
               Nome_da_RM VARCHAR(2000),
               Cod_municipio VARCHAR(1000),
               Nome_do_municipio VARCHAR(2000),
               Cod_distrito VARCHAR(200),
               Nome_do_distrito VARCHAR(2000),
               Cod_subdistrito VARCHAR(200),
               Nome_do_subdistrito VARCHAR(2000),
               Cod_bairro VARCHAR(2000),
               Nome_do_bairro VARCHAR(2000),
               Situacao_setor VARCHAR(100),
               Tipo_setor VARCHAR(100),
               V001 VARCHAR(100),
               V002 VARCHAR(100),
               V003 VARCHAR(100),
               V004 VARCHAR(100),
               V005 VARCHAR(100),
               V006 VARCHAR(100),
               V007 VARCHAR(100),
               V008 VARCHAR(100),
               V009 VARCHAR(100),
               V010 VARCHAR(100),
               V011 VARCHAR(100),
               V012 VARCHAR(100)
               );''')

# Commit e fechamento da conexão
conn.commit()
cur.close()
conn.close()