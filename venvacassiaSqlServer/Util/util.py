import calendar
from datetime import datetime
from functools import lru_cache
import itertools

def ultimo_dia_mes(ano, mes):
    # Obter o número de dias no mês e ano especificados
    dias_no_mes = calendar.monthrange(ano, mes)[1]

    # Criar um objeto datetime com o último dia do mês
    ultimo_dia = datetime(ano, mes, dias_no_mes)

    # Formatar a data como uma string no formato dd/mm/aaaa
    ultimo_dia_formatado = ultimo_dia.strftime('%d/%m/%Y')

    return ultimo_dia_formatado


@lru_cache(maxsize=None)
def ultimo_numero_cache(limpar_cache=False):
    if limpar_cache:
        with open("cache_numero_sequencial.txt", "w") as f:
            f.write("1")
            return 1
    try:
        with open("cache_numero_sequencial.txt", "r") as f:
            ultimo_numero = int(f.read())
            novo_numero = ultimo_numero + 1
    except FileNotFoundError:
        with open("cache_numero_sequencial.txt", "w") as f:
            f.write("1")
            return 1

    with open("cache_numero_sequencial.txt", "w") as f:
        f.write(str(novo_numero))
    return novo_numero

def gerar_sequencia_memoria():
    for numero in itertools.count(start=1, step=1):
        yield numero