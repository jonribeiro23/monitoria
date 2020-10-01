from pilha import Pilha
from fila import Fila
from random import randint

p = Pilha()
f = Fila()

for i in range(10):
    numero_aleatorio = randint(20, 30)
    f.enfila(numero_aleatorio)

p.empilha(f.desenfila())

while not f.is_vazia():
    # try:
    #     if f.primeiro() <= p.topo() or p.is_vazia():
    #         p.empilha(f.desenfila())
    #     else:
    #         f.enfila(p.desempilha())
    # except IndexError:
    #     p.empilha(f.desenfila())

    
    if p.is_vazia() or f.primeiro() <= p.topo():
        p.empilha(f.desenfila())
    else:
        f.enfila(p.desempilha())

f.mostra_fila()
p.mostra_pilha()
