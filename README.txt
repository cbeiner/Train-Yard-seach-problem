############################### Written by Corey Beinhart

Hello! 

This project is formatted such that the fundamental functions, such as right() and left() are in Train.py. Also included
in this file is a Train class that stores the connectivity list, initial state, and goal state of a given train yard. It
also has a Node class used in the search algorithms. This stores a state, its parent state, and depth at which it occurs
in a search expansion.

The train yard is a connectivity list which describes which tracks in the train yard are connected. The engine (the '*')
is the only car that can move independently so each car can only move to a track with the engine. Each move only allows
cars to travel to a connected track specified by the connectivity list. The yard is represented as a list of lists, wherein
each sublist represents the cars on each track. [['*'], ['b'], ['a']] would be a three-track train yard in its initial 
state. The project will make possible movements of cars until the goal state is reached. 

Problems 1-3 in the PDF are included in ExpandingAndMoving.py. Problem 1 generates a list of possible left and right 
movements from a current state. Problem 2 will show the state that results from an action being taken. Problem 3 will 
return a list of states that are the results of all possible actions being taken.

Seach.py implements both an iterative deepening and A* search to find a the optimal sequence of actions from the initial
state to the goal state. The iterative deepening takes a *very long time to run but still finds the optimal solution.
I attribute the long runtime to ineffective state representation. On the other hand, my heuristic is extremely efficient. 
My heuristic calculates the total distance of all cars from the goal state.

In order to run the project, open up/run main.py. This will run every function that was assigned as part of the project
on each of the test yards given in the homework PDF. Follow the same formatting if you wish to test additional yards.

The write-up for the lab as well as explanation required in the assignment and Problem 5 are in a PDF called Program 1.doc
in the directory folder.

Hope you have as much fun testing it as I did writing it!
(Not actually, this was miserable to debug)

-Corey