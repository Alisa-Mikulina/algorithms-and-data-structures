class election:
	def __init__(self):
		self.items = {}
	def add(self, name, votes):
		current = 0
		if str(name) in self.items:
			current = self.items.get(str(name))
		self.items[str(name)] = int(votes)+current
	def print(self):
		answer = ''
		#return self.items
		for i in sorted(list(self.items.keys())):
			answer += f"{i} {self.items[i]} \n"
		return answer

with open('input.txt') as a:
	lines = a.readlines()
elections = election()
n = int(lines[18])
for i in range(n):
	name, votes = lines[i+19].split()
	elections.add(name, votes)

print(elections.print())