import time, json, sys

MAX_DRINKS = 10
MAX_CUPS = 20

filename = "cooler.json"
drinks_list = []

try:
	with open(filename) as file:
		available_drinks = json.load(file)
except FileNotFoundError:
	with open (filename, 'w') as file:
		available_drinks = {}
		json.dump(available_drinks, file)
		file.close

def typewrite(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.005)

def save_drinks():
	with open(filename, 'w') as file:
		json.dump(available_drinks, file)

class Dispenser:
	def start(self):
		"""Initialize dispenser object and define attributes."""
		typewrite("Dispenser is on!\n")

		if not len(available_drinks) == 0:
			thirsty = input("Would you like a drink? (yes/no)")

			if thirsty == "y" or thirsty == "yes":
				typewrite(f"We have {len(available_drinks)} available drinks:\n\n")
				i = 1

				for soda, amount in available_drinks.items():
					drinks_list.append(soda)
					typewrite(f"{i}. {soda}: {amount} cups\n")
					i += 1
				print(drinks_list)
			else:
				sys.exit("You are not thirsty!")

			typewrite("What drink would you like? (Enter a number)\n")
			self.drink = int(input(">>> "))

			if not self.drink < 1 and not self.drink > len(available_drinks):
				available_cups = available_drinks[drinks_list[self.drink - 1]]
				self.chosen_cups = drinks_list[self.drink - 1]
				typewrite(f"You have chosen {self.chosen_cups}\n")
				typewrite("And how many cups would you like?\n(Enter a valid number)\n")
				cups = int(input(">>> "))

				if cups <= available_cups:
					self.cups = cups
				else:
					sys.exit(f"Not enough cups of {self.chosen_cups}!\nYou wanted {cups} cups but only {available_cups} cups are available.")
			else:
				sys.exit("You entered an invalid number!")
		else:
			sys.exit("Dispenser is empty!\nPlease add drinks to the cooler first.")

	def dispense_drink(self):
		"""Simulate dispenser pouring a drink."""
		# TODO Subtract dispensed cups from total amount.
		available_cups = available_drinks[self.chosen_cups] 
		available_cups -= self.cups

		typewrite(f"Pouring {self.cups} cup(s) of {self.chosen_cups}.\nEnjoy your drink!\n")
		typewrite(f"Remaining cups of {self.chosen_cups}: {available_cups}")
		
		# TODO Call save_drink to dump dict data to JSON
		save_drinks()

	def add_new_drink(self, new_drink, new_cup):
		"""Add a new drink to the dispenser cooler."""
		if not len(available_drinks) > MAX_DRINKS:
			for drink, cup in available_drinks.items():
				if drink == new_drink:
					sys.exit("New drink already in cooler!")
			
			if not new_cup > MAX_CUPS:
				available_drinks[new_drink] = new_cup

				typewrite(f"Adding {new_cup} cup(s) of {new_drink} to cooler!")
				
				# TODO Call save_drink to dump dict data to JSON
				save_drinks()
			else:
				sys.exit("You can not add more than 20 cups!")
		else:
			sys.exit("Dispenser cooler limit reached!")

	def topup_drink(self, old_drink, cups):
		"""Top up existing drinks in the dispenser cooler."""
		try:
			current_cups = [cup for drink, cup in available_drinks.items() if drink == old_drink][0]
			
			typewrite(f"Topping up {old_drink}...\n")
			typewrite(f"Current cups in cooler: {current_cups}\n")
			typewrite(f"Cups to add: {cups}\n\n")

			if available_drinks[old_drink] + cups <= MAX_CUPS:
				available_drinks[old_drink] += cups
				typewrite(f"Total cups now stands at {available_drinks[old_drink]} cups.") 
			else:
				sys.exit("Too many cups added!\nThe maximum per drink is 20 cups.")

			# TODO Call save_drink to dump dict data to JSON
			save_drinks()
		except IndexError:
			typewrite(f"Drink {old_drink} not found in cooler!\n")

soda_vending_machine = Dispenser()

# soda_vending_machine.start()

# soda_vending_machine.dispense_drink()

soda_vending_machine.add_new_drink("7UP", 13)

# soda_vending_machine.topup_drink("Fanta", 1)

