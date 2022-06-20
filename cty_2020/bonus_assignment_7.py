def even_win():
	# generate 10 random numbers
	# then print
	#
	import random
	even_total = 0
	odd_total = 0
	for random_num in range(1, 11):
		one_random_result = random.randint(1, 2)
		# print(one_random_result)

		if one_random_result % 2 == 0:
			# add the even numbers
			even_total = even_total + one_random_result
		else:
			odd_total = odd_total + one_random_result
	# 	print('Even total is %s and odd total is %s' % (even_total, odd_total))
	#
	# print('final even total is %s and final odd total is %s' % (even_total, odd_total))

	if even_total >= odd_total:
		return True
	else:
		return False


#make a loop to run this function 4000 times
num_of_even_win = 0
num_of_total_runs = 4000000
for i in range(1,num_of_total_runs + 1 ):
	if even_win():
		num_of_even_win = num_of_even_win + 1

print('percentage of even win is ', num_of_even_win / num_of_total_runs * 100, "%")
