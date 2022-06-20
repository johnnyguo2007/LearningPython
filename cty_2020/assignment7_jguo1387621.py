# | 5space 10 star 6space 10 star 5space |
def print_solid_window_line():
	print("|", " " * 5, "*" * 10, " " * 6, "*" * 10, " " * 5, "|")


# | 5space 1 star 8space 1 star 6 space 1 star 8space 1 star 5space |
def print_side_window_line():
	print("|", " " * 5, "*", " " * 6, "*", " " * 6, "*", " " * 6, "*", " " * 5, "|")


# print solid line
# print side line 5X
# print solid line
def print_window():
	print_solid_window_line()
	for line_number in range(1, 6):
		print_side_window_line()
	print_solid_window_line()


def print_bottem_window_line():
	print("| ", "-" * 38, " |")


def print_one_floor():
	print_window()
	print_bottem_window_line()


def print_foundation_lines():
	for a_line in range(1, 3):
		print("^" * 44)


def print_ceiling_line():
	print("|" * 44)


# # user tells me the number of floors n.
# # Then print ceiling line.
# # Loop n times, each time print a floor.
# # print foundation lines

num_floors = int(input('How many floors?'))
print_ceiling_line()
for floor_number in range(1, num_floors + 1):
	print_one_floor()

print_foundation_lines()
# for a_floor in range(1,4):
# 	print_one_floor()
#
# print_foundation_lines()


# print_window()
# print_bottem_window_line()
# print_solid_window_line()
# print_side_window_line()


# generate 10 random numbers
# then print
#
import random
even_total = 0
odd_total = 0
for random_num in range(1, 11):
	one_random_result = random.randint(1,25)
	print(one_random_result)

	if one_random_result % 2 == 0:
		# add the even numbers
		even_total = even_total + one_random_result
	else:
		odd_total = odd_total + one_random_result
	print('Even total is %s and odd total is %s' % (even_total, odd_total))

print('final even total is %s and final odd total is %s' % (even_total, odd_total))
