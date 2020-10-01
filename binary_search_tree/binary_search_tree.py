class Node(object):
	def __init__(self, data):
		self.data = data
		self.left_child = None
		self.right_child = None


class BinarySearchTree(object):
	def __init__(self):
		self.root = None

	def insert(self, data):
		if not self.root:
			self.root = Node(data)
		else:
			self.insert_node(data, self.root)


	# O(logN complexity) If de tree is balanced --> It can reduced to O(N) --> AVL RBT are needed
	def insert_node(self, data, node):
		if data < node.data:
			if node.left_child:
				self.insert_node(data, node.left_child)
			else:
				node.left_child = Node(data)
		else:
			if node.right_child:
				self.insert_node(data, node.right_child)
			else:
				node.right_child = Node(data)


	def remove(self, data):
		if self.root:
			self.root = self.remove_node(data, self.root)


	def remove_node(self, data, node):
		if not node:
			return node

		if data < node.data:
			node.left_child = self.remove_node(data, node.left_child)
		elif data > node.data:
			node.right_child = self.remove_node(data, node.right_child)
		else:

			# First situation: when a node is a leaf node
			if not node.left_child and not node.right_child:
				print('removing a leaf node')
				del node
				return None

			# Second situation: when a node have just one child
			if not node.left_child:
				print('Removing a node with a sigle right child')
				temporary_node = node.right_child
				del node
				return temporary_node
			elif not node.right_child:
				print('Removing a node with single left child')
				temporary_node = node.left_child
				del node
				return temporary_node

			# third situation: when a node have two children
			print('Removing node with two children')
			temporary_node = self.get_predecessor(node.left_child)
			node.data = temporary_node.data
			node.left_child = self.remove_node(temporary_node.data, node.left_child)

		return node


	def get_predecessor(self, node):
		if node.right_child:
			return self.get_predecessor(node.right_child)
		return node


	def get_min_value(self):
		if self.root:
			return self.get_min(self.root)


	def get_min(self, node):
		if node.left_child:
			return self.get_min(node.left_child)
		return node.data


	def get_max_value(self):
		if self.root:
			return self.get_max(self.root)


	def get_max(self, node):
		if node.right_child:
			return self.get_max(node.right_child)
		return node.data


	def traverse(self):
		if self.root:
			self.traverse_in_order(self.root)


	def traverse_in_order(self, node):
		if node.left_child:
			self.traverse_in_order(node.left_child)

		print(node.data, end=' ')

		if node.right_child:
			self.traverse_in_order(node.right_child)

		# print(node.data, end=' ')