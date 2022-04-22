from conexao_sheets import plan
from conexao_fire_base import get

sheets = plan.worksheets()


def criar_txt_de_folhas():
    folha1 = open('folhas.txt', '+w', encoding='utf-8')

    for sheet in sheets:
        print(sheet.title, sheet.id)
        folha1.write(f'{sheet.title},{sheet.id}\n')


def consultar_edificio(nome, nivel):
    print(get(f'{nome}/NVL {nivel}'))

    return get(f'{nome}/NVL {nivel}')


if __name__ == '__main__':
    consultar_edificio("rainha", 1)
