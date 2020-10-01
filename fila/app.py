from fila import Fila

f = Fila()

f.enfila(2)
f.enfila(4)
f.enfila(6)
f.enfila(8)

f.mostra_fila()
print('O item removido foi: ', f.desenfila())
f.mostra_fila()
print('O primeiro item da fila é: ', f.pega_item())
print('O tamanho da fila é: ', f.tamanho_fila())