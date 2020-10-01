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

	def primeiro(self):
		return self.fila[0]


	def tamanho_fila(self):
		return len(self.fila)

	
	def mostra_fila(self):
		print(self.fila)


	def retorna_fila(self):
		return self.fila

	def em_ordem(self):
		fila_crescente = []
		
		array = self.fila
		while len(array):
			menor = array[0]
			for numero in array:
				if numero < menor:
					menor = numero
			array.remove(menor)
			fila_crescente.append(menor)

		for i in self.fila:
			self.desenfila()
		
		return fila_crescente


