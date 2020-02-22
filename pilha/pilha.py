class Pilha:
	def __init__(self):
		self.pilha = []


	def is_vazia(self):
		return self.pilha == []


	def empilha(self, item):
		self.pilha.append(item)


	def desempilha(self):
		data = self.pilha[-1]
		del self.pilha[-1]
		return data


	def pegar(self):
		return self.pilha[-1]


	def tamanho_pilha(self):
		return len(self.pilha)