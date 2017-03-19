############################### Written by Corey Beinhart
from Train import TrainYard, Node
from Search import itrDeepening, astar
from ExpandingAndMoving import result, expand, possibleActions
import time


def testYard():

    train1 = TrainYard([(1,2),(1,3),(2,6),(3,5),(4,5),(5,6)], [['*'],['e'],[],['b','c','a'],[],['d']],
                                [['*','a','b','c','d','e'],[],[],[],[],[]])

    train2 = TrainYard([(1, 2), (1, 5), (2, 3), (2, 4)], [['*'], ['d'], ['b'], ['a', 'e'], ['c']],
                              [['*', 'a', 'b', 'c', 'd', 'e'], [], [], [], []])

    train3 = TrainYard([(1,2),(1,3)], [['*'],['a'],['b']], [['*','a','b'],[],[]])

    train4 = TrainYard([(1,2),(1,3),(1,4)], [['*'],['a'],['b','c'],['d']], [['*','a','b','c','d'],[],[],[]])

    train5 = TrainYard([(1,2),(1,3),(1,4)], [['*'],['a'],['c','b'],['d']], [['*','a','b','c','d'],[],[],[]])

    start = time.clock()

    print("---------------Result---------------", "\n")
    print(result(train5.yard, train5.state, "R", 1, 2))
    print(result(train5.yard, train5.state, "L", 2, 1))
    print("---------------Possible Actions---------------", "\n")
    print(possibleActions(train5.yard, train5.state))
    print(expand(train5.yard, train5.state))
    print("---------------Iterative Deepening---------------", "\n")
    itr5 = itrDeepening(train5)
    print(itr5.solution())
    print("---------------A*---------------", "\n")
    astar5 = astar(train5)
    print(astar5.solution())
    print("Solution found at depth", astar5.depth)

    print(time.clock() - start, "seconds")

    print("---------------Result---------------", "\n")
    print(result(train4.yard, train4.state, "R", 1, 2))
    print(result(train4.yard, train4.state, "L", 2, 1))
    print("---------------Possible Actions---------------", "\n")
    print(possibleActions(train4.yard, train4.state))
    print("---------------Expand---------------", "\n")
    print(expand(train4.yard, train4.state))
    print("---------------Iterative Deepening---------------", "\n")
    itr4 = itrDeepening(train4)
    print(itr4.solution())
    print("---------------A*---------------", "\n")
    astar4 = astar(train4)
    print(astar4.solution())
    print("Solution found at depth", astar4.depth)

    print(time.clock() - start, "seconds")

    print("---------------Result---------------", "\n")
    print(result(train3.yard, train3.state, "R", 1, 2))
    print(result(train3.yard, train3.state, "L", 2, 1))
    print("---------------Possible Actions---------------", "\n")
    print(possibleActions(train3.yard, train3.state))
    print("---------------Expand---------------", "\n")
    print(expand(train3.yard, train3.state))
    print("---------------Iterative Deepening---------------", "\n")
    itr3 = itrDeepening(train3)
    print(itr3.solution())
    print("---------------A*---------------", "\n")
    astar3 = astar(train3)
    print(astar3.solution())
    print("Solution found at depth", astar3.depth)

    print(time.clock() - start, "seconds")

    print("---------------Result---------------", "\n")
    print(result(train2.yard, train2.state, "R", 1, 2))
    print(result(train2.yard, train2.state, "L", 2, 1))
    print("---------------Possible Actions---------------", "\n")
    print(possibleActions(train2.yard, train2.state))
    print("---------------Expand---------------", "\n")
    print(expand(train2.yard, train2.state))
    # print("---------------Iterative Deepening---------------", "\n)
    # Uncomment when you want to test... it will take awhile
    # itr2 = itrDeepening(train3)
    # print(itr2.solution())
    print("---------------A*---------------", "\n")
    astar2 = astar(train2)
    print(astar2.solution())
    print("Solution found at depth", astar2.depth)

    print(time.clock() - start, "seconds")

    print("---------------Result---------------", "\n")
    print(result(train1.yard, train1.state, "R", 1, 2))
    print(result(train1.yard, train1.state, "L", 2, 1))
    print("---------------Possible Actions---------------", "\n")
    print(possibleActions(train1.yard, train1.state))
    print("---------------Expand---------------", "\n")
    print(expand(train1.yard, train1.state))
    print("---------------A*---------------", "\n")
    astar1 = astar(train1)
    print(astar1.solution())
    print("Solution found at depth", astar1.depth)

    print(time.clock() - start, "seconds")


testYard()