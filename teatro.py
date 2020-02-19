class Teatro():
	
	def __init__(self, linha, coluna):
		self.linha = linha
		self.coluna = coluna
		self.qtd = 0
		self.tamanho = linha*coluna
		self.teatro = []

		self.monta_teatro()


	def monta_teatro(self):
		cadeiras = []
		for i in range(self.get_linha()):
			for j in range(self.get_coluna()):
				cadeiras.append(False)


	def exibe_teatro(self, arg):
		for i in range(self.linha):
			for j in range(self.coluna):
				print(arg[i][j], end='')
			print()


	def get_linha(self):
		return self.linha

	def get_coluna(self):
		return self.coluna


	def get_teatro(self):
		return self.teatro
