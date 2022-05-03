import requests

from conexao_sheets import plan
from conexao_fire_base import get
# import json
# import csv
# import gzip
# import io
# from bs4 import BeautifulSoup
# from unicodedata import normalize

sheets = plan.worksheets()


def criar_txt_de_folhas():
    folha1 = open('folhas.txt', '+w', encoding='utf-8')

    for sheet in sheets:
        print(sheet.title, sheet.id)
        folha1.write(f'{sheet.title},{sheet.id}\n')


def convert_str_to_time(schedule: str):
    if '~' in schedule:
        ini, fin = schedule.split(' ~ ')
        h_ini = [int(x) for x in ini.split(':')]
        h_fin = [int(x) for x in fin.split(':')]
        return h_ini, h_fin
    else:
        return [int(x) for x in schedule.split(':')]


def consultar_edificio(nome, nivel):
    response = get(f'Edificios/{nome}/NVL {nivel}')
    if not response:
        return 'Opa, reveja os parâmetros passados.'

    result = ''
    for k, v in response.items():
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


def listar_edificios():
    response = get(f'Edificios/')

    result = ''
    for x in response.keys():
        result += f'{x}\n'

    return result


"""def encode(name):
    ascii_name = normalize("NFKD", name).encode("ascii", errors="ignore").decode("ascii")
    return ascii_name.upper()


def dictionary(palavra):
    encoded_name = encode(palavra)
    url = f"https://www.google.com/search?q={palavra}&oq={palavra}&aqs=chrome.0.69i59j0i512l5j69i60j69i61" \
          ".2671j1j4&sourceid=chrome&ie=UTF-8 "
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    soup.find_all(class_='vmod')
    return soup.find_all(class_='vmod')"""


"""def encode(name):
    ascii_name = normalize("NFKD", name).encode("ascii", errors="ignore").decode("ascii")
    return ascii_name.upper()


def classify_api(name):
    encoded_name = encode(name)
    url = "https://brasil.io/api/dataset/genero-nomes/nomes/data?first_name=" + encoded_name
    response = urlopen(url)
    json_response = json.loads(response.read())
    return json_response["results"][0]["classification"]


def load_data():
    fobj = io.TextIOWrapper(gzip.open("nomes.csv.gz"), encoding="utf-8")
    csv_reader = csv.DictReader(fobj)
    data = {
        row["first_name"]: row["classification"]
        for row in csv_reader
    }
    fobj.close()
    return data


def classify_download(name):
    name_data = load_data()
    encoded_name = encode(name)
    return name_data[encoded_name]"""

if __name__ == '__main__':
    ...
    # txt = open('saida.txt', 'w+')
    # txt.write(consultar_edificio("rainha", 1))

    # print(consultar_edificio("rainha", 1))
    # listar_edificios()

    # print(dictionary("malrry"))
