import datetime

from conexao_sheets import acao_da_colonia
from vars import *


def acao(dia_da_semana):
    for x in acao_da_colonia.worksheets(f'{dia_da_semana}'):
        print(x.title)
        rows = range(1, 27)
        for l in rows:
            print(f'{x.cell(l, 1).value}==>{x.cell(l, 2).value}')


if __name__ == "__main__":
    now = datetime.datetime.now()
    indice_da_semana = now.weekday()
    dia = DIAS[indice_da_semana]
    print(now.time())

    print(datetime.time() > now.time())
