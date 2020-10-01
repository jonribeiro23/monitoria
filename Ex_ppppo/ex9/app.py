from pilha import Pilha
from fila import Fila
from random import randint

p = Pilha()
f = Fila()

for i in range(10):
    numero_aleatorio = randint(20, 30)
    f.enfila(numero_aleatorio)

for numero in f.em_ordem():
    p.empilha(numero)

print('Pilha:')
p.mostra_pilha()