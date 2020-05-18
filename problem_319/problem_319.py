# Heuristic search is a technique that uses heuristic value for optimizing the search.
# A* is a computer algorithm that is widely used in pathfinding and graph traversal,
# the process of plotting an efficiently traversable path between multiple points, called nodes.
# The key feature of the A* algorithm is that it keeps a track of each visited node which helps
# in ignoring the nodes that are already visited, saving a huge amount of time.
# It also has a list that holds all the nodes that are left to be explored and it chooses the most optimal node
# from this list, thus saving time not exploring unnecessary or less optimal nodes.
# So we use two lists namely ‘open list‘ and ‘closed list‘ the open list contains all the nodes
# that are being generated and are not existing in the closed list and each node explored after
# it’s neighboring nodes are discovered is put in the closed list and the neighbors are put in
# the open list this is how the nodes expand
#
# The next node chosen from the open list is based on its f score,
# the node with the least f score is picked up and explored
# f-score = h-score + g-score
# A* uses a combination of heuristic value (h-score: how far the goal node is)
# as well as the g-score (i.e. the number of nodes traversed from the start node to current node).
# We first move the empty space in all the possible directions in the start state and calculate f-score
# for each state. This is called expanding the current state.
# After expanding the current state, it is pushed into the closed list and
# the newly generated states are pushed into the open list
from basic import NodePuzzle


class Puzzle:
    def __init__(self, size):
        self.n = size
        self.open = []
        self.closed = []

    def accept(self):
        puzzle = []
        for i in range(0, self.n):
            temp = input().split(" ")
            puzzle.append(temp)
        return puzzle

    def f(self, start, goal):
        return self.h(start.data, goal) + start.level

    def h(self, start, goal):
        temp = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp

    def process(self):
        print("Enter the start state matrix \n")
        start = self.accept()
        print("Enter the goal state matrix \n")
        goal = self.accept()
        start = NodePuzzle(start, 0, 0)
        start.fval = self.f(start, goal)
        """ Put the start node in the open list"""
        self.open.append(start)
        print("\n\n")
        while True:
            cur = self.open[0]
            print("")
            print("  | ")
            print("  | ")
            print(" \\\'/ \n")
            for i in cur.data:
                for j in i:
                    print(j, end=" ")
                print("")
            """ If the difference between current and goal node is 0 we have reached the goal node"""
            if self.h(cur.data, goal) == 0:
                break
            for i in cur.generate_child():
                i.fval = self.f(i, goal)
                self.open.append(i)
            self.closed.append(cur)
            del self.open[0]

        """ sort the open list based on f value """
        self.open.sort(key=lambda x: x.fval, reverse=False)


puz = Puzzle(3)
puz.process()
