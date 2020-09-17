class Trie:

	def __init__(self):
		self.children = {}
		self.isEndOfWord = False

	# add nodes in the trie 
	def insert(self, key):
		length = len(key)
		for level in range(length):
			if not key[level] in self.children:
				self.children[key[level]] = Trie()
			self = self.children[key[level]]

		self.isEndOfWord = True

	# search function to search a particular word
	def search(self, key):
		
		if self.isEndOfWord and len(key) == 0:
			return True
		length = len(key)
		for level in range(length):
			if not key[level] in self.children:
				return False
			self = self.children[key[level]]
		return True

	# this function traverses the graph from a particular point
	def travel(self, key):
		if self.isEndOfWord:
			print(key)
		for new in self.children:
			string_append = key + new
			self.children[new].travel(string_append)

	# checks whether the partial string is correct or not
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

	# suggest the words
	def suggest(self, key):
		 new_string = ''
		 length = len(key)
		 for level in range(length):
		 	if key[level] in self.children:
		 		new_string += key[level]
		 		self = self.children[key[level]]
		 	else:
		 		break
		 self.travel(new_string)
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

# print(t.suggest('ax'))
