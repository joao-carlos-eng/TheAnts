import requests
import json

link = "https://theantsbot-default-rtdb.firebaseio.com/"

"""
Como salvar dados
PUT	    Grave ou substitua dados em um caminho definido, como fireblog/users/user1/<data>
PATCH	Atualize algumas chaves de um caminho específico sem substituir todos os dados.
POST	Adicione a uma lista de dados do banco de dados do Firebase. Sempre que uma solicitação POST é enviada, o cliente do Firebase gera uma chave exclusiva, como fireblog/users/<unique-id>/<data>
DELETE	Remova os dados da referência especificada de banco de dados do Firebase.

"""


def post(tabela: str, dados):
    """

        :param dados: dicionario com os dados a serem criados
        :param tabela: string com o caminho onde se deve criar o POST
        :return: retorna o codigo do response
        """
    requisicao = requests.post(f'{link}/{tabela}.json', dados)
    print(requisicao)
    print(requisicao.text)


def put(tabela: str, dados):
    """

        :param dados: dicionario com os dados a serem criados
        :param tabela: string com o caminho onde se deve criar o PUT
        :return: retorna o codigo do response
        """
    requisicao = requests.put(f'{link}/{tabela}.json', dados)
    print(requisicao)
    # print(requisicao.text)


def get(tabela: str):
    requisicao = requests.get(f'{link}/{tabela}/.json')
    print(requisicao)
    # print(requisicao.json())

    return requisicao.json()


if __name__ == '__main__':
    data = {'LVL': '8', 'Comida': 'None', 'Planta': 'None', 'Fungo ': 'None', 'Terra mida ': 'None', 'Areia': 'None',
            'Melado ': 'None', 'Tempo hms ': 'None', 'Dias': 'None', 'Horas': '0', 'P Aumento': '247',
            'Hora dh ': '0d3h', 'Diamantes ': '419', 'Potncia P': 'None', 'Formiga Pop': '0', 'Requisito ': 'None'}

    test = open('jj.json', 'w+')
    test.write(f'{data}')
