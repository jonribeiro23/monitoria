# Collections: Counter, namedtuple, OrderedDict, defaultdict, deck
from collections import Counter, namedtuple
from random import choice
from pprint import pprint

# == Counter ==
'''cria um dicionário a partir de elementos para ele passado, onde
os elementos são as chaves e o número de vezem que o elemento
aparece são os valores'''

a = 'aaabbcccdddd'
frase = 'esta e uma frase'
my_counter = Counter(a)

# retorna dicionário
print(my_counter)

# retorna os itens
print(my_counter.items())

# retorna os elementos como um objeto interável
print(my_counter.elements())

#retorna as chaves
print(my_counter.keys())

# retorna os elementos que mais se repetem
print(my_counter.most_common())
# pode-se passa o nº de elementos mais comuns que se deseja retornar
print(my_counter.most_common(1))
# pode-se acessar o elemento através de índices
print(my_counter.most_common(1)[0][0])
print(my_counter.most_common(1)[0][1])

# lendo um texto e contando palavras
import re
words = re.findall(r'\w+', open('poema.txt').read().lower())
palavras = Counter(words).most_common(10)
print(palavras)
print()
print('='*40)
print()


# === NAMEDTUPLE ===
'''Retorna uma subclasse. É utilizada para criar objetos semelhantes
a tuplas que possuem campos acessíveis, como atributos, sendo também 
indexáveis e iteráveis.'''

Point = namedtuple('Point', 'x,y')
pt = Point(1, -3)
print(pt)

# acessando os atributos
print(pt.x)
print(pt.y)

# Exemplo

Card = namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
	ranks = [str(n) for n in range(2, 11)] + list('JQKA')
	suits = 'spades diamonds clubs hearts'.split()

	def __init__(self):
		self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

	def __len__(self):
		return len(self._cards)

	def __getitem__(self, position):
		return self._cards[position]



beer_card = Card('7', 'diamonds')
print(beer_card)

deck = FrenchDeck()
print(len(deck))
print(deck[32])
pprint(deck[12:20])
print()

# pegar uma carta aleatória do baralho
print(choice(deck))

# imprimir tudo
for card in reversed(deck):
	print(card)
print()

#dando valor às cartas
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
	rank_value = FrenchDeck.ranks.index(card.rank)
	return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
	print(card)