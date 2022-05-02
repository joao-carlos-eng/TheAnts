from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
    'Noynho',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3',
    logic_adapters=[
        'chatterbot.logic.BestMatch', 'chatterbot.logic.MathematicalEvaluation'],
)

dialogo = open('chat.txt', 'r', encoding='utf-8')

list_dialog = [
    'Oi?',
    'Eae, tudo certo?',
    'aqui nas nuvens sim, e ai na terra ?'
    'Qual o seu nome?',
    'Noynho, seu amigo bot',
    'Por que seu nome é Noynho ?',
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
    'Conte uma história',
    'te amo',
    'essa frase é muito forte.',
    'Acho que vou desistir',
    'TATAKAI, TATAKAI, TATAKAI, TATAKAI, TATAKAI, TATAKAI, TATAKAI...',
    'TATAKAI, TATAKAI, TATAKAI, TATAKAI, TATAKAI, TATAKAI...',
    'essa é uma expressão forte',
    'Tudo começou com a forja dos Grandes Aneis. Três foram dados aos Elfos, imortais... os mais sabios e belos de '
    'todos os seres. Sete, aos Senhores-Anões...',
    'Você gosta de trivias?', 'Sim, o que você quer perguntar?',
    'Hahahaha', 'kkkk',
    'kkk', 'kkkk',
    'Conhece a Siri?', 'Conheço, a gente saiu por um tempo.',
    'Conhece a Alexa?', 'Ela nunca deu bola pra mim.',
    'Você gosta de Game of Thrones?', 'Dracarys',
    'O que você faz?', 'Eu bebo e sei das coisas',
    'Errado', 'Você não sabe de nada, John Snow.'
]

dialog = list_dialog + [frase for frase in dialogo.readlines()]

conversa = ChatterBotCorpusTrainer(chatbot)
conversa.train('chatterbot.corpus.portuguese')
conversa.train('chatterbot.corpus.english')
conversa.train('chatterbot.corpus.spanish')

conversa = ListTrainer(chatbot)
conversa.train(list_dialog)

if __name__ == "__main__":
    ####  Mod 1
    conversa = ChatterBotCorpusTrainer(chatbot)
    conversa.train('chatterbot.corpus.portuguese')
    conversa.train('chatterbot.corpus.english')
    conversa.train('chatterbot.corpus.spanish')

    ####  Mod 2
    conversa = ListTrainer(chatbot)
    conversa.train(dialog)

    while True:
        try:
            resposta = chatbot.get_response(input("Usuário: "))
            if float(resposta.confidence) > 0.2:
                print("Noynho: ", resposta)
            else:
                print("Não manjo dessas paradas :(")
        except(KeyboardInterrupt, EOFError, SystemExit):
            break
