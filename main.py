import pyodbc
import pandas as pd
import sqlalchemy as sa
from Arquivos import arquivos

dados_conexao= ("Driver={SQL Server};" "Server=PAT-1620\SQLEXPRESS;" "Database=Scf_CM_TerraRica;" )

conn = pyodbc.connect(dados_conexao)
cur = conn.cursor()
resp = cur.execute('SELECT table_name FROM information_schema.tables;')

selects = []

for tables in resp.fetchall():
    try:
        count = cur.execute(f'SELECT count(*) from {tables[0]};')
        count = count.fetchone()[0]
        print(f'{tables[0]} : {count}')
        if count > 0:
           selects.append(f'SELECT * from {tables[0]};')


    except:print(tables[0], 'tabela com erro.')

# print(len(selects), 'Tabelas com dados')
# for select in selects:
#     print(select)

dataSet = pd.read_sql('SELECT * from PORTEEMPRESA', conn)

dataset_2 = pd.read_sql('SELECT upper(c.COR_PREDOMINANTE) from VEICULO_COR as c', conn)
dataset_3 = pd.read_sql(""" SELECT 
md.DsModelo,
mr.DsMarca,
e.DsTpVeiculo, 
''
from VEICULO v
join MODELOVEICULO md on (md.CdModelo = v.cdmodelo)
join MarcaVeiculo mr on (mr.CdMarca = md.CdMarca)
join TIPOVEICULO e on (e.CdTpVeiculo = v.CdTpVeiculo) """, conn)

dataset_4 = pd.read_sql(""" SELECT
499 as codEntidade,
a.NrSequencia as NrAbastecimento,
a.CdVeiculo as NrFrota,
v.IdVeiculoTCEPR as codBem,
a.CdItemMaterial as CodProduto,
p.DsMaterial as nomeProduto,
'NrCodigoMotorista' as NrCodigoMotorista,
ROUND((a.VlValor / a.QtMovimentada), 4) as vlUnitario,
concat(FORMAT(a.DtEvento, 'dd/MM/yyyy '), REPLACE(STR(a.HrEvento / 100, 2) + ':' + STR(a.HrEvento % 100, 2), ' ', '0')) as DtAbastecimento,
a.QtMovimentada as NrLitrosAbastecimento,
a.VlValor as VlAbastecimento,
1 as TpAbastecimento,
a.nrnfdepartamento as NrNotaFiscal,
a.dshistorico as DsObservacao,
a.cdFornecedorMotorista as CodFornecedor,
RIGHT(REPLICATE('0', 14) + f.cnpj, 14) as Cnpj,
'' as CodPessoa,
l.nomelocal,
'' as NrInterno,
'1' as IsAcumuladorFuncionando, --1=Sim 2=Não
'' as CodEntidadeLiquidacao,
'' as ExercicioLiquidacao,
'' as NrLiquidacao,
'' as ExLiquidacao,
'' as CodEntidadeOrigemLiquidacao,
'' as CodEntidadeEmpenho,
'' as ExercicioEmpenho,
'' as NrEmpenho,
'' as ExEmpenho,
'' as CodEntidadeOrigemEmpenho
from MOVTOVEICULO a
join MATERIAL p on (p.CdMaterial = a.CdItemMaterial)
join VEICULO v on (v.CdVeiculo = a.CdVeiculo)
left join SCF_Fornecedor f on (f.cdfornecedor = a.cdFornecedorMotorista)
left join SCF_Local l on (l.veiculo = a.CdVeiculo)
where a.NrSequencia > 0
order by a.NrSequencia """, conn)

dataset_4["concatenado"] = dataset_4.apply(lambda row: "|".join([str(val) for val in row.values]), axis=1)

arquivos.criar_arquivo_ansi('Abastecimento', dataset_4["concatenado"])


