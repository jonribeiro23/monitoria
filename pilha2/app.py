import pilha

pilha = pilha.Pilha()

pilha.empilha(2)
pilha.empilha(9)
pilha.empilha(26)
pilha.empilha(29)
pilha.empilha(260)
print('=============')
print('Mostra pilha')
pilha.mostra_pilha()
print('=============')

pilha.desempilha()

print('=============')
print('Mostra pilha')
pilha.mostra_pilha()
print('=============')


print(pilha.pilha_cheia())

print('=============')
print('Elemento do topo')
print(pilha.elemento_do_topo())

print('=============')


pilha.desempilha()
pilha.desempilha()
pilha.pilha_vazia()
pilha.desempilha()
pilha.desempilha()
pilha.desempilha()
print('=============')
print('Pilha vazia')
# print(pilha.pilha_vazia())

print('=============')
