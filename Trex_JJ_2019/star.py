
rows = 8
for row_num in range(rows):
	for col_num in range(row_num + 1):
		if col_num == 0 or col_num == row_num or row_num == rows - 1:
			print("*", end='')
		else:
			print(" ", end='')

	print("\n")







