import random
import re

texto1 = """abafa-a-palhinha, abécula, abelhudo, abichanado, abutre, agarrado, agiota, agressivo, alarve, alcouceira, 
alcoviteira, aldrabão, aleivoso, amalucado, amarelo, amaneirado, amigo-da-onça, analfabeto, analfabruto, animal, 
anormal, apanhado do clima, aparvalhada, apóstata, arrelampado, arrogante, artolas, arruaceiro, aselha, asno, 
asqueroso, atarantada, atrasado mental, atraso de vida, avarento, avaro, ave rara, aventesma, azeiteiro, bacoco, 
bácoro, badalhoca, badameco, baixote, bajulador, baldas, baleia, balhelhas, balofo, banana, bandalho, bandido, 
barata tonta, bárbaro, bardajona, bardamerdas, bargante, barrigudo, basbaque, basculho, bastardo, batoque, batoteiro, 
beata, bebedanas, bebedolas, beberrão, besta, besta quadrada, bexigoso, bicho do mato, biltre, bimbo, bisbilhoteira, 
boateiro, bobo, boca de xarroco, boçal, bode, bófia, boi, boneca de trapos, borracho, borra-botas, bota de elástico, 
brochista, bronco, brutamontes, bruto, bruxa, bufo, broxa, burgesso, burlão, burro cabeça de abóbora, 
cabeça-de-alho-chôcho, cabeça-de-vento, cabeça no ar, cabeça oca, cabeçudo, cabotino, cabra, cabrão, cábula, 
caceteiro, cachorro, caco, cadela, caga-leite, caga-tacos, cagão, caguinchas, caixa de óculos, calaceiro, calão, 
calhandreira, calhordas, calinas, caloteiro, camafeu, camelo, campónio, canalha, canastrão, candongueiro, cão, 
caquética, cara-de-cu-à-paisana, caramelo, carapau de corrida, careca, careta, carniceiro, carraça, carrancudo, 
carroceiro, casca grossa, casmurro, cavalgadura, cavalona, cegueta, celerado, cepo, chalado, chanfrado, charlatão, 
chatarrão, chato, chauvinista, chibo, chico-esperto, chifrudo, choné, choninhas, choramingas, chulo, chunga, 
chupado das carochas, chupista, cínico, cobarde, cobardolas, coirão, comuna, cona-de-sabão, convencido, corno, 
cornudo, corrupto, coscuvilheira, coxo, crápula, cretino, cromo, cromaço, cunanas, cusca, debochado, delambida, 
delinquente, demagogo, demente, demônio, depravado, desajeitado, desastrada, desaustinado, desavergonhada, desbocado, 
desbragado, descabelada, desdentado, desengonçado, desgraçado, deshumano, deslavado, desleal, desmancha prazeres, 
desmazelada, desmiolado, desengonçado, desenxabida, desonesto, despistado, déspota, destrambelhado,  destravada, 
destroço, desvairado, devasso, diabo, ditador, doidivanas, doido varrido, dondoca, doutor da mula russa, drogado, 
egoísta, embirrento, embusteiro, empata-fodas, empecilho, emplastro, enconado, energúmeno, enfadonho, enfezado, 
engraxador, enjoado da trampa, enrabador, escanifobética, escanzelada, escarumba, escrofuloso, escroque, escumalha, 
esgalgado, esganiçada, esgroviada, esguedelhado, espalha-brasas, espalhafatoso, espantalho, esparvoado, 
esqueleto vaidoso, estafermo, estapafúrdio, estouvada, estroina, estropício, estulto, estúpido, estupor, faccioso, 
facínora, fala-barato, falhado, falsário, falso, fanático, fanchono, fanfarrão, fantoche, fariseu, farrapo, 
farropilha, farsante, farsolas, fatela, fedelho, feia-comó-demo, fersureira, figurão, filho da mãe, filho da puta, 
fingido, fiteiro, flausina, foção, fodido, fodilhona, foleiro, forreta, fraco-de-espírito, fraca figura, franganote, 
frangueiro, frasco, frígida, frícolo, frouxo, fufa, fuinha, fura-greves, fútil, gabarola, gabiru, galdéria, 
galinha choca, ganancioso, gandim, gandulo, garganeira, gato pingado, gatuno, gazeteiro, glutão, gordalhufo, gordo, 
gosma, gralha, grosseiro, grotesco, grunho, guedelhudo, herege, hipócrita, histérica, idiota, ignorante, imaturo, 
imbecil, impertinente, impostor, incapaz, incompetente, inconveniente, indecente, indigente, indolente, inepto, 
infame, infeliz, infiel, imprudente, intriguista, intrujona, invejoso, insensivel, insignificante, insípido, 
insolente, intolerante, intriguista, inútil, irritante, javardo, labrego, labroste, lacaio, ladrão, lambão, 
lambareiro, lambe-botas, lambéconas, lambisgóia, lamechas, lapa, larápio, larilas, lavajão, lerdo, lesma, 
leva-e-traz, libertino, limitado, língua-de-trapos, língua viperina, linguareira, lingrinhas, lontra, lorpa, louco, 
lunático, má rês, madraço, mafioso, maganão, magricela, malcriado, mal enjorcado, mal fodida, malacueco, malandreco, 
malandrim, malandro, malfeitor, maltrapilho, maluco, malvado, mamalhuda, mandrião, maneta, mangas-de-alpaca, manhoso, 
maníaco, manipulador, maniqueista, manteigueiro, maquiavélico, marado-dos-cornos, marafado, marafona, marginal, 
maria-vai-com-as-outras, maricas, mariconço, mariola, mariquinhas-pé-de-salsa, marmanjo, marrão, marreco, masoquista, 
mastronço, matarroano, matrafona, matrona, mau, medíocre, medricas, medroso, megera, meia-leca, meia-tijela, melga, 
meliante, menino da mamã, mentecapto, mentiroso, merdas, merdoso, mesquinho, metediço, mijão, mimado, mineteiro, 
miserável, mixordeiro, moina, molengão, mongas, monhé, mono, monstro, monte-de-merda, mórbido, morcão, mosca morta, 
mostrengo, mouco, mula, múmia, nababo, nabo, não-fode-nem-sai-de-cima, não-tens-onde-cair-morto, narcisista, 
narigudo, nariz-arrebitado, nazi, necrófilo, néscio, nhonhinhas, nhurro, ninfomaníaca, nódoa, nojento, nulidade, 
obcecado, obnóxio, obstinado, obtuso, olhos-de-carneiro-mal-morto, onanista, oportunista, ordinário, 
orelhas-de-abano, otário, pacóvio, padreca, palerma, palhaço, palhaçote, palonça, panasca, paneleiro, panhonhas, 
panilas, pantomineiro, papa-açorda, papagaio, papalvo, paranóico, parasita, pária, parolo, parvalhão, parvo, 
paspalhão, paspalho, passado, passarão, pata-choca, patarata, patego, pateta, patife, patinho feio, pato, pató, 
pau-de-virar-tripas, pedante, pederasta, pedinchas, pega-de-empurrão, peida-gadoxa, pelintra, pendura, peneirenta, 
pequeno burguês, pérfido, perliquiteques, pernas-de-alicate, pés de chumbo, peso morto, pesporrente, petulante, 
picuinhas, piegas, pilha-galinhas, pílulas, pindérica, pinga-amor, pintas, pinto calçudo, piolho, piolhoso, 
pirata, piroso, pitosga, pobre de espírito, pobretanas, poltrão, popularucho, porcalhão, porco, pote de banhas, 
preguiçoso, presunçoso, provocador, proxeneta, pulha, punheteiro, puta, putéfia, quadrilheira, quatro-olhos, 
quebra-bilhas, queixinhas, quezilento, rabeta, rabugento, radical, rafeiro, ralé, rameira, rameloso, rancoroso, 
ranhoso, raquítico, rasca, rascoeira, rasteiro, rata de sacristia, reaccionário, reaças, reles, repelente, 
ressabiado, retardado, retorcido, ridículo, roto, rufia, rústico, sabujo, sacana, sacripanta, sacrista, sádico, 
safado, safardana, salafrário, saloio, salta-pocinhas, sandeu, sarnento, sarrafeiro, sebento, seboso, sem classe, 
sem vergonha, serigaita, sevandija, sicofanta, simplório, snob, soba, sodomita, soez, somítico, sonsa, sórdido, 
sorna, sovina, suíno, sujo, tacanho, tagarela, tanso, tarado, taralhouca, tavolageiro, teimoso, tinhoso, tísico, 
títere, toleirão, tolo, tonto, torpe, tosco, totó, trabeculoso, trafulha, traiçoeiro, traidor, trambolho, trapaceiro, 
trapalhão, traste, tratante, trauliteiro, tresloucado, trinca-espinhas, trique-lariques, triste, troca-tintas, 
troglodita, trombalazanas, trombeiro, trombudo, trouxa, unhas de fome, untuoso, urso, vaca gorda, vadio, vagabundo, 
vaidoso, valdevinos, vândalo, velhaco, velhadas, vendido, verme, vesgo, víbora, viciado, vigarista, vígaro, vil, 
vilão, vira-casacas, Xé-xé, xico esperto, zarolho, zé-ninguém, zelota, zero à esquerda"""

