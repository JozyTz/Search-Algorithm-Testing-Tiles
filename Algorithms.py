import itertools
import time
from collections import deque
from queue import PriorityQueue

nodesVisited = 0


# Breadth First Search
def BFS(initialState, startTime):
    global nodesVisited

    queue = deque([initialState])
    explored = set()

    while len(queue) > 0:
        if time.time() > startTime + 60 * 15:
            return None
        node = queue.popleft()
        explored.add(node.map)
        nodesVisited += 1
        if node.checkGoal():
            goal = [node]
            return nodesVisited, goal[0]
        for neighbor in node.neighbors():
            if neighbor.map not in explored:
                queue.append(neighbor)
    return None


#Iterative Deepening DFS
def dls(initialState, limit, startTime):
    global nodesVisited
    nodesVisited += 1

    if initialState.checkGoal():
        goal = [initialState]
        return goal
    if time.time() > startTime + 60 * 15:
        return "None"
    if limit <= 0:
        return None
    for neighbor in initialState.neighbors():
        next = dls(neighbor, limit - 1, startTime)
        if next:
            return next
    return None

def IDS(initialState, startTime):
    global nodesVisited
    maxDepth = 99999999
    for i in range(maxDepth):
        output = dls(initialState, i, startTime)
        if type(output) is list:
            return nodesVisited, output[0]
        if output == "None":
            return None


# A* Misplaced Tiles
def h1(initialState, startTime):
    nodesVisited = 0

    queue = PriorityQueue()
    queue.put(initialState.toPQMisplacedTiles(0))
    i = 1
    while not queue.empty():
        if time.time() > startTime + 60 * 15:
            return None
        board = queue.get()[2]
        nodesVisited = nodesVisited + 1
        if not board.checkGoal():
            for neighbor in board.neighbors():
                if neighbor != board.previous:
                    queue.put(neighbor.toPQMisplacedTiles(i))
                    i += 1
        else:
            return nodesVisited, board

    return nodesVisited, board


# A* Manhattan
def h2(initialState, startTime):
    nodesVisited = 0

    queue = PriorityQueue()
    queue.put(initialState.toPQManhattan(0))
    i = 1
    while not queue.empty():
        if time.time() > startTime + 60 * 15:
            return None
        board = queue.get()[2]
        nodesVisited = nodesVisited + 1
        if not board.checkGoal():
            for neighbor in board.neighbors():
                if neighbor != board.previous:
                    queue.put(neighbor.toPQManhattan(i))
                    i += 1
        else:
            return nodesVisited, board

    return nodesVisited, board


# A* Euclidian
def h3(initialState, startTime):
    nodesVisited = 0

    queue = PriorityQueue()
    queue.put(initialState.toPQEuclidian(0))
    i = 1
    while not queue.empty():
        if time.time() > startTime + 60 * 15:
            return None
        board = queue.get()[2]
        nodesVisited = nodesVisited + 1
        if not board.checkGoal():
            for neighbor in board.neighbors():
                if neighbor != board.previous:
                    queue.put(neighbor.toPQEuclidian(i))
                    i += 1
        else:
            return nodesVisited, board

    return nodesVisited, board
