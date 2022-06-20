
is_male= True
is_tall= False

if is_male and is_tall:
	print("Hi man who is tall ")
elif is_male and not is_tall:
	print("Hi, male who is short")
elif not is_male and is_tall:
	print("Hi, woman who is tall")
else:
	print("You are not tall and not male")
