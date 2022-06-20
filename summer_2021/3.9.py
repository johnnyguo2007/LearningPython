#number = int(input('enter a 5-dight integer; '))
number = 73849
result = number
for i in range(1, 6):
	dem = 10 ** (5-i)
	#result = number % 10
	result = number // dem
	number = number % dem
	#print('This is loop number ', i, 'number now is ', number, 'result is ', result)
	print(result, end=' ')

# dight5 = number % 10
# number = int(number/10)