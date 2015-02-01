from random import randrange
from graphics import * #WINNER graphic that will display when player wins


class Player:
	def __init__(self, name):
		self.name = name
		self.tokens = 0
		self.luck = 0

	def add_tokens(self, numtokens):
		self.tokens += numtokens

	def has_balance(self, self.tokens):
		if self.tokens == 0:
			return False
		else:
			return True

	def add_luck(self):			#not sure if going to keep this
		self.luck +=1

#slot machine will be based on 'lucky-7' 3-reel slot
# with the values in each reel consisting of:
# In order of value (and order on the reel?):
# -So if row 1, column 1 value == SIX!!!, row2, column 1 value ==  LUCKY6

# 	SIX!!!
# 	LUCKY6
# 	CHERRY
# 	3-BAR!
# 	2-BAR!
# 	1-BAR!

#probabilities (maybe?) and payout structures for matching rows:
#
# SIX!!!= 1500x
# LUCKY6 = 250x
# CHERRY = 150x
# 3-BAR! = 100x
# 2-BAR! = 50x
# 1-BAR! = 20x
# Mixed bars= 3x

# 1x payout for horizontal match
# .75x payout for diagonal match

#readout will look like:
#	[[CHERRY,3-BAR!,3-BAR!],
#	 [3-BAR!, 2-BAR!, 2-BAR!],
#	 [2-BAR!,1-BAR!,1-BAR!]]

class Slot_machine:
	def __init__(self):
		self.values = ["SIX!!!", "LUCKY6", "CHERRY", "3-BAR!","2-BAR!","1-BAR!"]
		self.multiplier = 1 
		self.wager = 0    

		#wheel spins vertically:

	def valid_bet(self, wagerSize):
		if wagerSize < 0 or wagerSize > 3:
			return False
		else:
			return True
			
	def spin(self):
		print "You can bet up to 3 tokens per spin: "
		self.wager = raw_input("Please enter your bet: ")
		if self.valid_bet(self.wager):
			#spin

		pass

	def diagonal(self):	#checks to see if values match diagonally
		pass

	def multiplier(self):	#sets the payout to 75% of full if diagonal match
		if self.diagonal:
			self.multiplier = 0.75

	def payouts(self): #payouts should vary
		pass


		

	

def test():

	assert display[0][0] != [1][0]
	assert display [0][1] != [1][1]

	print "**Create player instance, print amt of tokens(0): "
	player1 = Player('Alan')
	print player1.tokens, "\n"

	print "**add_tokens(10), print player tokens(10): "
	player1.add_tokens(10)
	print player1.tokens, "\n"

	print dir(player1)

#test()



