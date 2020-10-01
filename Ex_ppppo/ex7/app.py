from pilha import Pilha
from fila import Fila

p = Pilha()
f = Fila()

p.empilha('Manoel')
p.empilha('Paloma')
p.empilha('Marcio')
p.empilha('Rosangela')
p.empilha('Paula')
p.empilha('Nayma')
print('Pilha:')
p.mostra_pilha()

pilha_de_nomes = p.retorna_pilha()
for nome in pilha_de_nomes:
    f.enfila(nome)

print('Fila:')
f.mostra_fila()