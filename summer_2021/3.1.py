passes = 0


for student in range(10):
	result = int(input('Enter result(1=pass, 2=fail): '))
	while result != 1 and result != 2:
		result = int(input('Only enter result(1=pass, 2=fail): '))
	if result == 1:
		passes = passes + 1
	# elif result == 2:
	# 	failures = failures + 1
	# else:
	# 	print('Enter 1 or 2 only')


print('Passed:', passes)
print('Failed:', 10 - passes)

print('you',end='')
print('he')