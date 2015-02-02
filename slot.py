from random import randrange
from graphics import * #WINNER graphic that will display when player wins


class Player:
	def __init__(self, name):
		self.name = name
		self.tokens = 0
		self.luck = 0

	def add_tokens(self, numtokens):
		self.tokens += numtokens

	def has_balance(self):
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
		self.values = [(0, 'SIX!!!'), (1, 'LUCKY6'), (2, 'CHERRY'), 
					   (3, '3-BAR!'), (4, '2-BAR!'), (5, '1-BAR!')]
		self.multiplier = 1 
		self.wager = 0    
		self.map = []


	def valid_bet(self, wagerSize):
		if wagerSize < 0 or wagerSize > 3:
			return False
		else:
			return True
	
	def reel_values(self, value):
		"""Based on the value on display in the middle, calculates the values
		above and below on the reel"""
		upper = 0
		lower = 0
		if value == 0:
			upper, lower = 5, 1
		elif value == 5:
			upper, lower = 4, 0
		else:
			upper, lower = value - 1, value + 1
		return upper, lower



	def matrix(self):
		num1, num2, num3 = randrange(6), randrange(6), randrange(6)
		display = [[],[],[]]
		for item in display:
			if item == display[0]:
				display[0].append(self.reel_values(num1)[0])
				display[0].append(self.reel_values(num2)[0])
				display[0].append(self.reel_values(num3)[0])
			elif item == display[1]:
				display[1].append(num1)
				display[1].append(num2)
				display[1].append(num3)
			elif item == display[2]:
				display[2].append(self.reel_values(num1)[1])
				display[2].append(self.reel_values(num2)[1])
				display[2].append(self.reel_values(num2)[1])
		self.map = display

	def rep_matrix(self, matrix):
		
		reppped = [[],[],[]]


	def diagonal(self):	#checks to see if values match diagonally
		pass

	def multiplier(self):	#sets the payout to 75% of full if diagonal match
		if self.diagonal:
			self.multiplier = 0.75

	def payouts(self): #payouts should vary
		pass




	

def test():
	test = Slot_machine()
	print test.map
	test.matrix()
	print test.map

	print "**Create player instance, print amt of tokens(0): "
	player1 = Player('Alan')
	print player1.tokens, "\n"

	print "**add_tokens(10), print player tokens(10): "
	player1.add_tokens(10)
	print player1.tokens, "\n"

	#print dir(player1)

#test()