insultos = [re.sub("[\n]", '', insulto) for insulto in texto1.split(", ")]

texto2 = 'Bela • Amorosa • Inteligente • Destemida • Adorável • Apaixonante • Bondosa • Trabalhadora • Brilhante • ' \
         'Carinhosa • Charmosa • Confiante • Doce • Delicada • Educada • Corajosa • Esperta • Forte • Esbelta • ' \
         'Calorosa • Simpática • Espetacular • Serena • Glamurosa • Humilde • Impressionante • Irresistível • Jeitosa' \
         ' • Incrível • Única • Linda • Maravilhosa • Mágica • Majestosa • Sexy • Otimista • Perseverante • Poderosa' \
         ' • Protetora • Prodígio • Protetora • Romântica • Simpática • Sensacional • Sagaz • Sedutora • Sofisticada' \
         ' • Talentosa • Terna • Verdadeira • Visionária • Livre • Modesta • Meiga • Legítima • Iluminada'

texto3 = "Carinhoso • Amoroso • Belo • Lindo • Destemido • Gracioso • Apaixonante • Bondoso • Meigo • Protetor • " \
         "Corajoso • Sereno • Forte • Esbelto • Poderoso • Único • Incrível • Esbelto • Maravilhoso • Modesto • " \
         "Humilde • Charmoso • Talentoso • Simpático • Legítimo • Visionário • Talentoso • Terno • Livre • Caloroso • " \
         "Sensacional • Confiante • Verdadeiro • Irresistível • Doce • Justo • Gentil • Intelectual • Impecável • " \
         "Impressionante • Genial • Formoso • Fofo • Franco • Leal • Encantador • Extraordinário • Especial • " \
         "Delicado • Deslumbrante • Elegante • Ideal • Idílico • Incansável • Devoto • Equilibrado • Extrovertido"
