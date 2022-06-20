for count in range(1, 11):
	print(count)
	if count == 6:
		# ask user if they want to continue
		user_choice = input('Would you like to continue? Please enter Y or N:')
		if user_choice.upper() == 'Y':
			continue
		else:
			break

print("out of loop")
