while(True):
	number = int(input('Enter a number (0 to exit):'))
	if number == 0:
		break
	else:
		for count in range (1, number + 1):
			print(count)

print("I am still alive")