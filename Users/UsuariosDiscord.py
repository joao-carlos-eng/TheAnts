class Players:
    def __init__(self, id_discord):
        self.dic = None
        self.id_discord = id_discord
        self.nickGame = None
        self.alianca = None
        self.cargo = None
        self.nickDiscord = None
        self.name = None
        self.genero = None
        self.dialogos = []
        self.elogios = []
        self.insultos = []
        self.saudacoes = []
        self.tratamentos = []

    def criar(self, response, author):
        self.dic = dict(response)
        self.name = self.dic['name']
        self.nickDiscord = author
        self.cargo = self.dic['cargo']
        self.alianca = self.dic['alianca']
        self.tratamentos = list(self.dic['tratamentos'])
        self.saudacoes = list(self.dic['saudacoes'])
        self.insultos = list(self.dic['insultos'])
        self.elogios = list(self.dic['elogios'])
        self.dialogos = list(self.dic['elogios'])

    def consultar(self, key):
        return self.dic[key]

    def atualiza(self, lis):
        self.dic[lis[0]] = lis[1]
