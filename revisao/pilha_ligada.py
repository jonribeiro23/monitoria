class Node:
    def __init__(self, x):
        self.info = x
        self.next = None

    def get_info(self):
        return self.info

    def get_next(self):
        return self.next



class PilhaLigada:
    def __init__(self):
        self.topo = None

    def empilha(self, x):
        aux = Node(x)
        aux.next = self.topo
        self.topo = aux

    def desempilha(self):
        temp = self.topo.info
        self.topo = self.topo.next
        # self.topo.next = None
        return temp

    def elementodotopo(self):
        return self.topo

    def pilhavazia(self):
        return self.topo == None

    def getTopo(self):
        return self.topo

    def mostra(self):
        no_atual = self.topo
        while no_atual != None:
            print(no_atual.get_info())
            no_atual = no_atual.get_next()
        print('')









