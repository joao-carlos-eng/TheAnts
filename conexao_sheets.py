import re
import time

import gspread
from google.oauth2 import service_account
from conexao_fire_base import *

scopes = ['https://spreadsheets.google.com/feeds',
          'https://www.googleapis.com/auth/drive']

credentials = service_account.Credentials.from_service_account_file('credentials.json')
scoped_credentials = credentials.with_scopes(scopes)
client = gspread.authorize(scoped_credentials)
plan = client.open("The Ants - Edificios")
acao_da_colonia = client.open("Ação da Colônia Calendário")

lis = [x.upper().split(',')[0] for x in open("folhas.txt", 'r', encoding='utf-8').readlines()]


def tratar(valor: str):
    if valor.isalnum():
        return re.sub('[^0-9.,:a-zA-Z]', '', valor) or 0
    else:
        return (re.sub('[^0-9.,:]', '', valor)) or 0


if __name__ == "__main__":
    list_tabela = get(f'Edificios')
    if type(list_tabela) is str:
        list_tabela = {}

    print(list_tabela.keys())

    for i in plan.worksheets():
        print(i.title)
        if i.title.upper() in lis and i.title.lower() not in list_tabela:
            ky = [str(re.sub('[^a-zA-Z ]', '', a)) for a in i.row_values(3)]
            dt_0 = {}

            for x in range(4, 31):
                vl = [str(tratar(a)) for a in i.row_values(x)]
                if len(vl) > 0:
                    print(ky[1:], '\n', vl[1:])
                    dt = dict(zip(ky[1:], vl[1:]))
                    time.sleep(1)
                    dt_0[f'NVL {vl[0]}'] = dt
                else:
                    break

            put(tabela=f'Edificios/{i.title.lower()}/', dados=str(dt_0).replace('\'', '"'))
        print('\n')
        time.sleep(1)
