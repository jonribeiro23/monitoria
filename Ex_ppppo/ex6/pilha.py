class Pilha:
	def __init__(self):
		self.pilha = []


	def is_vazia(self):
		return self.pilha == []


	def empilha(self, item):
		self.pilha.append(item)


	def desempilha(self):
		if not self.is_vazia():
			data = self.pilha[-1]
			del self.pilha[-1]
			return data
		return 'A pilha está vazia.'


	def pegar(self):
		return self.pilha[-1]


	def tamanho_pilha(self):
		return len(self.pilha)

	def mostra_pilha(self):
		print(self.pilha[::-1])