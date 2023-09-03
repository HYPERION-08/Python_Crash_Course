class Dog:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def sit(self):
		print(f'{self.name} is now sitting')
	def roll(self):
		print(f'{self.name} has rolled over')

""" making instances """
dog = Dog('Willie',6)
dog2 = Dog('Lucy',3)



print(f'My dogs name is {dog.name}')
print(f'His age is {dog.age}')

print(f'Your dogs name is {dog2.name}')
print(f'His age is {dog2.age}')

""" calling the methods """
dog.sit()
dog.roll()

dog2.sit()
dog2.roll()