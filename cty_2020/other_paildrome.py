def len_of_num(num):
	length = int(len(str(x)))
	return int(length)


def get_first_digits(num):
	length = len_of_num(num)
	divider = 10 ** (length - 1)
	result = num // divider
	return result


def get_last_digit(num):
	return num % 10


def chop_off_first_and_last_digit(num):
	length = len_of_num(num)
	divider = 10 ** (length - 1)
	num = num % divider
	num = num // 10
	return num


same = True
x = int(12333)
while same and len_of_num(x) > 1:
	first_digit = get_first_digits(x)
	last_digit = get_last_digit(x)
	if first_digit == last_digit:
		same = True
		x = chop_off_first_and_last_digit(x)
	else:
		same = False


if same:
	print('it is a palindrome')
else:
	print('it is not a palindrome')
