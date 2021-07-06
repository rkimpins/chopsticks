FINGERS = 5 # number of fingers per hand
HANDS = 2 # number of hands per player


#TODO add switching rule (1,2 -> 2,1)
def next_states(state, suicide=False):
    next_states = []

    if state[0]:
        hand = (state[3], state[4])
        opponent_hand = (state[1], state[2])
    else:
        hand = (state[1], state[2])
        opponent_hand = (state[3], state[4])

    hand_total = hand[0] + hand[1]


    # Generate hand switch next states
    if suicide:
        start = 0
    else:
        start = 1

    new_hands = []
    for i in range(start, hand_total//2 + 1):
        if i%5 < (hand_total-i)%5:
            new_hand = (i % 5, (hand_total - i) % 5 )
        else:
            new_hand = ((hand_total - i) % 5, i % 5)
        if new_hand != hand and new_hand not in new_hands:
            new_hands.append(new_hand)

    for new_hand in new_hands:
        if state[0] == 0:
            new_state = (-state[0]+1, new_hand[0], new_hand[1], state[3], state[4])
        elif state[0] == 1:
            new_state = (-state[0]+1, state[1], state[2], new_hand[0], new_hand[1])
        next_states.append(new_state)

    # Generate hand strike next states
    temp_opponent_hands = []
    if hand[0] != 0:
        if opponent_hand[0] != 0:
            temp_opponent_hands.append((opponent_hand[0] + hand[0], opponent_hand[1]))
        if opponent_hand[1] != 0:
            temp_opponent_hands.append((opponent_hand[0], opponent_hand[1] + hand[0]))
    if hand[1] != 0:
        if opponent_hand[0] != 0:
            temp_opponent_hands.append((opponent_hand[0] + hand[1], opponent_hand[1]))
        if opponent_hand[1] != 0:
            temp_opponent_hands.append((opponent_hand[0], opponent_hand[1] + hand[1]))
    #temp_opponent_hands = [
    #        (opponent_hand[0] + hand[0], opponent_hand[1]),
    #        (opponent_hand[0] + hand[1], opponent_hand[1]),
    #        (opponent_hand[0], opponent_hand[1] + hand[0]),
    #        (opponent_hand[0], opponent_hand[1] + hand[1])
    #        ]
    opponent_hands = []
    #remove duplicates and remove case where striking hand is dead
    for new_opponent_hand in temp_opponent_hands:
        if new_opponent_hand[0]%5 > new_opponent_hand[1]%5:
            new_opponent_hand = (new_opponent_hand[1]%5, new_opponent_hand[0]%5)
        else:
            new_opponent_hand = (new_opponent_hand[0]%5, new_opponent_hand[1]%5)
        if new_opponent_hand != opponent_hand and new_opponent_hand not in opponent_hands:
            opponent_hands.append(new_opponent_hand)

    for new_opponent_hand in opponent_hands:
        if state[0] == 0:
            new_state = (-state[0]+1, state[1], state[2], new_opponent_hand[0], new_opponent_hand[1])
        elif state[0] == 1:
            new_state = (-state[0]+1, new_opponent_hand[0], new_opponent_hand[1], state[3], state[4])
        next_states.append(new_state)



    return next_states

def validate_state(state):
    #valid turn indicator
    if state[0] not in [0,1]:
        return False
    #valid finger amount
    for i in range(1, HANDS*2 + 1):
        if state[i] < 0 or state[i] > FINGERS - 1:
            return False
    #at least one player alive
    alive = False
    for i in range(1, HANDS*2 + 1):
        if state[i]:
            alive = True
    return alive

def game_over(state):
    if (state[1] == 0 and state[2] == 0) or (state[3] == 0 and state[4] == 0):
        return True
    return False

def winner(state):
    if (state[1] == 0 and state[2] == 0):
        return 0
    if(state[3] == 0 and state[4] == 0):
        return 1
    return -1

def state_value(state):
    """
    if (state[1] == 0 and state[2] == 0):
        if state[0] == 0:
            return -1
        else:
            return 1
    if (state[3] == 0 and state[4] == 0):
        if state[0] == 1:
            return -1
        else:
            return 1
    return 0
    """
    if (state[1] == 0 and state[2] == 0) or (state[3] == 0 and state[4] == 0):
        return 1
    else:
        return 0

def negamax(state, depth, player):
    if depth == 0 or game_over(state):
        #print(state, depth, player * state_value(state))
        return player * state_value(state)
    value = float("-inf")
    children = next_states(state)
    for child in children:
        value = max(value, negamax(child, depth - 1, player * -1))
    #print(state, depth, -value)
    return value * -1

def generate_all_states():
    # before shortcut = 800
    # after shortcut = 196 (not counting game end states)
    states = []
    for p1h1 in range(0, FINGERS):
        for p1h2 in range(max(1, p1h1), FINGERS):
            for p2h1 in range(0, FINGERS):
                    for p2h2 in range(max(1, p2h1), FINGERS):
                        states.append((0, p1h1, p1h2, p2h1, p2h2))
    return states

def state_p_to_negamax_p(state_player):
    return ((state_player * 2) - 1) * -1

def solve_all_states():
    states = generate_all_states()
    for state in generate_all_states():
        print(state, negamax(state, 8, state_p_to_negamax_p(state[0])))

def main():
    print(-negamax((0, 0, 1, 0, 3), 5, 1)) #-1
    print(-negamax((1, 0, 1, 0, 4), 5, -1)) #1
    print(-negamax((1, 0, 1, 0, 4), 5, -1)) #1
    print(negamax((0, 0, 3, 0, 3), 5, 1)) #1
    print(negamax((1, 2, 3, 0, 3), 5, -1)) #-1
    print(negamax((1, 0, 3, 0, 3), 5, -1)) #1
    print(negamax((0, 0, 1, 0, 3), 5, 1)) #-1
    print(negamax((1, 0, 1, 0, 4), 5, -1)) #1
    print(negamax((0, 0, 4, 0, 1), 5, 1)) #1
    print(negamax((1, 0, 4, 0, 0), 5, -1)) #-1

if __name__ == "__main__":
    main()
