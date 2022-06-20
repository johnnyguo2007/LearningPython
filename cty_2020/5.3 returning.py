def popluation_density(population, area):
	return population / area

def print_state_name_density (state_name, population_density):
	print('state name is %s and population density is %s (million/square mile)' % (state_name, population_density))

print_state_name_density('Maryland', popluation_density(6.052, 12407))
print_state_name_density('Pennsylvania', popluation_density(12.81, 46055))
print_state_name_density('Virginia', popluation_density(8.4, 42775))


# motel_cost = motel_cost_per_night * total_nights
# total_nights = total_travel_distance/average_milies_per_hour_speed
# motel_cost = motel_cost_per_night * total_travel_distance/average_milies_per_hour_speed
