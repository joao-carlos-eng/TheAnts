from edificios.edificio import Edificio


class Requirements:
    def __init__(self, *args):
        self.args = args
        self.comida = 0
        self.plantas = 0
        self.fungo = 0
        self.terra = 0
        self.areia = 0
        self.melado = 0
        self.tempo = 0

        for x in self.args:
            pass


if __name__ == '__main__':
    ed = Edificio()
