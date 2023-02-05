import numpy as np

class Board(object):

    def __init__(self, board=None, moves=0, previous=None, depth=0, cost=0, key=0, parent=None, idsCost=0):

        self.board = board
        self.previous = previous
        self.moves = moves
        self.depth = depth
        self.parent = parent
        self.cost = cost
        self.key = key
        self.idsCost = idsCost
        if self.board:
            self.map = ''.join(str(e) for e in self.board)

    def checkGoal(self):
        goalState = np.array([1, 2, 3, 4, 5, 6, 7, 8, 0])
        count = 0
        for i in range(0, 9):
            if goalState[i] != self.board[i]:
                count += 1
        return count == 0

    def setParent(self):
        self.parent = self.previous

    def updateBoardMap(self):
        self.map = ''.join(str(e) for e in self.board)

    def moveTile(self, where):
        zero = self.findZero()
        if where == 'left':
            if zero % 3 != 0:
                t_col = (zero % 3) - 1
                t_row = int(zero / 3)
                self.swap(zero, t_row * 3 + t_col)
        if where == 'right':
            if zero % 3 != 2:
                t_col = (zero % 3) + 1
                t_row = int(zero / 3)
                self.swap(zero, t_row * 3 + t_col)
        if where == 'up':
            if int(zero / 3) != 0:
                t_col = (zero % 3)
                t_row = int(zero / 3) - 1
                self.swap(zero, t_row * 3 + t_col)
        if where == 'down':
            if int(zero / 3) != 2:
                t_col = (zero % 3)
                t_row = int(zero / 3) + 1
                self.swap(zero, t_row * 3 + t_col)

    def findZero(self):
        zero = None
        for i in range(0, 9):
            if self.board[i] == 0:
                zero = i
                break
        return zero

    def clone(self):
        return Board(self.board.copy(), self.moves + 1, self)

    def swap(self, source, target):
        self.board[source], self.board[target] = self.board[target], self.board[source]

    def neighbors(self):
        zero_index = self.findZero()
        neighbors = []
        # left
        if zero_index % 3 != 0:
            new_board = self.clone()
            new_board.moveTile('left')
            new_board.updateBoardMap()
            new_board.depth += 1
            new_board.idsCost += 1
            neighbors.append(new_board)
        # right
        if zero_index % 3 != 2:
            new_board = self.clone()
            new_board.moveTile('right')
            new_board.updateBoardMap()
            new_board.depth += 1
            new_board.idsCost += 1
            neighbors.append(new_board)
        # up
        if int(zero_index / 3) != 0:
            new_board = self.clone()
            new_board.moveTile('up')
            new_board.updateBoardMap()
            new_board.depth += 1
            new_board.idsCost += 1
            neighbors.append(new_board)
        # down
        if int(zero_index / 3) != 2:
            new_board = self.clone()
            new_board.moveTile('down')
            new_board.updateBoardMap()
            new_board.depth += 1
            new_board.idsCost += 1
            neighbors.append(new_board)
        return neighbors

    @staticmethod
    def index(state):
        index = np.array(range(9))
        for x, y in enumerate(state):
            index[y] = x
        return index

    def heurMisplacedTiles(self):
        goalState = np.array([1, 2, 3, 4, 5, 6, 7, 8, 0])
        state = self.board
        return np.sum(goalState != state)

    def heurManhattan(self):
        goalState = np.array([1, 2, 3, 4, 5, 6, 7, 8, 0])
        state = self.index(self.board)
        goal = self.index(goalState)
        return sum((abs(state // 3 - goal // 3) + abs(state % 3 - goal % 3))[1:])

    def heurEuclidian(self):
        goalState = np.array([1, 2, 3, 4, 5, 6, 7, 8, 0])
        state = self.index(self.board)
        goal = self.index(goalState)
        return sum(np.sqrt((np.square(state // 3 - goal // 3)) + np.square(state % 3 - goal % 3))[1:])

    def toPQMisplacedTiles(self, count):
        return (self.moves + self.heurMisplacedTiles(), count, self)

    def toPQManhattan(self, count):
        return (self.moves + self.heurManhattan(), count, self)

    def toPQEuclidian(self, count):
        return (self.moves + self.heurEuclidian(), count, self)

    def __eq__(self, other):
        if other is not None:
            return self.board == other.board
        else:
            return False

    def get_previous_states(self):
        states = [self]
        prev = self.previous
        while prev is not None:
            states.append(prev)
            prev = prev.previous

        states.reverse()
        return states
