import numpy as np

"""
Hidden Markov Model using Viterbi algorithm to find most
likely sequence of hidden states.

The problem is to find out the most likely sequence of states
of the weather (hot, cold) from a describtion of the number
of ice cream eaten by a boy in the summer.
"""


def main():
    np.set_printoptions(suppress=True)

    states = np.array(["initial", "hot", "cold", "final"])

    # To simulate starting from index 1, we add a dummy value at index 0
    observationss = [
        [None, 3, 1, 3],
        [None, 3, 3, 1, 1, 2, 2, 3, 1, 3],
        [None, 3, 3, 1, 1, 2, 3, 3, 1, 2],
    ]

    # Markov transition matrix
    # transitions[start, end]
    transitions = np.array([[.0, .8, .2, .0],  # Initial state
                            [.0, .6, .3, .1],  # Hot state
                            [.0, .4, .5, .1],  # Cold state
                            [.0, .0, .0, .0],  # Final state
                            ])

    # P(v|q)
    # emission[state, observation]
    emissions = np.array([[.0, .0, .0, .0],  # Initial state
                          [.0, .2, .4, .4],  # Hot state
                          [.0, .5, .4, .1],  # Cold state
                          [.0, .0, .0, .0],  # Final state
                          ])

    for observations in observationss:
        print("Observations: {}".format(' '.join(map(str, observations[1:]))))

        probability = compute_forward(states, observations, transitions, emissions)
        print("Probability: {}".format(probability))

        path = compute_viterbi(states, observations, transitions, emissions)
        print("Path: {}".format(' '.join(path)))

        print('')


def inclusive_range(a, b):
    return range(a, b + 1)


def compute_forward(states, observations, transitions, emissions):
    # number of states - subtract two because "initial" and "final" doesn't count.
    big_n = len(states) - 2

    # number of observations - subtract one, because a dummy "None" is added on index 0.
    big_t = len(observations) - 1

    # final state
    f = big_n + 1

    # probability matrix - all values initialized to 5, as 0 has meaning in the matrix
    forward = np.ones((big_n + 2, big_t + 1)) * 5

    '''
    FINISH FUNCITON
    '''
    


def compute_viterbi(states, observations, transitions, emissions):
    # number of states - subtract two because "initial" and "final" doesn't count.
    big_n = len(states) - 2

    # number of observations - subtract one, because a dummy "None" is added on index 0.
    big_t = len(observations) - 1

    # final state
    f = big_n + 1

    # probability matrix - all values initialized to 5, as 0 is valid value in matrix
    viterbi = np.ones((big_n + 2, big_t + 1)) * 5

    # Must be of type int, otherwise it is tricky to use its elements to index
    # the states
    # all values initialized to 5, as 0 is valid value in matrix
    backpointers = np.ones((big_n + 2, big_t + 1), dtype=int) * 5

    return []
    '''
    FINISH FUNCTION
    '''

    


def argmax(sequence):
    # Note: You could use np.argmax(sequence), but only if sequence is a list.
    # If it is a generator, first convert it: np.argmax(list(sequence))

    # Since we loop from 1 to big_n, the result of argmax is between
    # 0 and big_n - 1. However, 0 is the initial state, the actual
    # states start from 1, so we add 1.
    return 1 + max(enumerate(sequence), key=lambda x: x[1])[0]


if __name__ == '__main__':
    main()
