import random
heads = 0
tails = 0
head_total = 0
toss_count = 2000000
for coin_toss in range(toss_count):
	toss_result = random.randrange(0,2)
	if toss_result == 1:
		print('head')
	else:
		print('tail')
	head_total += toss_result
print(head_total/toss_count)

	#print(random.randrange(1,21),end= ' ' )


