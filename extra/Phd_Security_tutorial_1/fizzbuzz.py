# FizzBuzz from (1 to 100)
# if a number is divisible by 3, print fizz
# if a numebr is divisible by 5, print buzz
# if a number is divisible by both, print fizzbuzz

#
# for i in range(1,101):
# 	if (i%3 == 0) and (i%5 == 0):
# 		print(i,"fizzbuzz")
# 	if i % 3 == 0:
# 		print(i,'fizz')
# 	elif i % 5 == 0:
# 		print(i,'buzz')
# 	else:
# 		print(i)

for i in range(1,101):
	if (i%3 == 0) and (i%5 == 0):
		print(i,"fizzbuzz")
	elif i%3 == 0:
		print(i,"fizz")
	elif i%5 == 0:
		print(i,"buzz")
	else:
		print(i)