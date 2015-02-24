import unittest, mock
from slot import SlotMachine, Player


class SlotTests(unittest.TestCase):

    def setUp(self):
        self.slot = SlotMachine()

    def test_checkMatches(self):
        """horizontal_winning_value should == "MIX BAR" when [3,4,5] is 
        slotMachine.matrix[1] and diagonal_winning_value should == "2-BAR!"
        when [4,4,4] in matrix[0][2], [1][1], and [2][0] """
        self.slot.matrix = [[2, 3, 4],  # matches horizontally and diagonally
                            [3, 4, 5],
                            [4, 5, 0]]

        self.slot.horizontal_check(self.slot.matrix)
        self.slot.diagonal_check(self.slot.matrix)

        self.assertEqual(self.slot.horizontal_winning_value, "MIX BAR")
        self.assertTrue(self.slot.diagonal_winning_value == "2-BAR!", True)

    def test_generateMatrix(self):
        """Should return a 2-d list with 3 elements in each list"""
        self.slot.create_matrix_values()
        self.assertEqual(len(self.slot.matrix), 3)
        for element in self.slot.matrix:
            self.assertEqual(len(element), 3)

    def test_repMatrix(self):
        """Should map generated values to appropriate values in value 
        list (SlotMachine.v)"""
        _,repped_matrix = self.slot.rep_matrix()
        for element in repped_matrix:
            for item in element:
                self.assertIn(item, self.slot.v)


class PlayerTests(unittest.TestCase):
    def setUp(self):
        self.user = Player('User')

    def test_balance(self):
        """User balance should equal whatever amount is added
        via add_tokens() method"""
        self.assertIs(self.user.tokens, 0)
        self.user.add_tokens(10)
        self.assertEqual(self.user.tokens, 10)

        self.user.add_tokens(20)
        self.assertEqual(self.user.tokens, 30)

    def test_betMethod(self):
        """User balance should decrease by whatever amount is
        passed to bet() method"""
        self.user.add_tokens(100)
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
        self.user.add_tokens(10)

    def test_placeBets(self):
        pass

    def test_payouts(self):
        pass


if __name__ == '__main__':
    unittest.main()
