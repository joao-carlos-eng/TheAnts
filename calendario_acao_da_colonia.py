import datetime

from conexao_sheets import acao_da_colonia

DIAS = [
    'Dia 1: Segunda-feira',
    'Dia 2: Terça-feira',
    'Dia 3: Quarta-feira',
    'Dia 4: Quinta-Feira',
    'Dia 5: Sexta-feira',
    'Dia 6: Sábado',
    'Dia 7: Domingo'
]

HORAS = [
            '21:05 ~ 21:59':,
            '22:05 ~ 22:59':,
            '23:05 ~ 23:59':,
            '00:05 ~ 00:59':,
            '01:05 ~ 01:59':,
            '02:05 ~ 02:59':,
            '03:05 ~ 03:59':,
            '04:05 ~ 04:59':,
            '05:05 ~ 05:59':,
            '06:05 ~ 06:59':,
            '07:05 ~ 07:59':,
            '08:05 ~ 08:59':,
            '09:05 ~ 09:59':,
            '10:05 ~ 10:59':,
            '11:05 ~ 11:59':,
            '12:05 ~ 12:59':,
            '13:05 ~ 13:59':,
            '14:05 ~ 14:59':,
            '15:05 ~ 15:59':,
            '16:05 ~ 16:59':,
            '17:05 ~ 17:59':,
            '18:05 ~ 18:59':,
            '19:05 ~ 19:59':,
            '20:05 ~ 20:59':
        ]

def acao(dia_da_semana):
    for x in acao_da_colonia.worksheets(f'{dia_da_semana}'):
        print(x.title)
        rows = range(1, 27)
        for l in rows:
            print(f'{x.cell(l, 1).value}==>{x.cell(l, 2).value}')


if __name__ == "__main__":
    now = datetime.datetime.now()
    indice_da_semana = now.weekday()
    dia_da_semana = DIAS[indice_da_semana]
    print(now.time())

    print(datetime.time() > now.time())
