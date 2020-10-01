class Pilha:
	def __init__(self, tam=5):
		self.topo = -1
		self.tamanho = tam        
		self.elementos = []


	def empilha(self, item):
		if self.topo <= (self.tamanho-2):
			self.elementos.append(item)
			self.topo += 1
			print('meu topo: ', self.topo)
		else:
			print('Pilha cheia')


	def desempilha(self):
		if self.topo == -1:
			return 'A pilha já está vazia'
		else:
			item_que_foi_deletado = self.elementos[-1]
			del self.elementos[-1]
			self.topo -= 1
			return item_que_foi_deletado

	
	def elemento_do_topo(self):
		if self.topo == -1:
			return 'A pilha está vazia'
		else:
			return self.elementos[self.topo]


	def pilha_cheia(self):
		if self.tamanho == len(self.elementos):
			return 'A pilha está cheia'
		else:
			return 'A pilha não está cheia'

	
	def pilha_vazia(self):
		# essa parte aqui
		# if self.tamanho == -1:
		# 	return True
		# else:
		# 	return False
		
		# é igual a essa
		# return self.tamanho == -1

		return self.elementos == []

	def mostra_pilha(self):
		for i in self.elementos:
			print(i)



