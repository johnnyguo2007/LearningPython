
def max_num (num_1, num_2, num_3):
	if num_1 >= num_2 and num_1 >= num_3:
		return num_1
	elif num_2 >= num_1 and num_2 >= num_3:
		return num_2
	else:
		return num_3


print(max_num(7372111111, 52 , 7111))

