from decimal import Decimal
principal = Decimal('1000.00')
rate = Decimal('0.07')
for year in range(1,11):
	amount = principal * (1 + rate) ** year
	print(amount)
principal = 1000
rate = 0.07



