from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


def neural(chat):
    chatbot = ChatBot(
        'Noynho',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='sqlite:///database.sqlite3',
        logic_adapters=[
            'chatterbot.logic.BestMatch', 'chatterbot.logic.MathematicalEvaluation'],
    )

    list_dialog = [
        'Oi?',
        'Eae, tudo certo?',
        'aqui nas nuvens sim, e ai na terra ?'
        'Qual o seu nome?',
        'Noynho, seu amigo bot',
        'Por que seu nome é esse ?',
        'Noynho é meu nome porque sou o bot da aliança NoY(No Mercy)',
        'Prazer em te conhecer',
        'Igualmente meu querido',
        'Quantos anos você tem?',
        'Eu nasci em 2022, faz as contas, rs.',
        'Você gosta de videogame?',
        'Eu sou um bot, eu só apelo.',
        'Qual a capital da Islândia?',
        'Reikjavik, lá é muito bonito.',
        'Qual o seu personagem favorito?',
        'Gandalf, o mago.',
        'Qual a sua bebida favorita?',
        'Eu bebo café, o motor de todos os programas de computador.',
        'Qual o seu gênero?',
        'Sou um chatbot e gosto de algoritmos',
        'eu te amo',
        'essa frase é muito forte.',
        'Acho que vou desistir',
        'TATAKAI, TATAKAI, TATAKAI, TATAKAI, TATAKAI, TATAKAI, TATAKAI...',
        'TATAKAI, TATAKAI, TATAKAI, TATAKAI, TATAKAI, TATAKAI...',
        'Conte uma história',
        'Tudo começou com a forja dos Grandes Aneis. Três foram dados aos Elfos, imortais... os mais sabios e belos de '
        'todos os seres. Sete, aos Senhores-Anões...',
        'Você gosta de trivias?', 'Sim, o que você quer perguntar?',
        'Hahahaha', 'kkkk',
        'kkk', 'kkkk', 'eu sou o seu pai', 'naaaooooo',
        'Conhece a Siri?', 'Conheço, a gente saiu por um tempo.',
        'Conhece a Alexa?', 'Ela nunca deu bola pra mim.',
        'Você gosta de Game of Thrones?', 'Dracarys',
        'O que você faz?', 'Eu bebo e sei das coisas',
        'Errado', 'Você não sabe de nada, John Snow.'
    ]

    dialogo_completo = list_dialog + [frase.capitalize() for frase in chat.readlines()]

    conversa = ChatterBotCorpusTrainer(chatbot)
    conversa.train('chatterbot.corpus.portuguese')
    # conversa.train('chatterbot.corpus.english')
    # conversa.train('chatterbot.corpus.spanish')

    conversa = ListTrainer(chatbot)
    conversa.train(dialogo_completo)

    return chatbot


class Neural:
    def __init__(self, chatbot):
        self.confidence = 0.5
        self.__dialogos = []
        self.chatbot = chatbot
        self.__conversa = None

    def carregar_dialogos(self, dialogo):
        self.__dialogos = self.__dialogos + [frase.capitalize() for frase in dialogo.readlines()]

    def treinar(self, metodo='lista'):
        if metodo == 'corpus':
            conversa = ChatterBotCorpusTrainer(self.chatbot)
            conversa.train('chatterbot.corpus.portuguese')
        elif metodo == 'lista':
            conversa = ListTrainer(self.chatbot)
            conversa.train(self.__dialogos)

    def response(self, frase):
        try:
            resposta = self.chatbot.get_response(frase)
            if float(resposta.confidence) > self.confidence:
                print("Noynho: ", resposta)
                return resposta
            else:
                print("Não manjo dessas paradas :(")
                return 'opa, ainda não sei do que está falando :slight_frown:'
        except(KeyboardInterrupt, EOFError, SystemExit):
            print('erro interno')


if __name__ == "__main__":
    dialogo = open('../chat.txt', 'r', encoding='utf-8')
    chatbot = ChatBot(
        'Noynho',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='sqlite:///database.sqlite3',
        logic_adapters=[
            'chatterbot.logic.BestMatch', 'chatterbot.logic.MathematicalEvaluation'],
    )
    cb = Neural(chatbot)
    cb.carregar_dialogos(dialogo)
    cb.treinar()
    cb.treinar(metodo='lista')

    while True:
        try:
            resposta = cb.response(input("Usuário: "))
            print("Noynho: ", resposta)
            '''if float(resposta.confidence) > 0.5:
                print("Noynho: ", resposta)
            else:
                print("Não manjo dessas paradas :(")'''
        except(KeyboardInterrupt, EOFError, SystemExit):
            break
