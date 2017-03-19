# This file is pretty much the backbone for every higher order function we need for this

# This is a node that's utilized when we need to store the moves we've made
# It also allows us to record the depth of each action in the search tree
class Node:
    def __init__(self, state, parent, depth):
        self.state = state
        self.parent = parent
        self.depth = depth

    # Override '<' so we can implement a priority queue
    def __lt__(self, other):
        return type(self.state) == type(other.state)

    # This just follows the node chain up to the root
    def solution(self):

        thisNode = self
        solutionList = []
        # Follows parent node until we reach the head, the return a sequence to a solution
        while thisNode != 0:
            solutionList.insert(0, thisNode.state)
            thisNode = thisNode.parent

        return solutionList


# Define a yard as a class for easy grouping/access to connectivity list, state, and goal state.
class TrainYard:
    def __init__(self, yard, initState, goalState):
        self.yard = yard
        self.state = initState
        self.goalState = goalState

# Checks that a move is valid before doing said move
# ( x-1 because python lists are 0-indexed )
def validL(yardList, yardState, y, x):
    return ((x, y) in yardList) and (len(yardState[y - 1]) != 0) and \
           ('*' in yardState[x - 1] or '*' in yardState[y - 1])


def validR(yardList, yardState, x, y):
    return ((x, y) in yardList) and (len(yardState[x - 1]) != 0) and \
           ('*' in yardState[x - 1] or '*' in yardState[y - 1])


# For both left() and right(), we must check that the move is allowed before making it
def left(yardList, yardState, y, x):
    valid = validL(yardList, yardState, y, x)

    if valid:
        # left moves get appended
        yardState[x - 1].append(yardState[y - 1].pop(0))

    else:
        return 0


def right(yardList, yardState, x, y):
    valid = validR(yardList, yardState, x, y)

    if valid:
        # right moves get inserted at the beginning
        yardState[y - 1].insert(0, yardState[x - 1].pop(len(yardState[x - 1]) - 1))

    else:
        return 0
