#
# my_sum = 0
# for item in range(3, 46, 4):
# 	my_sum += item
#
# print( my_sum)
my_sum = 0
start = 3
step = 4
for loop_num in range(11):
	item = start + step * loop_num
	print(item)
	my_sum += item


print("my total is", my_sum)
