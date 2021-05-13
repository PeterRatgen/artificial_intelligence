def alpha_beta_decision(state):
    infinity = float('inf')

    def max_value(state, alpha, beta):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for successor in successors_of(state):
            v = max(v, min_value(successor, alpha, beta))
            if v >= beta:
                return v
            alpha = min(alpha, v)
        return v

    def min_value(state, alpha, beta):
        if is_terminal(state):
            return utility_of(state)
        v = infinity

        for successor in successors_of(state):
            v = min(v, max_value(successor, alpha, beta))
            if v <= alpha:
                return v
            beta = max(beta, v)
        return v

    state = argmax(
        successors_of(state),
        lambda a: min_value(a, infinity, -infinity)
    )
    return state


def is_terminal(state):
    finishing = [1, 2]
    #print("state " + str(state))
    for i in state:
        if i not in finishing:
            return False

    return True


def utility_of(state):
    if sum(state) % 2 == 0:
        if len(state) % 2 == 0:
            #length is uneven
            return 1
        else:
            #length is even
            return -1
    else: 
        if len(state) % 2 == 0:
            return -1
        else:
            return 1


def successors_of(state):
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

def argmax(iterable, func):
    return max(iterable, key=func)


def computer_select_pile(state):
    new_state = alpha_beta_decision(state)
    return new_state


def user_select_pile(list_of_piles):
    '''
    Given a list of piles, asks the user to select a pile and then a split.
    Then returns the new list of piles.
    '''
    print("\n    Current piles: {}".format(list_of_piles))

    i = -1
    while i < 0 or i >= len(list_of_piles) or list_of_piles[i] < 3:
        print("Which pile (from 1 to {}, must be > 2)?".format(len(list_of_piles)))
        i = -1 + int(input())

    print("Selected pile {}".format(list_of_piles[i]))

    max_split = list_of_piles[i] - 1

    j = 0
    while j < 1 or j > max_split or j == list_of_piles[i] - j:
        if list_of_piles[i] % 2 == 0:
            print(
                'How much is the first split (from 1 to {}, but not {})?'.format(
                    max_split,
                    list_of_piles[i] // 2
                )
            )
        else:
            print(
                'How much is the first split (from 1 to {})?'.format(max_split)
            )
        j = int(input())

    k = list_of_piles[i] - j

    new_list_of_piles = list_of_piles[:i] + [j, k] + list_of_piles[i + 1:]

    print("    New piles: {}".format(new_list_of_piles))

    return new_list_of_piles


def main():
    state = [20]

    while not is_terminal(state):
        state = computer_select_pile(state)
        if not is_terminal(state):
            state = user_select_pile(state)

    print("    Final state is {}".format(state))


if __name__ == '__main__':
    main()
