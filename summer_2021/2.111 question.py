number = int(input('enter a 5-dight integer; '))
dight5 = number % 10
number = int(number/10)
dight4 = number % 10
number = int(number/10)
dight3 = number % 10
number = int(number/10)
dight2 = number % 10
number = int(number/10)
dight1 = number % 10
number = int(number/10)
print(dight1, '   ',dight2, '   ',dight3, '   ',dight4, '   ', dight5, '   ')