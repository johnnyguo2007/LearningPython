num_balloons = input('How many balloons do you need?\n')
num_balloons = int(num_balloons)
price_under_50 = 1.00
price_between_50_and_100 = 0.50
price_over_100 = 0.25
# This is representing each additional balloon
cost = 0
if num_balloons <= 50:
	cost = num_balloons * price_under_50
elif num_balloons <= 100:
	cost = 50 + (num_balloons - 50) * price_between_50_and_100
else:
	cost = 50 + 25 + (num_balloons - 100) * price_over_100

print('Your cost is:', cost)
