from pilha import Pilha
from fila import Fila

p = Pilha()
f = Fila()

f.enfila('Manoel')
f.enfila('Paloma')
f.enfila('Marcio')
f.enfila('Rosangela')
f.enfila('Paula')
f.enfila('Nayma')


fila_de_nomes = f.retorna_fila()
for nome in fila_de_nomes:
    p.empilha(nome)


print('Fila:')
f.mostra_fila()
print('')

print('Pilha:')
p.mostra_pilha()