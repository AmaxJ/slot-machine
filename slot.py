from math import floor as fl
from random import randrange
from itertools import permutations
from graphics import *  # WINNER graphic that will display when player wins


class InsufficientFunds(Exception):
    pass

class Player(object):
    def __init__(self, name):
        self.name = name
        self.tokens = 0
        self.luck = 0

    def add_tokens(self, number_of_tokens):
        try:
            self.tokens += number_of_tokens
        except TypeError:
            print "Please enter the number of tokens you wish to add."
        
            
    def bet(self, amount):
        if self.tokens >= amount:
            self.tokens -= amount
        else:
            raise(InsufficientFunds("You do not have enough tokens to make that bet."))

    def has_balance(self):
        return self.tokens > 0

class SlotMachine(object):
    def __init__(self):
        self.values = ['SIX!!!', 'LUCKY6', 'CHERRY', '3-BAR!', '2-BAR!', '1-BAR!']
        self.multiplier = 1
        self.wager = 0
        self.diagonal_winning_value = 0
        self.horizontal_winning_value = 0
        self.matrix = [[], [], []]
        self.mix_bar_value = list(set(permutations([3, 3, 3, 4, 4, 4, 5, 5, 5], 3)))

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
        # creates a matrix with numbers that correspond to each value.
        self.matrix = [[],[],[]]  # resets matrix values
        numbers = [randrange(6) for r in range(3)]
        # Top Row
        for n in numbers:
            self.matrix[0].append(self.reel_values(n)[0])
        # Middle Row
            self.matrix[1].append(n)
        # Bottom Row
            self.matrix[2].append(self.reel_values(n)[1])
        return self.matrix

    def represent_matrix(self):
        # Generates a matrix and then converts it to slot values for display
        matrix = self.create_matrix_values()
        represented_values = [[self.values[int(matrix[0][i])] for i in range(3)],
                             [self.values[int(matrix[1][i])] for i in range(3)],
                             [self.values[int(matrix[2][i])] for i in range(3)]]
        self.package_matrix(represented_values)
        # Kept return for testing purposes(?)
        return matrix, represented_values

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
        if self.all_same(first_diagonal):
            self.diagonal_winning_value = self.values[first_diagonal[0]]
        elif self.all_same(second_diagonal):
            self.diagonal_winning_value = self.values[second_diagonal[0]]
        elif first_diagonal in self.mix_bar_value or second_diagonal in self.mix_bar_value:
            self.diagonal_winning_value = "MIX BAR"
        else:
            self.diagonal_winning_value = 0

    def horizontal_check(self, matrix):
        # Checks the horizontal row for a match, and returns the values in the row if they do match.
        horizontal = [i for i in matrix[1]]
        if self.all_same(horizontal):
            self.horizontal_winning_value = self.values[horizontal[0]]
        elif tuple(horizontal) in self.mix_bar_value:
            self.horizontal_winning_value = "MIX BAR"
        else:
            self.horizontal_winning_value = 0

    def place_bet(self, player):
        # sets self.wager to whatever the person bets
        print("Place a bet (max: 3). \n")
        try:
            print("How much would you like to bet?")
            self.wager = int(raw_input("Tokens: "))
            if self.valid_bet(self.wager):
                player.bet(self.wager)
            else:
                print("That amount is not allowed.")
                self.place_bet(player)
        except (ValueError, TypeError):
            print("That's not a valid bet!")
            self.place_bet(player)

    def payouts(self, player):
        payouts = {
            'SIX!!!': 1500, 'LUCKY6': 250, 'CHERRY': 150,
            '3-BAR!': 100, '2-BAR!': 50, '1-BAR!': 20, 'MIX BAR': 3
        }
        
        if self.horizontal_winning_value:
            payout_value = payouts[self.horizontal_winning_value]
            print("You have won {} tokens!".format(self.wager * payout_value))
            player.add_tokens(self.wager * payout_value)
        elif self.diagonal_winning_value:
            payout_value = payouts[self.diagonal_winning_value]
            floor_payout = int(fl(self.wager * payout_value * 0.75))
            print("You have won {} tokens!".format(floor_payout))
            player.add_tokens(floor_payout)
        else:
            print("Won 0 tokens. Try again!")
