# Find the length of the digits
# Get the first digit
# Get the last digit
# cut off last two digits to create a new number

same = True
while same and length_of_digits(x) > 1:
	first_num = get_first_dight(x)
	last_num = get_last_dight(x)
	if first_num == last_num:
		same = True
		x = chop_off_first_and_last(x)
	else:
		same = False

if same:
	print('it is a palindrome')
else:
	print('it is not a palindrome')