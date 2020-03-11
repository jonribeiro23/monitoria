import time
class Teatro:
	def __init__(self, linha, coluna):
		self.linha = linha
		self.coluna = coluna
		self.qtd = 0
		self.tamanho = linha*coluna
		self.teatro = []


		for i in range(self.get_linha()):
			linha = []
			for j in range(self.get_coluna()):
				linha.append(False)
			self.teatro.append(linha)


	def exibe_teatro(self):
		for i in range(self.get_linha()):
			for j in range(self.get_coluna()):
				# time.sleep(0.2)
				print(self.teatro[i][j], end=' ')
			print()


	def vende_ingresso(self, linha, coluna):
		if self.teatro[linha][coluna] == True:
			print('Lugar ocupado')
		else:
			self.teatro[linha][coluna] = True
			self.incrementa()

	
	def devolve_ingresso(self, linha, coluna):
		if self.teatro[linha][coluna] == False:
			print('Não há reservas para esse ingresso')
		else:
			self.teatro[linha][coluna] = False
			self.decrementa()


	def trocar_ingresso(self, linha_antiga, coluna_antiga, linha_nova, coluna_nova):
		if self.teatro[linha_nova][coluna_nova] == True:
			print('Impossível trocar. O lugar já está ocupado')
		else:
			self.teatro[linha_nova][coluna_nova] = True
			self.teatro[linha_antiga][coluna_antiga] = False


	def incrementa(self):
		self.qtd += 1


	def decrementa(self):
		self.qtd -= 1
	
	
	# ==== GETTERS e SETTERS ===
	def get_linha(self):
		return self.linha


	def get_coluna(self):
		return self.coluna


	def get_qtd(self):
		return self.qtd
