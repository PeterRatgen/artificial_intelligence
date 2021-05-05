winning_states = [[0,1,2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5 , 8], [0, 4, 8], [2, 4, 6]]
signs = ["X", "O"]

def minmax_decision(state):

    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for (a, s) in successors_of(state):
            v = max(v, min_value(s))
        #print('V: ' + str(v))
        return v

    def min_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = infinity
        for (a, s) in successors_of(state):
            v = min(v, max_value(s))
        return v

    infinity = float('inf')
    action, state = argmax(successors_of(state), lambda a: min_value(a[1]))
    return action


def is_terminal(state):
    """
    returns True if the state is either a win or a tie (board full)
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    for placement in winning_states:
        if state[placement[0]] not in signs:
            continue
        if state[placement[0]] == state[placement[1]] and state[placement[1]] == state[placement[2]]:
            return True

    for i in state:
        if i not in signs:
            return False
    return True



def utility_of(state):
    """
    returns +1 if winner is X (MAX player), -1 if winner is O (MIN player), or 0 otherwise
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """

    for placement in winning_states:
        if state[placement[0]] not in signs:
            continue
        if state[placement[0]] == state[placement[1]] and state[placement[1]] == state[placement[2]]:
            if state[placement[0]] == "X":
                return 1
            if state[placement[0]] == "O":
                return -1
    return 0



def successors_of(state):
    """
    returns a list of tuples (move, state) as shown in the exercise slides
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    state_list = []
    counter = 0
    
    for i in range(len(state)):
        if state[i] not in signs:
            new_state = state[:]
            new_state[i] = "X"
            state_list.append((i, new_state))
    return state_list


def display(state):
    print("-----")
    for c in [0, 3, 6]:
        print(state[c + 0], state[c + 1], state[c + 2])


def main():
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    while not is_terminal(board):
        board[minmax_decision(board)] = 'X'
        if not is_terminal(board):
            display(board)
            board[int(input('Your move? '))] = 'O'
    print("Game has ended: " + str(utility_of(board)))
    display(board)


def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    #print(successors_of([0, 1, 2, 3, 4, "X", 6, 7, "X"]))
    main()
