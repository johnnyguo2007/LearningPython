name = input('Enter name:')
number_of_times = int(input('Enter the number of times:'))
for count in range (0,number_of_times):
	print(name)






word = input('Enter the word:')
letter_to_find = input('Enter letter in word to find:')
for letter in word:
	if letter == letter_to_find:
		print('Yay me I found it')