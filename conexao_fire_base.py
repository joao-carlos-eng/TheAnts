import requests
import json

link = "https://theantsbot-default-rtdb.firebaseio.com/"

"""
POST = cria
requisicao = requests.post(f'{link}/tabela/.json', data=json.dumps(dados))
dados - do tipo json, dicionario com os dados
GET = solicita
DELETE = ...
PATCH = modifica

"""


def post(tabela: str, dados):
    """

        :param dados: dicionario com os dados a serem criados
        :param tabela: string com o caminho onde se deve criar o POST
        :return: retorna o codigo do requests
        """
    requisicao = requests.post(f'{link}/{tabela}/.json', dados)
    print(requisicao)
    print(requisicao.text)
