class Trie:

	def __init__(self):
		self.children = {}
		self.isEndOfWord = False

	def insert(self, key):
		length = len(key)
		for level in range(length):
			if not key[level] in self.children:
				self.children[key[level]] = Trie()
			self = self.children[key[level]]

		self.isEndOfWord = True

	def search(self, key):
		
		if self.isEndOfWord and len(key) == 0:
			return True
		length = len(key)
		for level in range(length):
			if not key[level] in self.children:
				return False
			self = self.children[key[level]]
		return True


	def travel(self, key):
		if self.isEndOfWord:
			print(key)
		for new in self.children:
			string_append = key + new
			self.children[new].travel(string_append)

	def auto(self, key):
		make_string = ''
		length = len(key)
		for level in range(length):
			make_string += key[level]
			if key[level] in self.children:
				self = self.children[key[level]]
			else:
				return 'No keyword found'
		self.travel(make_string)
		return 'Completed'


# list = ['age',
# 	'agee',
# 	'agree',
# 	'bowl',
# 	'ball',
# 	'bat',
# 	'bark',
# 	'ba',
# 	'bench',
# 	'bet',
# 	'bery',
# 	'blink',
# 	'blie',]

# t = Trie()
# for words in list:
# 	t.insert(words)

# print(t.search('aaa'))
