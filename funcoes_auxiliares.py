from conexao_sheets import plan
from conexao_fire_base import get

sheets = plan.worksheets()


def criar_txt_de_folhas():
    folha1 = open('folhas.txt', '+w', encoding='utf-8')

    for sheet in sheets:
        print(sheet.title, sheet.id)
        folha1.write(f'{sheet.title},{sheet.id}\n')


def consultar_edificio(nome, nivel):
    response = get(f'Edificios/{nome}/NVL {nivel}')
    if not response:
        return 'Opa, reveja os parâmetros passados.'

    result = ''
    for k, v in response.items():
        text = ''
        if 'Tempo (h:m:s)' in k:
            text = k.replace('Tempo (h:m:s)', 'Tempo(h:mn:s)')
        elif 'time(h:m:s)' in k:
            text = k.replace('Tempo (h:m:s)', 'Tempo(h:mn:s)')
        elif 'mida' in k:
            text = k.replace('Terra mida', 'Terra úmida')
        elif 'Potncia (P)' in k:
            text = k.replace('Potncia (P)', 'Poder Aumentado')
        elif 'P Aumento' in k:
            text = k.replace('P Aumento', 'P. Acumulado/Total')
        else:
            text = k

        result += f'{text}: {v}\n'

    return result + '\ndestroy: irei apagar em 1min'


if __name__ == '__main__':
    # txt = open('saida.txt', 'w+')
    # txt.write(consultar_edificio("rainha", 1))
    print(consultar_edificio("rainha", 1))
