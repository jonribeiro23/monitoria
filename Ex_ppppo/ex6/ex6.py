from pilha import Pilha

p = Pilha()
def dec2bin(n):
    while n != 0:
        p.empilha(str(n % 2))
        n = int(n / 2)
    return p.mostra_pilha()