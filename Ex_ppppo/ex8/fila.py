class Fila:

	def __init__(self):
		self.fila = []


	def is_vazia(self):
		return self.fila == []


	def enfila(self, item):
		self.fila.append(item)


	def desenfila(self):
		if not self.is_vazia():
			return self.fila.pop(0)
		return 'A fila está vazia.'

	def pega_item(self):
		return self.fila[0]


	def tamanho_fila(self):
		return len(self.fila)

	
	def mostra_fila(self):
		print(self.fila)


	def retorna_fila(self):
		return self.fila