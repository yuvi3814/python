import random

random_number = random.randint(1,10)  # numbers 1 - 10

while True:
	number = input("pick your number from 1:10: ")
	number = int(number)
	
	if number < random_number: 
		print ("Guess is low")
	elif number > random_number: 
		print("Guess is high")
	else:
		print("you are correct")
		print(random_number)

		play=input("Do you want to play again Y/N:")
		if play == "y":
			random_number = random.randint(1,10)  # numbers 1 - 10
			number = None
		else:
			print("Thanks for playing")
			break
		


# handle user guesses
#   if they guess correct, tell them they won
#     otherwise tell them if they are too high or too low

# BONUS - let player play again if they want!