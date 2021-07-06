from chopsticks import *

def test_switch_next_states():
    tests = [
        ((0, 0, 1, 1, 1), [(1, 0, 1, 1, 2)]),
        ((0, 1, 1, 1, 1), [(1, 1, 1, 1, 2)]),
        ((0, 1, 2, 1, 1), [(1, 1, 2, 1, 2), (1, 1, 2, 1, 3)]),
        ((0, 1, 3, 1, 1), [(1, 2, 2, 1, 1), (1, 1, 3, 1, 2), (1, 1, 3, 1, 4)]),
        ((0, 1, 4, 1, 1), [(1, 2, 3, 1, 1), (1, 1, 4, 1, 2), (1, 1, 4, 0, 1)]),
        ((0, 2, 4, 1, 1), [(1, 0, 1, 1, 1), (1, 3, 3, 1, 1), (1, 2, 4, 1, 3), (1, 2, 4, 0, 1)]),
        ((0, 3, 4, 1, 1), [(1, 1, 1, 1, 1), (1, 0, 2, 1, 1), (1, 3, 4, 1, 4), (1, 3, 4, 0, 1)]),
        ((0, 4, 4, 1, 1), [(1, 1, 2, 1, 1), (1, 0, 3, 1, 1), (1, 4, 4, 0, 1)]),
        ((1, 1, 1, 0, 1), [(0, 1, 2, 0, 1)]),
        ]

    for test in tests:
        print(next_states(test[0]))
        assert next_states(test[0]) == test[1]

def test_validate_state():
    tests = [
        ((0, 0, 1, 0, 0), True),
        ((1,0,1,0,0), True),
        ((2,0,1,0,1), False),
        ((-1,0,1,0,1), False),
        ((0,0,6,0,1), False),
        ((0,0,3,0,3), True)
        ]
    for test in tests:
        print(validate_state(test[0]))
        assert validate_state(test[0]) == test[1]

def test_negamax():
    tests = [
        ((0, 4, 4, 0, 1), 1),
        ((0, 0, 1, 0, 3), -1),
        ((1, 0, 1, 4, 4), 1)
    ]
    for test in tests:
        assert negamax(test[0]) == test[1]

def state_p_to_negamax_p(state_player):
    return ((state_player * 2) - 1) * -1

def test_negamax():
    tests = [
        ((0, 4, 4, 0, 1), 1),
        ((0, 0, 1, 0, 3), -1),
        ((1, 0, 1, 4, 4), 1)
    ]
    for test in tests:
        assert negamax(test[0], 12, state_p_to_negamax_p(test[0][0])) == test[1]
