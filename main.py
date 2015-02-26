from slot import SlotMachine, Player
import graphics

yes = ("yesyeayeyayahyyeahyup")
no = ("nonopenahn")

print graphics.title
raw_input("Press enter to start!")
print("\n")
slot = SlotMachine()
user = Player(raw_input("What's your name, gambler? "))
print("\n")
user.add_tokens(3)


def rebuy(player):
	while not player.has_balance():	
		resume = raw_input("Would you like to keep playing? ('y','n') ")
		if resume.lower() in yes:
			try:
				player.add_tokens(int(raw_input("Enter the number of tokens you'd like to add: ")))
				if player.has_balance():
					main()
			except ValueError or TypeError:
				print("Sorry, it seems you didn't enter a number. ")
				rebuy(player)
		elif resume.lower() in no:
			print("\n")
			raw_input('THANKS FOR PLAYING! HIT ENTER TO QUIT.')
			quit(0)
		else:
			main()
	
def main():
	raw_input("***** PRESS ENTER TO CONTINUE *****")
	print("\n")
	print("Hello, {}! Ready to try your luck on the Lucky-6 slot machine?".format(user.name))
	print("\n")
	raw_input("***** PRESS ENTER TO CONTINUE *****")
	print("\n")
	print("Your current balance is {}.".format(user.tokens))
	while user.has_balance():
		slot.place_bet(user)
		print("\n")
		raw_input("***** PRESS ENTER TO SPIN!! *****")
		print("\n")
		slot.represent_matrix()
		slot.diagonal_check(slot.matrix)
		slot.horizontal_check(slot.matrix)
		print("\n")
		slot.payouts(user)
		print("Your current balance is {}.".format(user.tokens))
	else:
		print("Looks like your all out of tokens!")
		rebuy(user)



		

if __name__ == '__main__': 
	main()



