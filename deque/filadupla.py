class FilaDupla:
	def __init__(self):
		self.deke = []


	def colocar(self, item):
		self.deke.append(item)


	def colocar_na_esquerda(self, item):
		self.deke.insert(0, item)


	def deletar(self):
		deletado = self.deke[-1]
		self.deke.pop()
		return deletado


	def deletar_da_esquerda(self):
		deletado = self.deke[0]
		self.deke.pop(0)
		return deletado


	def mostrar(self):
		print(self.deke)


