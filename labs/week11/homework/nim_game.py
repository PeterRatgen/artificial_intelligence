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
    finishing = [1, 2]
    for i in state:
        if i not in finishing:
            return False

    return True



def utility_of(state):
    """
    returns +1 if MAX is the winner, returns 0 if MIN is the winner
    """

    if sum(state) % 2 == 1:
        if len(state) % 2 == 1:
            return 1
        else:
            return 0
    else: 
        if len(state) % 2 == 0:
            return 0
        else:
            return 1



def successors_of(state):
    """
    returns a list of tuples (move, state) as shown in the exercise slides
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """

    def expand(param):
        return_arr = [] 
        for i in range(1, param // 2 + 1):
            add_arr = sorted([param - i, i - 0], reverse=True)
            if add_arr[0] == add_arr[1]:
                continue
            return_arr.append(add_arr) 
        if len(return_arr) == 0:
            return return_arr.append([])
        return return_arr

    def flatten(arr):
        flat = []
        for j in arr:
            if type(j) == list:
                for k in j:
                    flat.append(k)
            else:
                flat.append(j)
        return flat

    
    return_state = []

    for i in range(len(state)):
        print(state[i])
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
    for c in state:
        print(c * "-")


def main():
    board = [7]
    while not is_terminal(board):
        board.append(minmax_decision(board))
        board.sort()
        if not is_terminal(board):
            display(board)
            board[int(input('Your move? '))] = 'O'
    print("Game has ended: " + str(utility_of(board)))
    display(board)


def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    #print(successors_of([0, 1, 2, 3, 4, "X", 6, 7, "X"]))
    #print(is_terminal([2, 2, 1, 1, 1]))
    print(successors_of([5,4, 3, 2]))
    #main()
