import psycopg2


# Conexão com o banco de dados PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5433,
    database="Multiverso - Expansão",
    user="postgres",
    password="Multiverso@Educa"
)

# Cursor
cur = conn.cursor()

################# Traking ###############################


# Se a tabela não existe, cria
cur.execute('''CREATE TABLE INEP (
               Considerar VARCHAR(100),
               Ativa_ou_Inativa VARCHAR(100),
               Privada_ou_Publica VARCHAR(5000),
               Escola VARCHAR(5000),
               MEC VARCHAR(1000),
               Bairro VARCHAR(500),
               Predio_Escola VARCHAR(500),
               Segmentos VARCHAR(10),
               Salas VARCHAR(100),
               Socios VARCHAR(150),
               CNPJ_Escola VARCHAR(1000),
               CNPJ_Matriz VARCHAR(1000),
               Alunos_Total VARCHAR(100),
               Alunos_EI VARCHAR(100),
               Alunos_EF1 VARCHAR(100),
               Alunos_EF2 VARCHAR(100),
               Alunos_EM VARCHAR(100),
               CAGR_10_22 VARCHAR(100),
               Alunos_2010 VARCHAR(500),
               Turma_EI VARCHAR(100),
               Turma_EF1 VARCHAR(100),
               Turma_EF2 VARCHAR(100),
               Turma_EM VARCHAR(100),
               Alunos_EI_Turma_EI VARCHAR(100),
               Alunos_EF1_Turma_EF1 VARCHAR(100),
               Alunos_EF2_Turma_EF2 VARCHAR(100),
               Alunos_EM_Turma_EM VARCHAR(100),
               Quantidade_docentes VARCHAR(100),
               Piscina_1_sim VARCHAR(100),
               Quadra_descoberta VARCHAR(100),
               Quadra_coberta VARCHAR(100),
               Telefone VARCHAR(150),
               Municipio VARCHAR(500),
               Endereço VARCHAR(1000),
               Numero VARCHAR(150),
               CEP VARCHAR(150),
               UF VARCHAR(100),
               Qtde_Total_2012 VARCHAR(100),
               Qtde_Total_2013 VARCHAR(100),
               Qtde_Total_2014 VARCHAR(100),
               Qtde_Total_2015 VARCHAR(100),
               Qtde_Total_2016 VARCHAR(100),
               Qtde_Total_2017 VARCHAR(100),
               Qtde_Total_2018 VARCHAR(100),
               Qtde_Total_2019 VARCHAR(100),
               Qtde_Total_2020 VARCHAR(100),
               Qtde_Total_2021 VARCHAR(100),
               Qtde_Total_2022 VARCHAR(100)
               );''')

# Commit e fechamento da conexão
conn.commit()
cur.close()
conn.close()