from slot import SlotMachine, Player
import graphics

yes = ("yesyeayeyayahyyeahyup")
no = ("nonopenahn")

def broke_test(player):
	while not player.has_balance():	
		print("Looks like your all out of tokens!")
		resume = raw_input("Would you like to keep playing? ('y','n') ")
		if resume.lower() in yes:
			try:
				player.add_tokens(int(raw_input("Enter the number of tokens you'd like to add: ")))
				print player.tokens
			except ValueError or TypeError:
				print("Sorry, it seems you didn't enter a number. ")
				player.add_tokens(int(raw_input("Enter the number of tokens you'd like to add: ")))
		elif resume.lower() in no:
			print("Hope you enjoyed the game!")
			print("\n")
			raw_input('Hit enter to quit.')
			quit(0)
		else:
			print("P")
			print("\n")
	
def main():
	print graphics.title
	raw_input("Press enter to start!")
	print("\n")
	user = Player(raw_input("What's your name, gambler? "))

	print("Hello, {}! \nTry your luck on the Lucky-6 slot machine!".format(user.name))
	print("\n")
	slot = SlotMachine()
	user.add_tokens(6)
	while user.has_balance():
		slot.place_bet(user)
		slot.create_matrix_values()
		slot.diagonal_check(slot.matrix)
		slot.horizontal_check(slot.matrix)
		slot.rep_matrix()
		slot.payouts(user)
		#slot.matrix = [[],[],[]]
		print("Your current balance is {}.".format(user.tokens))
	else:
		broke_test(user)



		

if __name__ == '__main__': 
	main()

