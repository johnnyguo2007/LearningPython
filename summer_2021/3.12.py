def length_of_digits(num):
	length = len(str(num))
	return int(length)


def get_first_digit(num):
	length = length_of_digits(num)
	denominator = 10 ** (length - 1)
	result = num // denominator
	return result


def get_last_digit(num):
	return num % 10


def chop_off_first_and_last(num):
	length = length_of_digits(num)
	denominator = int(10 ** (length - 1))
	num = num % denominator
	num = int(num) // 10
	return num



x = int(input('Enter a number:'))
same = True
while same and length_of_digits(x) > 1:
	first_num = get_first_digit(x)
	last_num = get_last_digit(x)
	if first_num == last_num:
		same = True
		x = chop_off_first_and_last(x)
	else:
		same = False

if same:
	print('it is a palindrome')
else:
	print('it is not a palindrome')
