############################### Written by Corey Beinhart
from itertools import count
from queue import PriorityQueue
from ExpandingAndMoving import expand
from Train import Node

############################################# Problem 4 ###############################################################

# NOTE: For some reason, this takes extremely long on YARD-2 - around 12 minutes. But it still finds a solution.

# A recursive DLS implementation
def recursiveDLS(yardList, yardState, yardGoal, limit):
    # Count expanded nodes
    counter = 0
    # return state if it is the goal
    if yardState.state == yardGoal:
        return yardState

    # return 0 if cutoff is reaches
    elif limit == 0:
        return 0

    else:
        # Now we expand each node of the tree
        # Each action is a node from which we can branch further into more actions
        for action in expand(yardList, yardState.state):
            # print(action, limit)
            counter += 1
            search = recursiveDLS(yardList, Node(action, yardState, yardState.depth + 1), yardGoal, limit - 1)

            # If the search did no return 0, then we have found a solution
            if search != 0:
                return search

        return 0


# def dls(yard, limit):
#     return recursiveDLS(yard.yard, Node(yard.state, 0), yard.goalState, limit)

# Iterative deepening portion
def itrDeepening(yard):
    # Iterate to infinity - be careful to use only solvable yards, otherwise this will iterate forever
    for i in count():
        # Simply run DLS for each iterated depth
        # print("Depth %s" % i)
        search = recursiveDLS(yard.yard, Node(yard.state, 0, 0), yard.goalState, i)

        # Make sure we don't return a cutoff
        if search != 0:

            return search

    return 0

##################################################### Problem 6 ########################################################

# First we construct a data structure to store the locations of the cars in the goal state
# This prevents us from having to calculate the goal positions every single time we calculate a heuristic
def goalMap(goalState):
    gMap = {}

    # Iterate through all of the elements of the yard in the goal state
    for x in goalState:

        for y in x:
            # Map each car to its track location
            gMap[y] = (goalState.index(x) + 1, x.index(y) + 1)

    return gMap


def heuristic(yardList, yardState, gMap):
    score = 0

    # Iterate through the current state
    for track in yardState:

        for car in track:

            # Compare car locations in the current state to the locations in the goal state
            # If the car is connected to the goal track, add 1 to the heuristic score
            if ((yardState.index(track) + 1, gMap[car][0]) in yardList) or (
                (gMap[car][0], yardState.index(track) + 1) in yardList):
                score += 1

            # If the car is on the correct track
            elif yardState.index(track) + 1 == gMap[car][0]:

                # And the car is in the correct position on the correct track, then nothing is added to the heuristic
                if track.index(car) + 1 == gMap[car][1]:
                    score = score

                # But if the car is on the correct track but not in the correct position
                # then add the distance from the correct position to the score
                else:
                    score += abs(track.index(car) + 1 - gMap[car][1])

            # Otherwise the car is not directly connected to the goal track, so it will take AT LEAST two moves
            else:

                score += 2

    return score


def astar(yard):


    # Here I am storing the frontier as a priority queue
    frontier = PriorityQueue()

    # Initialize initial state as the head node
    node = Node(yard.state, 0, 0)

    # This calculates "coordinates" of cars in solution so we don't recalculate them over and over
    goals = goalMap(yard.goalState)

    # Now we iterate through the search tree
    while node.state != yard.goalState:
        # Expand each visited state
        for action in expand(yard.yard, node.state):
            # Insert each child of the current state into our priority queue,
            # recording the depth of the node as we go down

            frontier.put((heuristic(yard.yard, action, goals) + node.depth + 1, Node(action, node, node.depth + 1)))
        # Pick the node on the frontier with the lowest heuristic score
        node = frontier.get()[1]
    return node