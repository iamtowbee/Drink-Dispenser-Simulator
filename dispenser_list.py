import sys
import time

MAX_DRINKS = 10
MAX_CUPS = 20

available_drink_cups = [["Coke", 5], ["Fanta", 5],["Pepsi", 5],["7UP", 5],["Smoov", 5],["Coke", 5], ["Fanta", 5],["Pepsi", 5],["Sprite", 5],["Smoov", 5]]

def typewrite(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.04)

class Dispenser:
	def start(self):
		"""Initialize dispenser object and attributes."""
		typewrite("Dispenser is on!\n")
		thirsty = input("Would you like a drink? (y/n)")

		if thirsty == "y":
			typewrite(f"We have {len(available_drink_cups)} available drinks:\n\n")
			i = 1

			for soda in available_drink_cups:
				typewrite(f"{i}. {soda[0]}: {soda[1]} cups\n")
				i += 1
		else:
			sys.exit("You are not thirsty!")

		typewrite("What drink would you like? (Enter a number)\n")
		self.drink = int(input(">>> "))

		if not self.drink < 1 and not self.drink > len(available_drink_cups):
			typewrite(f"You have chosen {available_drink_cups[self.drink - 1][0]}\n")
			typewrite("And how many cups would you like?\n(Enter a valid number)\n")
			cups = int(input(">>> "))

			if cups <= available_drink_cups[self.drink - 1][1]:
				self.cups = cups
			else:
				sys.exit(f"Not enough cups of {available_drink_cups[self.drink - 1][0]}\nYou wanted {cups} cups but only {available_drink_cups[self.drink - 1][1]} cups are available.")
		else:
			sys.exit("You entered an invalid number!")

	def dispense_drink(self):
		"""Simulate dispenser pouring a drink."""
		typewrite(f"Pouring {self.cups} cups of {available_drink_cups[self.drink - 1][0]}.\nEnjoy your drink!")

	def add_new_drink(self, new_drink, new_cup):
		"""Add a new drink to the dispenser cooler."""
		if not len(available_drink_cups) > MAX_DRINKS:
			for drink, cup in available_drink_cups:
				if drink == new_drink:
					sys.exit("New drink in cooler!")
			
			if not new_cup > MAX_CUPS:
				available_drink_cups.append([new_drink.title(), new_cup])
			else:
				sys.exit("You can not add more than 20 cups!")
		else:
			sys.exit("Dispenser cooler limit reached!")

	def topup_drink(self, old_drink, cups):
		"""Top up existing drinks in the dispenser cooler."""
		# current_cups = [cup for [drink, cup] in available_drink_cups if drink == new_drink][0]
		# print(f"Current cups of {new_drink}: {current_cups}")
		try:
			current_cups = [cup for drink, cup in available_drink_cups.items() if drink == old_drink][0]
			
			typewrite(f"Topping up {old_drink}...\n")
			typewrite(f"Current cups in cooler: {current_cups}\n")
			typewrite(f"Cups to add: {cups}\n\n")

			if available_drink_cups[old_drink] + cups <= MAX_CUPS:
				available_drink_cups[old_drink] += cups
				typewrite(f"Total cups now stands at {available_drink_cups[old_drink]} cups.") 
			else:
				sys.exit("Too many cups added!\nThe maximum per drink is 20 cups.")

		except IndexError:
			typewrite(f"Drink {old_drink} not found in cooler!\n")

soda_vending_machine = Dispenser()

soda_vending_machine.start()

soda_vending_machine.dispense_drink()

# soda_vending_machine.add_new_drink("Monster", 10)