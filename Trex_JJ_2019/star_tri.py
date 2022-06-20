
height = 10
for row_number in range(height):
	for col_num in range(row_number):
		if col_num == 0 or col_num == row_number - 1 or row_number == height - 1:
			print("*", end='')
		else:
			print(" ", end='')

	print("\n")








