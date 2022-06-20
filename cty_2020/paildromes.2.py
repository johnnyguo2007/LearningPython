def length_of_number(num):
	length = int(len(str(num)))
	return int(length)


def get_first_digit(num):
	length = length_of_number(num)
	divider = 10 ** (length - 1)
	result = num // divider
	return result


def get_last_digit(num):
	return num % 10


def chop_off_first_and_last_num(num):
	length = length_of_number(num)
	divider = 10 ** (length - 1)
	num = num % divider
	num = num // 10
	return num


###########################
same = True
x = int(12329)
while same and length_of_number(x) > 1:
	first_digit = get_first_digit(x)
	last_digit = get_last_digit(x)
	if first_digit == last_digit:
		same = True
		x = chop_off_first_and_last_num(x)
	else:
		same = False


if same:
	print('it is a palindrome')
else:
	print('it is not a palindrome')