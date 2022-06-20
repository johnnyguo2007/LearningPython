


def factorial(input_num):
	result = 1
	if input_num != 0 and input_num != 1:
		for n in range(1, input_num + 1):
			result = result * n

	return result


my_input = int(input('Please enter a nonnegative integer:'))
my_result = factorial(my_input)
print('The factorial of', my_input, 'is', factorial(my_input))
