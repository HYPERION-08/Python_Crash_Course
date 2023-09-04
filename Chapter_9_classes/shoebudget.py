class Shoes:
	def __init__(self,name,price):
		self.name = name
		self.price = float(price)

	def budget_check(self,buget):
		if not isinstance(budget,(int,float)):
			print('Invalid entry. Please enter a number')
			exit()

	"""check if the budget is int and float or not"""



	def change(self,budget):
		return (budget - self.price)

	
	def buy(self,budget):

		if budget >= self.price:
			print(f'You can cop some {self.name}')
			if budget == self.price:
				print(f'You have exactly enough money for these shoes')
			else:
				print(f'You can buy these shoes and have ${self.change(budget)} left over')
			exit('Thanks for using this app')



from shoebudget import Shoes
low = Shoes('And 1s',30)
medium = Shoes('Air Force 1s',120)
high = Shoes('Off Whites',400)

try:
	shoe_budget = float(input('What is your budget? '))
except ValueError:
	exit('Pleas enter a number')

for shoes in [high,medium,low]:
	shoes.buy(shoe_budget)