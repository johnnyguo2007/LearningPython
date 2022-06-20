print("Press 1 for burger")
print("Press 2 for ice-cream")
print("Press 3 for coffee")
print("Press any other for water")

choice = input("Enter your choice ")
itemName = "choose an item"
if choice == 1 :
	itemName = "Burger"
price = 6.60
elif choice == 2 :
itemName = "Ice-cream"
price = 5.50
elif choice == 3 :
itemName = "Coffee"
price = 2.50
else :
itemName = "Water"
price = 0.0
print("Item name: %s Price :$ %s" % (itemName, price))