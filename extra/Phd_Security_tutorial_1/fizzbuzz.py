# FizzBuzz from (1 to 100)
# if a number is divisible by 3, print fizz
# if a numebr is divisible by 5, print buzz
# if a number is divisible by both, print fizzbuzz
import time

choice = int(input('what is your choice ?'))
def fizzbuzz(choice):
	for i in range(1,choice):
		if (i%3 == 0) and (i%5 == 0):
			print(i,"fizzbuzz")
		elif i%3 == 0:
			print(i,"fizz")
		elif i%5 == 0:
			print(i,"buzz")
		else:
			print(i)


if __name__ == '__main__':
	print("about to run program")
	time.sleep(5)
	fizzbuzz(choice)

# name = input("what is your name : ")
# def username(name):
# 	print(f"hello there {name}")
# 	print("how are you %s" %name)
#
# if __name__ == '__main__':
# 	username(name)
