import os

def ler_arquivos_consumo_combustivel(diretorio):
    # percorre todas as subpastas do diretório
    for root, dirs, files in os.walk(diretorio):
        # percorre todos os arquivos encontrados na subpasta atual
        for filename in files:
            if filename == "ConsumoCombustivel.txt":
                # constrói o caminho completo do arquivo
                filepath = os.path.join(root, filename)
                print(filepath)
                # abre o arquivo e lê seu conteúdo
                with open(filepath, "r") as f:
                    conteudo = f.read()
                    # faz o processamento necessário com o conteúdo do arquivo
                    print(conteudo)  # exemplo: imprime o conteúdo do arquivo

ler_arquivos_consumo_combustivel(r'C:\Users\Equiplano\Downloads\SimAm_CM_Terra_Rica')