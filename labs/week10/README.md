# Algorithm example

Completed the four functions.


# 8-queens

Created data structure such that fitness level are only calculated once. The
structure is `((individual), fitness))` where the individual is the placement of
the queens.

The `fitness_positive_fn` has been modified to take the data structure of an
individual with fitness field empty.

The reproduction generates two child in accordance with the Homework sheet.

Tuning of the parameter is not 100%, results are in the range of 24-28 correctly
placed queens.
