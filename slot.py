from random import randrange
from itertools import permutations
from graphics import *  # WINNER graphic that will display when player wins


class Player(object):
    def __init__(self, name):
        self.name = name
        self.tokens = 0
        self.luck = 0

    def add_tokens(self, number_of_tokens):
        self.tokens += number_of_tokens
        
            
    def bet(self, amount):
        if self.tokens >= amount:
            self.tokens -= amount
        else:
            print("You do not have enough tokens to make that bet.")

    def has_balance(self):
        return self.tokens > 0

# Move a formatted version of this info to the readme(?)
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


class SlotMachine(object):
    def __init__(self):
        self.v = ['SIX!!!', 'LUCKY6', 'CHERRY', '3-BAR!', '2-BAR!', '1-BAR!'] 
        self.multiplier = 1
        self.wager = 0
        self.diagonal_winning_value = 0
        self.horizontal_winning_value = 0
        self.matrix = [[], [], []]

    @staticmethod
    def valid_bet(wager_size):
        # Checks that player bet is 3 or less
        return 0 < wager_size <= 3

    @staticmethod
    def reel_values(value):
        # Based on the value on display in the middle, calculates the values above and below on the reel.
        upper, lower = 0, 0
        if value == 0:
            upper, lower = 5, 1
        elif value == 5:
            upper, lower = 4, 0
        else:
            upper, lower = value - 1, value + 1
        return [upper, lower]

    def create_matrix_values(self):
        # creates a matrix with numbers that correspond to each value in the list 'v'.
        self.matrix = [[],[],[]]
        numbers = [randrange(6) for r in range(3)]
        # Top Row
        for n in numbers:
            self.matrix[0].append(self.reel_values(n)[0])
        # Middle Row
            self.matrix[1].append(n)
        # Bottom Row
            self.matrix[2].append(self.reel_values(n)[1])

        return self.matrix

    def rep_matrix(self):
        # Generates a matrix and then converts it to slot values for display
        matrix = self.create_matrix_values()
        repped = [[self.v[int(matrix[0][i])] for i in range(3)],
                  [self.v[int(matrix[1][i])] for i in range(3)],
                  [self.v[int(matrix[2][i])] for i in range(3)]]
        self.package_matrix(repped)

        # Kept return for testing purposes(?)
        return matrix, repped

    @staticmethod
    def package_matrix(matrix):
        # Prints each row on a separate line
        for row_number in range(3):
            print('  '.join(matrix[row_number]))

    @staticmethod
    def all_same(values):
        # Checks to see if all values within a list are the same.
        return not values or values.count(values[0]) == len(values)
        # return all([values[0] == value for value in values])

    def diagonal_check(self, matrix):
        """Check if there is a match along the diagonals of the matrix and returns the winning value
        eg. SIX!!!, LUCKY6 or just BAR for any combination of 3-BAR, 2-BAR or 1-BAR."""
        # Assign matrix elements to variables to make it easier to view

        first_diagonal = (matrix[0][0], matrix[1][1], matrix[2][2])
        second_diagonal = (matrix[2][0], matrix[1][1], matrix[0][2])
        mix_bar_values = list(set(permutations([3, 3, 3, 4, 4, 4, 5, 5, 5], 3)))

        if self.all_same(first_diagonal):
            self.diagonal_winning_value = self.v[first_diagonal[0]]
        elif self.all_same(second_diagonal):
            self.diagonal_winning_value = self.v[second_diagonal[0]]
        elif first_diagonal in mix_bar_values or second_diagonal in mix_bar_values:
            self.diagonal_winning_value = "MIX BAR"
        else:
            self.diagonal_winning_value = 0

    # May want to rename this function to something that directly relates to the horizontal middle row.
    def horizontal_check(self, matrix):
        # Checks the horizontal row for a match, and returns the values in the row if they do match.
        horizontal = [i for i in matrix[1]]
        mix_bar_values = list(set(permutations([3, 3, 3, 4, 4, 4, 5, 5, 5], 3)))

        if self.all_same(horizontal):
            self.horizontal_winning_value = self.v[horizontal[0]]
        elif tuple(horizontal) in mix_bar_values:
            self.horizontal_winning_value = "MIX BAR"
        else:
            self.horizontal_winning_value = 0

    # def multiplier(self):  # redundant function
    #     if self.horizontal_winning_value:
    #         self.multiplier = 1
    #     elif self.diagonal_winning_value:
    #         self.multiplier = 0.75

    def place_bet(self, player):
        # sets self.wager to whatever the person bets
        print("Place a bet (max: 3). \n")
        try:
            print("How much would you like to bet?")
            self.wager = int(input("Tokens: "))
            if self.valid_bet(self.wager):
                player.bet(self.wager)
                print("You are betting {} tokens".format(self.wager))
            else:
                print("That amount is not allowed.")
                self.place_bet(player)
        except ValueError, TypeError:
            print("That's not a valid bet!")
            self.place_bet(player)

    def payouts(self, player):
        payouts = {
            'SIX!!!': 1500, 'LUCKY6': 250, 'CHERRY': 150,
            '3-BAR!': 100, '2-BAR!': 50, '1-BAR!': 20, 'MIX BAR': 3
        }

        # Can you win only horizontal or diagonal and not both?
        if self.horizontal_winning_value:
            payout_value = payouts[self.horizontal_winning_value]
            print("You have won {} tokens".format(payout_value))
            player.add_tokens(self.wager * payout_value)
        elif self.diagonal_winning_value:
            payout_value = payouts[self.diagonal_winning_value]
            print("You have won {} tokens".format(payout_value))
            player.add_tokens(self.wager * payout_value * 0.75)
        else:
            print("Won $0. Try again!")