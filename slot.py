from random import randrange
from graphics import *  # WINNER graphic that will display when player wins


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


# slot machine will be based on 'lucky-7' 3-reel slot
# with the values in each reel consisting of:
# In order of value (and order on the reel?):
# -So if row 1, column 1 value == SIX!!!, row2, column 1 value ==  LUCKY6

# SIX!!!
# LUCKY6
# CHERRY
# 	3-BAR!
# 	2-BAR!
# 	1-BAR!

# probabilities (maybe?) and payout structures for matching rows:
#
# SIX!!!= 1500x
# LUCKY6 = 250x
# CHERRY = 150x
# 3-BAR! = 100x
# 2-BAR! = 50x
# 1-BAR! = 20x
# Mixed bars= 3x
# 2 Bars, and some other value = 2x

# 1x payout for horizontal match
# .75x payout for diagonal match

#readout will look like:
#	[[CHERRY,3-BAR!,3-BAR!],
#	 [3-BAR!, 2-BAR!, 2-BAR!],
#	 [2-BAR!,1-BAR!,1-BAR!]]

class Slot_machine(object):
    def __init__(self):
        self.v = ['SIX!!!', 'LUCKY6', 'CHERRY', '3-BAR!', '2-BAR!', '1-BAR!']  # values
        self.multiplier = 1
        self.wager = 0
        self.map = []  # may be redundant
        self.diagonal_winning_value = 'No diagonal match!'
        self.horizontal_winning_value = 'No horizontal match!'
        self.matrix = []  # may be redundant

    def valid_bet(self, wagerSize):
        """ Checks that player bet is 3 or less """
        if wagerSize < 0 or wagerSize > 3:
            return False
        else:
            return True

    def reel_values(self, value):
        """Based on the value on display in the middle, calculates the values above and below on the reel"""

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
        """creates a matrix with numbers that correspond to each value in the list 'v' """
        num1, num2, num3 = randrange(6), randrange(6), randrange(6)
        matrix = [[], [], []]
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
        self.package_matrix(repped)
        return matrix, repped

    def package_matrix(self, matrix):
        """ Prints each row on a separate line"""
        print matrix[0]
        print matrix[1]
        print matrix[2]

    def diagonal(self, matrix):
        """Check if there is a match along the diagonals of the matrix and returns the winning value eg. SIX!!!, LUCKY6
        or just BAR for any combination of 3-BAR, 2-BAR or 1-BAR"""

        # Assign matrix elements to variables to make it easier to view

        _00, _01, _02 = matrix[0][0], matrix[0][1], matrix[0][2]
        _10, _11, _12 = matrix[1][0], matrix[1][1], matrix[1][2]
        _20, _21, _22 = matrix[2][0], matrix[2][1], matrix[2][2]

        if _00 == _11 and _11 == _22:
            self.diagonal_winning_value = self.v[_00]

        elif _02 == _11 and _11 == _20:
            self.diagonal_winning_value = self.v[_02]

        elif (_00 == 3 or _00 == 4 or _00 == 5) and (_11 == 3 or _11 == 4 or _11 == 5) and (_22 == 3 or _22 == 4 or _22
            == 5):
            self.diagonal_winning_value = 'Bar'

        elif (_02 == 3 or _02 == 4 or _02 == 5) and (_11 == 3 or _11 == 4 or _11 == 5) and (_20 == 3 or _20 == 4 or _20
            == 5):
            self.diagonal_winning_value = 'Bar'


    def match(self, matrix):
        """ Checks the horizontal row for a match, and returns the values in the row if they do match."""

        horizontal = []
        for i in matrix[1]:
            horizontal.append(i)

        if horizontal[0] == horizontal[1] and horizontal[1] == horizontal[2]:
            self.horizontal_winning_value = self.v[horizontal[0]]
        elif (horizontal[0] == 3 or horizontal[0] == 4 or horizontal[0] == 5) and (horizontal[1] == 3 or
            horizontal[1] == 4 or horizontal[1] == 5) and (horizontal[2] == 3 or horizontal[2] == 4 or
            horizontal[2] == 5):
            self.horizontal_winning_value = 'Bar'

    def multiplier(self):  # sets the payout to 75% of full if diagonal match
        if self.horizontal_winning_value is not None:
            self.multiplier = 1
        elif self.diagonal_winning_value is not None:
            self.multiplier = 0.75

    def payouts(self):  # payouts should vary
        pass

def test():
    x = 0
    while x < 15:

        #create slot_machine instance
        test = Slot_machine()
        spin = test.rep_matrix()[0]
        test.match(spin)
        test.diagonal(spin)


        print test.horizontal_winning_value
        print test.diagonal_winning_value
        x += 1
    # print spin
    #match() returns True if horizontal match, False if no match, True if 3 bars of any value
    # print test.match(spin)

        player1 = Player('Alan')
        assert player1.tokens == 0
        player1.add_tokens(100)
        assert player1.tokens == 100


test()



