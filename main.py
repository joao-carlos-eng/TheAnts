from noynho.funcoes_auxiliares import criar_txt_de_folhas

if __name__ == '__main__':
    try:
        folhas = open('folhas.txt', 'r')
    except FileNotFoundError:
        criar_txt_de_folhas()
        folhas = open('folhas.txt', 'r')

    