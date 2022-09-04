'''
my number is 7

h = (43 * 15 % 17) %9
print(h)
'''
class phonebook:
	def __init__(self):
		self.items = {}
	def throwin(self, number: int, name: str):
		if name == 'not found':
			raise AssertionError('Wrong Name!!!')
		self.items[number] = name
	def delete(self, number: int):
		if self.items.get(number) != None:
			del self.items[number]
		else:
			return None
	def find(self, number: int):
		name = self.items.get(number)
		if name == None:
			return 'not found'
		else:
			return name
	def show(self):
		return self.items

with open('input.txt') as a:
	lines = a.readlines()
myphonebook = phonebook()
n = int(lines[2])
for i in range(3, n+3):
	com = lines[i].split()
	command = com[0]
	if command == 'add':
		myphonebook.throwin(int(com[1]), com[2])
	if command == 'del':
		myphonebook.delete(int(com[1]))
	if command == 'find':
		print(myphonebook.find(int(com[1])))