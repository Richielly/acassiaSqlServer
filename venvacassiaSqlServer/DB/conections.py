import pyodbc
import pandas as pd
import sqlalchemy as sa
from Arquivos import arquivos

dados_conexao= ("Driver={SQL Server};" "Server=PAT-1620\SQLEXPRESS;" "Database=Scf_CM_TerraRica;" )

conn = pyodbc.connect(dados_conexao)
cur = conn.cursor()