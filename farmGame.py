import random
import time

inventory = []
inventorysize = 10
money = 0
validActions = ["grow", "sell", "bank", "inventory"]

def grow():
	progress = 0
	waittime = random.randrange(1, 11) / 10
	states = 7

	print("Growing wheat")
	for i in range(states+1):
		time.sleep(waittime)
		progress += 1

	print("Your wheat has succesfully growed")
	collect()

def collect():
	if inventorysize <= 0:
		print("No empty slot")
		print("Crop scrapped")
	else:
		print("Crop collected")
		inventory.append("wheat")

def sell():
	if "wheat" in inventory:
		print("Your wheat has sold for $10")
		return money + 10
	else:
		print("No wheat is in your inventory")
		print("Please grow some and sell some more")

def bank():
	print("You have", "$" + str(money))


def invsee():
	if len(inventory) > 0:
		print("Your inventory contains:", str(len(inventory)) + "x wheat")
	else:
		print("Your inventory is empty")
	print("Inventory slots:", inventorysize-len(inventory))

#Main program
while True:
	print("\nValid actions:", ", ".join(validActions))
	playerAction = input(">>")

	if playerAction == "end":
		break
	elif playerAction == "grow":
		grow()
	elif playerAction == "sell":
		money = sell()
	elif playerAction == "bank":
		bank()
	elif playerAction == "inventory":
		invsee()
