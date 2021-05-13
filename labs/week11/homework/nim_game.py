def minmax_decision(state):

    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for s in successors_of(state):
            v = max(v, min_value(s))
        #print('V: ' + str(v))
        return v

    def min_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = infinity
        for s in successors_of(state):
            v = min(v, max_value(s))
        return v

    infinity = float('inf')
    action = argmax(successors_of(state), lambda a: min_value(a))
    print("action " + str(action))
    return action


def is_terminal(state):
    """
    returns True if the state is either a win or a tie (board full)
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    finishing = [1, 2]
    #print("state " + str(state))
    for i in state:
        if i not in finishing:
            return False

    return True



def utility_of(state):
    """
    returns +1 if MAX is the winner, returns 0 if MIN is the winner
    """
    
    # if the initial state is uneven, then MAX will win only the len of the board is uneven.

    if sum(state) % 2 == 1:
        if len(state) % 2 == 1:
            #length is uneven
            return 1
        else:
            #length is even
            return 0
    else: 
        if len(state) % 2 == 0:
            return 0
        else:
            return 1

def flatten(arr):
    flat = []
    for j in arr:
        if type(j) == list:
            for k in j:
                flat.append(k)
        else:
            flat.append(j)
    return flat

def expand(param):
    return_arr = [] 
    for i in range(1, param // 2 + 1):
        add_arr = sorted([param - i, i - 0], reverse=True)
        if add_arr[0] == add_arr[1]:
            continue
        return_arr.append(add_arr) 
    if len(return_arr) == 0:
        return_arr = [[]]
    return return_arr

def successors_of(state):
    """
    returns a list of tuples (move, state) as shown in the exercise slides
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    return_state = []

    for i in range(len(state)):
        expanded = expand(state[i])
        if len(expanded[0]) != 0:
            for item in expanded: 
                new_state = state[:]
                new_state[i] = item
                new_state = flatten(new_state)
                new_state = sorted(new_state, reverse=True)
                return_state.append(new_state)

    return return_state

def display(state):
    print("Displaying state:")
    print(state)
    #for c in state:
    #    print(c * "-")

def get_new_stacks(board):
    new_board = board[:]
    index = int(input('Index to expanded (from 0) '))
    if len(board) <= index:
        print("Not a valid index, try again")
        return get_new_stacks(board)

    if len(expand(board[index])[0]) == 0:
        print("That index cannot be expanded, try again")
        return get_new_stacks(board)

    possible_stacks = expand(board[index])
    print("Split " + str(board[index]) + " into two stacks (equal size not allowed)")
    stack_1 = int(input('Stack 1: '))
    stack_2 = int(input('Stack 2: '))

    if stack_1 == stack_2:
        print("Stacks cannot be equal size, try again ")
        return get_new_stacks(board)

    if stack_1 + stack_2 != board[index]:
        print("Stacks do not equal " + str(board[index]) + ", try again")
        return get_new_stacks(board)

    new_stack = sorted([stack_1, stack_2], reverse=True)
    if new_stack not in possible_stacks:
        return get_new_stacks(board)

    new_board[index] = new_stack
    return sorted(flatten(new_board), reverse=True)




def main():
    board = [7]
    while not is_terminal(board):
        if not is_terminal(board):
            display(board)
            board = get_new_stacks(board)
        board = minmax_decision(board)
        board = sorted(board, reverse=True)

    print("Game has ended: " + str(utility_of(board)))
    display(board)


def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    print(utility_of([5, 1, 1]))
    main()
