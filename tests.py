import unittest
from slot import SlotMachine, Player, InsufficientFunds


class SlotTests(unittest.TestCase):

    def setUp(self):
        self.slot = SlotMachine()

    def test_matches(self):
        """Winning matches should equal their corresponding slot values."""
        self.slot.matrix = [[2, 3, 4],  # matches horizontally and diagonally
                            [3, 4, 5],
                            [4, 5, 0]]

        self.slot.horizontal_check(self.slot.matrix)
        self.slot.diagonal_check(self.slot.matrix)

        self.assertEqual(self.slot.horizontal_winning_value, "MIX BAR")
        self.assertEqual(self.slot.diagonal_winning_value, "2-BAR!")

    def test_generate_matrix(self):
        """Should return an embedded list with 3 elements within each list"""
        self.slot.create_matrix_values()
        self.assertEqual(len(self.slot.matrix), 3)
        for element in self.slot.matrix:
            self.assertEqual(len(element), 3)

    def test_represent_matrix(self):
        """Should map generated values to appropriate slot values"""
        represented_matrix = self.slot.represent_matrix()
        for row in represented_matrix:
            self.assertTrue(all(True for element in row if element in self.slot.values))


class PlayerTests(unittest.TestCase):
    def setUp(self):
        self.user = Player('User')

    def test_balance(self):
        """User balance should equal whatever amount is added via add_tokens() method"""
        self.assertIs(self.user.tokens, 0)
        self.user.add_tokens(10)
        self.assertEqual(self.user.tokens, 10)

        self.user.add_tokens(20)
        self.assertEqual(self.user.tokens, 30)

    def test_bet(self):
        """User balance should decrease by whatever amount is passed to bet() method"""
        self.user.add_tokens(100)
        with self.assertRaises(InsufficientFunds):
            self.user.bet(200)
        self.assertEqual(self.user.tokens, 100)
        self.user.bet(50)
        self.assertEqual(self.user.tokens, 50)
        self.user.bet(25)
        self.assertEqual(self.user.tokens, 25)
        self.user.bet(25)
        self.assertEqual(self.user.tokens, 0)


class GameTests(unittest.TestCase):

    def setUp(self):
        self.slot = SlotMachine()
        self.user = Player('User')
        self.slot.matrix = [[2, 3, 4], 
                            [3, 4, 5],
                            [4, 5, 0]]

    def test_bet(self):
        pass

    def test_horizontal_payouts(self):
        """Should multiply the wager amount by the associated
        multiplier value, and add the result to Player.tokens"""
        self.slot.horizontal_check(self.slot.matrix)  # MIX BAR
        self.slot.wager = 3
        self.slot.payouts(self.user)
        self.assertEqual(self.user.tokens, 9)

    def test_diagonal_payouts(self):
        """Should multiply the wager amount by the associated
        multiplier value and 0.75, then add the result to 
        Player.tokens"""
        self.slot.diagonal_check(self.slot.matrix)  # 2-BAR!
        self.slot.wager = 3
        self.slot.payouts(self.user)
        self.assertEqual(self.user.tokens, 112)

if __name__ == '__main__':
    unittest.main()
