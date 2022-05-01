class Node:

	def __init__(self,value):
		self.parent = value
		self.lchild = None
		self.rchild = None

	def insert(self, value):
		if self.parent:

			if value < self.parent:
				if self.lchild is None:
					self.lchild = Node(value)
				else:
					self.lchild.insert(value)

			else:
				if self.rchild is None:
					self.rchild = Node(value)
				else:
					self.rchild.insert(value)

		else:
			self.parent = value

	def printtree(self):
		if self.lchild:
			self.lchild.printtree()
		print(self.parent)
		if self.rchild:
			self.rchild.printtree()


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.printtree()

