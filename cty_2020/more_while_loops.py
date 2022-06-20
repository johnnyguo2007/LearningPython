stop_word = 'stop'
not_done = True
print("This game will repeat the word you say back to you until you type in 'quit'")
while not_done:
	word = input('Enter word:')
	if word == stop_word:
		print('You have won it all')
		not_done = False
	else:
		print(word)
