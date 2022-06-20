def popluation_density(population, area):
	return population / area


def print_state_name_density(state_name, population_density):
	print('state name is %s and population density is %s (million/square mile)' % (state_name, population_density))


print_state_name_density('Maryland', popluation_density(6.052, 12407))
print_state_name_density('Pennsylvania', popluation_density(12.81, 46055))
print_state_name_density('Virginia', popluation_density(8.4, 42775))


def motel_cost(motel_cost_per_night, total_travel_distance, travel_distance_per_day):
	# int function to remove the decimal and floor the float to integer.
	return motel_cost_per_night * int(total_travel_distance / travel_distance_per_day)


def travel_distance_per_day(total_hours_per_day_driving_time, average_miles_per_hour_speed):
	return (total_hours_per_day_driving_time * average_miles_per_hour_speed)


def gas_cost(total_travel_distance, car_miles_per_gallon, gas_price_per_gallon):
	return gas_price_per_gallon * total_travel_distance / car_miles_per_gallon


def total_cost(motel_cost, gas_cost):
	return motel_cost + gas_cost


print('enter total travel distance:')
my_total_travel_distance = float(input(''))
print('enter total hours per day driving time:')
my_total_hours_per_day_driving_time = float(input(''))
print('enter average miles per hour:')
my_average_miles_per_hour_speed = float(input(''))
print('enter average miles per gallon for your car:')
my_average_miles_per_gallon_for_your_car = float(input(''))
print('enter average gas price per gallon:')
my_average_gas_price_per_gallon = float(input(''))
print('motel cost per night:')
my_motel_cost_per_night = float(input(''))

my_travel_distance_per_day = int(
	travel_distance_per_day(my_total_hours_per_day_driving_time, my_average_miles_per_hour_speed))
print('my_travel_distance_per_day is: ', my_travel_distance_per_day)

my_motel_cost = motel_cost(my_motel_cost_per_night, my_total_travel_distance, my_travel_distance_per_day)
print('my_motel_cost is: ', my_motel_cost)

my_gas_cost = int(
	gas_cost(my_total_travel_distance, my_average_miles_per_gallon_for_your_car, my_average_gas_price_per_gallon))
print('my_gas_cost_is: ', my_gas_cost)

my_total_cost = total_cost(my_motel_cost, my_gas_cost)
print('my_total_cost: ', my_total_cost)

# print('total travel distance is: ' , total_travel_distance)
# print('total_hours_per_day_driving_time' , total_hours_per_day_driving_time)
# print('average_miles_per_gallon_for_your_car' , average_gas_price_per_gallon)
# print()
