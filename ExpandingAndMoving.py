############################### Written by Corey Beinhart
from copy import deepcopy
from Train import validL, validR, left, right

#################################### Problem 1 #####################################################################

def possibleActions(yardList, yardState):

    # Collect all connectivity tuples on which we can move
    rightList = [x for x in yardList if validR(yardList, yardState, x[0], x[1])]
    leftList = [x for x in yardList if validL(yardList, yardState, x[1], x[0])]

    return rightList, leftList

#################################### Problem 2 #####################################################################

# Pretty self-explanatory
# Specify  direction and the x and y values for the action
def result(yardList, yardState, direction, a, b):
    # Copy the state to ensure we don't actually modify the original
    yardCopy = deepcopy(yardState)

    # Then we perform a movement on the copy of the original state depending on the specified direction
    if direction == "R":
        right(yardList, yardCopy, a, b)
    else:
        left(yardList, yardCopy, a, b)

    return yardCopy

#################################### Problem 3 #####################################################################

def expand(yardList, yardState):

    # Generate possible actions from given state
    moveR, moveL = possibleActions(yardList, yardState)

    # Each of these comprehensions collect the states that result from each of the possible moves
    rightMoves = [result(yardList, yardState, "R", x[0], x[1]) for x in moveR]
    leftMoves = [result(yardList, yardState, "L", y[1], y[0]) for y in moveL]

    return rightMoves + leftMoves