from random import randrange
from graphics import * #WINNER graphic that will display when player wins


class Player(object):
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

class Slot_machine(object):
	def __init__(self):
		self.v = ['SIX!!!', 'LUCKY6', 'CHERRY', 
				  '3-BAR!', '2-BAR!', '1-BAR!']    #values
		self.multiplier = 1 
		self.wager = 0    
		self.map = [] # may be redundant


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

	def __matrix(self):
		"""creates a matrix with numbers that correspond to each value in
		the list 'v' """
		num1, num2, num3 = randrange(6), randrange(6), randrange(6)
		matrix = [[],[],[]]
		matrix[0].append(self.reel_values(num1)[0])
		matrix[0].append(self.reel_values(num2)[0])
		matrix[0].append(self.reel_values(num3)[0])
		matrix[1].append(num1)
		matrix[1].append(num2)
		matrix[1].append(num3)
		matrix[2].append(self.reel_values(num1)[1])
		matrix[2].append(self.reel_values(num2)[1])
		matrix[2].append(self.reel_values(num2)[1])
		return matrix

	def rep_matrix(self):
		""" Generates a matrix and then converts it to slot values for display""" 
		matrix = self.__matrix()
		repped = [[self.v[matrix[0][0]], self.v[matrix[0][1]], self.v[matrix[0][2]]],
				  [self.v[matrix[1][0]], self.v[matrix[1][1]], self.v[matrix[1][2]]],
				  [self.v[matrix[2][0]], self.v[matrix[2][1]], self.v[matrix[2][2]]]]
		return repped

	def package_matrix(self, matrix):
		""" Prints each row on a separate line"""
		print matrix[0]
		print matrix[1]
		print matrix[2]


	# need to get this function to recognize mixed Bars (1-bar, 2-bar,3-bar) as a valid
	# match
	def diagonal(self, matrix):
		diagonal = False
		if matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2]:
			diagonal = True
		elif matrix[0][2] == matrix[1][1] and matrix[1][1] == matrix[2][0]:
			diagonal = True

	def match(self, matrix):
		""" Checks the horizontal row for a match"""
		last_item = matrix[1][0][-4:]
		match = True
		for item in matrix[1]:
			if item[-4:] != last_item:
				match = False
			last_item = item[-4:]
		return match

	def is_bar(self):
		pass	

	def multiplier(self):	#sets the payout to 75% of full if diagonal match
		if diagonal():
			self.multiplier = 0.75
		else:
			self.multiplier = 1

	def payouts(self): #payouts should vary
		pass

	
def test():
	#create slot_machine instance
	test = Slot_machine()
	spin = test.rep_matrix()
	print spin
	#match() returns True if horizontal match, False if no match, True if 3 bars of any value
	print test.match(spin)

	print "Testing Brendan's edit"
	print "further edit 1"

	player1 = Player('Alan')
	assert player1.tokens == 0
	player1.add_tokens(100)
	assert player1.tokens == 100



#test()



