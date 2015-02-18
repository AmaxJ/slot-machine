from slots import SlotMachine, Player

def test():
    test_values = [[2, 3, 4],  # matches horizontally and diagonally
                   [3, 4, 5],
                   [4, 5, 0]]
    #create slot_machine instance
    test = SlotMachine()
    test.matrix = test_values

    test.horizontal_check(test.matrix)
    test.diagonal_check(test.matrix)

    assert test.horizontal_winning_value == 'MIX BAR'
    assert test.diagonal_winning_value == "2-BAR!"

    # spin = test.rep_matrix()[0]
    # print(spin)
    # test.match(spin)
    # test.diagonal(spin)
    # #test.payout()

    # print("horizontal: ", test.horizontal_winning_value)
    # print("diagonal: ", test.diagonal_winning_value)

    player1 = Player('Alan')
    assert player1.tokens == 0
    player1.add_tokens(100)
    assert player1.tokens == 100

test()


# Made sure the above test worked before creating the random one.
def example_slots():
    slots = SlotMachine()
    slots.create_matrix_values()
    slots.diagonal_check(slots.matrix)
    slots.horizontal_check(slots.matrix)
    slots.rep_matrix()
    print("\n")
    print("Horizontal Winnings: ", slots.horizontal_winning_value)
    print("Diagonal Winnings: ", slots.diagonal_winning_value)
example_slots()

