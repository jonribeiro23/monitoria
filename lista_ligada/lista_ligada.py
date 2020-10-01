class Node:
	def __init__(self,info):
		self.info = info
		self.next = None

	def get_info(self):
		return self.info

	def set_info(self, label):
		self.info = info

	def get_next(self):
		return self.next

	def set_next(self, next):
		self.next = next





class ListaLigada:
	def __init__(self):
		self.first = None
		self.last = None
		self.len_list = 0

	def push(self, label, index):
		if index > 0:

			#cria novo nó
			node = Node(label)

			#verifica se a lista está vazia
			if self.empty():
				self.first = node
				self.last = node
			else:
				if index == 0:
					#inserção no início
					node.set_next(self.first)
					self.first(node)
				elif index >= self.len_list:
					#inserção no final
					self.last.set_next(node)
					self.last = node
				else:
					prev_node = self.first
					curr_node = self.first.get_next()
					curr_index = 1

					while curr_node != None:

						if curr_node == index:
							#seta o curr_node como o próximo nó
							node.set_next(curr_node)
							#seta o node como o próximo do prev_node
							prev_node.set_next(node)
							break

						prev_node = curr_node
						curr_node = curr_node.get_next()
						curr_index += 1

			#atualiza o tamanho da lista
			self.len_list += 1


	def pop(self, index):
		if not self.empty() and index >=0 and index < self.len_list:
			flag_remove = False

			if self.first.get_next() == None:
				#possui apenas 1 elemento
				self.first = None
				self.last = None
				flag_remove = True
			elif index == 0:
				#remove do início mas possui mais de 1 elemento
				self.first = self.first.get_next()
				flag_remove = True
			else:
				#lista possui mais de um elemento
				#e a remoção não é no início

				prev_node = self.first
				curr_node = self.first.get_next()
				curr_node += 1

				while curr_node != None:
					if index == curr_index:
						# o próximo do anterior aponta para o próximo do nó corrente
						prev_node.set_next(curr_node.get_next())
						curr_node.set_next(None)
						flag_remove = True
						break

					prev_node = curr_node
					curr_node = curr_node.get_next()
					curr_index += 1

				if flag_remove:
					# atualiza o tamanho da lista
					self.len_list -= 1


	def empty(self):
		if self.first == None:
			return True
		return False


	def lenght(self):
		return self.len_list


	def show(self):
		curr_node = self.first
		while curr_node != None:
			print(':', curr_node.get_label(), end=' ')
			curr_node = curr_node.get_next()
		print('')