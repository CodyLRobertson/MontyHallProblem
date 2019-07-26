#Here we go boys
#Game Rules are as follows:
#The host must always open a door that was not picked by the contestant
#The host must always open a door to reveal a goat and never the car
#The host must always offer the chance to switch between the originally chosen door and the remaining closed door.





import random

def Main():
	#Need to implement a way to randomly generate door prize so host can avert to non value prize.
	
	doorOptions = ["a","b","c"]
	playerChoice = input("Please pick a door; A, B, or C".lower()) 
	if playerChoice	== "a":
		hostChoice = random.randint(1,2)
		if hostChoice == 1:
			hostChoice = 'b'
		else:
			hostChoice = 'c'
		print("Dev: Player Chose 'a', Host chose:" + hostChoice	)

	elif playerChoice == "b":
		hostChoice = random.randint(1,2)
		if hostChoice == 1:
			hostChoice = 'a'
		else:
			hostChoice = 'c'
		print("Dev: Player Chose 'b', Host chose:" + hostChoice	)

	else:
		hostChoice = random.randint(1,2)
		if hostChoice == 1:
			hostChoice = 'a'
		else:
			hostChoice = 'b'
		print("Dev: Player Chose 'c', Host chose:" + hostChoice	)


main()
















'''
def hostChoiceFunc():
		hostChoice = random.randint(1,3)
		if hostChoice	== 1:
			hostChoice = "a"
		elif hostChoice	== 2:
			hostChoice	= "b"
		else:
			hostChoice	= "c"
		print(hostChoice)
def userChoiceA():
		print("You picked Door A.")

def userChoiceB():
		print("You picked Door B.")

def userChoiceC():
		print("You picked Door C.")

def playerChoiceFunc():
	doorOptions = ["a","b","c"]
	playerChoice = input("Please pick a door; A, B, or C".lower()) #Is this a local or global scope?
	if playerChoice	== "a":
		userChoiceA()
	elif playerChoice == "b":
		userChoiceB()
	else:
		userChoiceC()



hostChoiceFunc()
playerChoiceFunc()
'''