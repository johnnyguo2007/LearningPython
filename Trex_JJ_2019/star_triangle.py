
height = 8
for row_number in range(height):
	for col_number in range(row_number):
		if (col_number == 0 or col_number == row_number - 1 or row_number == height - 1):
			print("*", end='')
		else:
			print(" ", end='')
	print("\n")









