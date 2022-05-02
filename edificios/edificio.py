from conexao_fire_base import get


class Edificio:
    def __init__(self):
        self.nivel = 0
        self.poder = 0.0
        # self.plannta_emergencia = 0.0
        self.others = ''
        self.requisito1 = None
        self.requisito2 = None

    def criar(self, name, level):
        response = get(f'Edificios/{name}/NVL {level}')
        self.nivel = int(level)
        self.poder = response['Potncia']

        if response.get('Formiga Pop'):
            self.others = response['Formiga Pop']

