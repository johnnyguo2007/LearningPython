def length_of_number(num):
	length = len(int(num))
	return length


def get_first_digit(num):
	length = length_of_number(num)
	divider = 10 ** (length - 1)
	result = num // divider
	return result


def get_last_digit(num):
	return num % 10


def chop_off_first_and_last_digit(num):
	length = length_of_number(num)
	divider = 10 ** (length - 1)
	num = num % divider
	divider = num // 10
	return num
same = True
while same and length_of_number > 1:
	first_num = get_first_digit(x)
	last_num = get_last_digit(x)
	if first_num == last_num:
		same = True
		x = chop_off_first_and_last_digit(x)
	else:
		same = False
