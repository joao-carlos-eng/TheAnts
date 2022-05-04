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
list_members = client.open("No Mercy - NoY (respostas)")

lis = [x.upper().split(',')[0] for x in open("folhas.txt", 'r', encoding='latin').readlines()]


def tratar(valor: str):
    return (re.sub('[^0-9a-zA-Z.,: `^~´s]', '', valor)) or 0


if __name__ == "__main__":
    list_tabela = get(f'Edificios')
    print(list_tabela)
    if type(list_tabela) is str:
        list_tabela = {}

    print(list_tabela.keys())

    for i in plan.worksheets():
        print(i.title)
        if i.title.upper() in lis and i.title.lower() not in list_tabela:
            ky = [str(re.sub('[*$#\[\]/.]', '', a)) for a in i.row_values(3)]
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

    # plan = list_members.worksheet('lista de membros')
    #
    # for x in range(2, 200):
    #     value = plan.cell(x, 1).value
    #     data = {
    #         "id_discord": "id_discord",
    #         "name": "None",
    #         "nickDiscord": "None",
    #         "apelido": "None",
    #         "cargo": "None",
    #         "alianca": "None",
    #         "tratamentos": "[]",
    #         "saudacoes": "[]",
    #         "insultos": "0",
    #         "elogios": "0"
    #     }
    #     if value:
    #         list_players = get(f'Players')
    #         print(list_players)
    #         if value.lower() not in list_players.keys():
    #             put(tabela=f'Players/{value.lower()}',
    #                 dados=str(data).replace('\'', '"'))
    #             time.sleep(3)
    #         print(value)
