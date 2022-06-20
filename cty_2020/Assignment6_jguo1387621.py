# Part A
guest_count = input('How many guest are there today?\n')
guest_count = int(guest_count)
num_nights = int(input('How many nights are you staying?\n'))
rate_single = 50.0
rate_double = 75.0
rate_deluxe = 200.0
rate_penthouse = 300.0
cost = 0
if guest_count == 1:
	print('You can have a single occupancy room\n')
	cost = rate_single * num_nights
elif guest_count == 2:
	print('You can have a double occupancy room\n')
	cost = rate_double * num_nights
else:
	choice = input('Would you like a deluxe suite? Please enter Y or N\n')
	if choice == 'Y':
		cost = rate_deluxe * num_nights
	else:
		print('You are choosing a penthouse suite now')
		cost = rate_penthouse * num_nights

print('Your cost is:', cost)

# Part B
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
