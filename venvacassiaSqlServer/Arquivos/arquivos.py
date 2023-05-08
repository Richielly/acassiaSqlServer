import os
import tabula
from functools import lru_cache
from Util import util

codEntidade = 410
def ler_arquivos_consumo_combustivel(diretorio):
    list_conteudo = []
    # percorre todas as subpastas do diretório
    for root, dirs, files in os.walk(diretorio):
        # percorre todos os arquivos encontrados na subpasta atual
        for filename in files:
            if filename == "ConsumoCombustivel.txt":
                # constrói o caminho completo do arquivo
                filepath = os.path.join(root, filename)
                # abre o arquivo e lê seu conteúdo
                with open(filepath, "r") as f:
                    conteudo = f.readline()
                    # faz o processamento necessário com o conteúdo do arquivo
                    list_conteudo.append(conteudo)  # inclui em uma lista o conteúdo do arquivo

    open("ConsumoCombustivel.txt", mode="w", encoding="ansi")

    for line in list_conteudo:
        data = line.split('|')
        print(
            f"""{codEntidade}|{data[1]}|{data[2]}|{data[5]}|{data[6]}|{data[3]}|{data[4]}|{data[7].replace('.', ',')}""")
        with open("ConsumoCombustivel.txt", mode="a", encoding="ansi") as arquivo:
            arquivo.writelines(
                f"""{codEntidade}|{data[1]}|{data[2]}|{data[5]}|{data[6]}|{data[3]}|{data[4]}|{data[7].replace('.', ',')}\n""")

    return list_conteudo


def ler_arquivos_Hodometro_horimetro(diretorio):
    list_conteudo = []
    # percorre todas as subpastas do diretório
    for root, dirs, files in os.walk(diretorio):
        # percorre todos os arquivos encontrados na subpasta atual
        for filename in files:
            if filename == "HodometroHorimetro.txt":
                # constrói o caminho completo do arquivo
                filepath = os.path.join(root, filename)
                # abre o arquivo e lê seu conteúdo
                with open(filepath, "r") as f:
                    conteudo = f.readline()
                    # faz o processamento necessário com o conteúdo do arquivo
                    list_conteudo.append(conteudo)  # inclui em uma lista o conteúdo do arquivo

    open("VeiculoControleSimAm.txt", mode="w", encoding="ansi")
    CdControle = util.gerar_sequencia_memoria()
    for line in list_conteudo:
        data = line.split('|')
        with open("VeiculoControleSimAm.txt", mode="a", encoding="ansi") as arquivo:
            arquivo.writelines(
                f"""{codEntidade}|{data[1]}|{next(CdControle)}|2|{util.ultimo_dia_mes(int(data[4]),int(data[3]))}|{data[8].replace('.', ',')}|{data[9]}|{data[2]}|2|{data[6].replace('.',',')}|{data[7].replace('.',',')}||\n""")

    return list_conteudo

def extrair_tabelas(arquivo_pdf, page):
    tabelas = tabula.read_pdf(arquivo_pdf, pages=page)
    return tabelas

def criar_arquivo_ansi(nome_arquivo, lista_dados):
    with open(nome_arquivo+'.txt', 'w', encoding='utf-8') as arquivo:
        for dado in lista_dados:
            arquivo.write(dado + '\n')

# resp = extrair_tabelas(r'C:\Users\Equiplano\PycharmProjects\acassiaSqlServer\layoutTCE_2023.pdf', 682)
# lista = ler_arquivos_consumo_combustivel(r'C:\Users\Equiplano\Downloads\SimAm_Samae_Castelo_Branco')
# lista_controle_simAm = ler_arquivos_Hodometro_horimetro(r'C:\Users\Equiplano\Downloads\SimAm_Samae_Castelo_Branco')