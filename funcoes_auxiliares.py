from conexao_sheets import plan

sheets = plan.worksheets()


def criar_txt_de_folhas():
    folha1 = open('folhas.txt', '+w', encoding='utf-8')

    for sheet in sheets:
        print(sheet.title, sheet.id)
        folha1.write(f'{sheet.title},{sheet.id}\n')
