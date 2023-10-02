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
cur.execute('''CREATE TABLE IBGE_DOMICILIO_RENDA (
               Cod_setor VARCHAR(1000),
               Situacao_setor VARCHAR(100),
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
               V012 VARCHAR(100),
               V013 VARCHAR(100),
               V014 VARCHAR(100)
               );''')

# Commit e fechamento da conexão
conn.commit()
cur.close()
conn.close()