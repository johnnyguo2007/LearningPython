number = int(input('enter your number between 1 and 10:'))
your_guess = True
while your_guess:
	guess = int(input('Enter the guess:'))
	if guess == number:
		your_guess = False
		print("you have guess it! The number was %s" % number)