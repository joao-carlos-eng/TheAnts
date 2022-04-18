import gspread
from google.oauth2 import service_account
from conexao_fire_base import *

scopes = ['https://spreadsheets.google.com/feeds',
          'https://www.googleapis.com/auth/drive']

credentials = service_account.Credentials.from_service_account_file('credentials.json')
scoped_credentials = credentials.with_scopes(scopes)
client = gspread.authorize(scoped_credentials)
plan = client.open("The Ants - Edificios")

lis = [x.upper().split(',')[0] for x in open("folhas.txt", 'r', encoding='utf-8').readlines()]

if __name__ == "__main__":
    for i in plan.worksheets():
        print(i.title.upper())
        if i.title.upper() in lis:
            ky = [str(a) for a in i.row_values(3)]
            print(ky)
            for x in range(4, 31):
                print(i.row_values(x))
                vl = [str(a) for a in i.row_values(x)]
                dt = dict(zip(ky, vl))
                post(tabela=f'Edificios/{i.title.lower()}', dados=json.dumps(dt))
            break