texto4 = ""
elogios = [elog.lower() for elog in texto3.split(' • ')] + [elog.lower() for elog in texto2.split(' • ')]


def elogio(pronome='M'):
    if pronome == 'F':
        return [elog for elog in texto2.split(" • ")]
    else:
        return [elog for elog in texto3.split(" • ")]


mod1 = ['Olá!', 'Oi!', 'Qual é o seu nome?', 'Seja bem-vindo(a)!', 'E aí!', 'Opa!', 'Fala aí, cara!', 'Beleza brother?',
        'Qual é?']

mod2 = ['Como vai?', 'Como vão as coisas?', 'Como você tem estado?', 'Como você tem passado?',
        'O que está acontecendo?', 'E aí? O que você me conta?', 'O que você conta de novo?', 'Quais são as novidades?',
        'Onde você esteve esses anos?', 'Por onde você andava?', 'Quanto tempo!', 'Faz um tempão que eu não te vejo.',
        'Há quanto tempo não te vejo!', 'Você sumiu!', 'Prazer em conhecê-lo!', 'Prazer em conhecer você também!',
        'O prazer é meu!', 'É sempre um prazer te ver!']

mod3 = ['Até logo!', 'Até a próxima!', 'Até amanhã!', 'Tchau!', 'Prazer em conhecê-lo!', 'Se cuida!',
        'Bom fim de semana!', 'Tenha um bom dia!', 'Até!']


def saudacao(frase):
    print('entrou na saudacao: frase--', frase)
    if 'bom dia' in frase.lower():
        return 'Bom dia !'
    elif 'boa tarde' in frase.lower():
        return 'Boa tarde !'
    if 'boa noite' in frase.lower():
        return 'Boa noite !'
    if any(word.lower() in frase.lower() for word in mod1):
        return random.choice(mod1)
    elif any(word.lower() in frase.lower() for word in mod2):
        return random.choice(mod2)
    elif any(word.lower() in frase.lower() for word in mod3):
        return random.choice(mod3)

    return False


def insultar(frase, pronome='M'):
    if pronome == 'F':
        lista = [insulto for insulto in insultos if insulto.endswith('a')]
    else:
        lista = [insulto for insulto in insultos if insulto.endswith('o')]

    if any(word.lower() in frase.lower().split() for word in insultos):
        return random.choice(lista)

    # print(list(lista))


if __name__ == "__main__":
    print(insultar('Noynho vil', 'N'))
