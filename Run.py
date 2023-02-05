from __future__ import print_function
from Algorithms import *
import Board
from Board import *
import time
import os
import sys
import numpy as np


def readFile(fileName):
    state = []
    read = np.loadtxt(fileName, "str").flatten()
    for i in read:
        if i == '_':
            state.append("0")
        else:
            state.append(i)
    state = list(map(int, state))
    return state


def outputBoard(inBoard):
    sBoard = map(str, inBoard)
    board = ""
    count = 0
    for num in sBoard:
        if count % 3 == 0 and count != 0:
            board += '\n'
        if num == '0':
            board += '_ '
        else:
            board += num + ' '
        count += 1
    return board


def isSolvable(board):
    inversion = 0
    for i in range(8):
        for j in range(i + 1, 9):
            if board[i] and board[j] and board[i] > board[j]:
                inversion += 1
    return inversion % 2 == 0


def pathOutput(pathlist, initialBoardState):
    stateOld = initialBoardState
    output = " "

    for path in pathlist:

        if path.board == 'NULL':
            return
        else:
            # pathOutput(stateNew, visited[stateNew][2], visited)
            stateNew = path.board
            s = getMoveDirection(stateNew, stateOld)
            stateOld = stateNew
            if str(s) == "None":
                continue
            output = str(output) + str(s)
    return output


def getMoveDirection(newState, oldState):
    newState = int("".join(map(str, newState)))
    oldState = int("".join(map(str, oldState)))
    for x in range(9):
        if newState % 10 == 0:
            iNew = (8 - x) // 3
            jNew = (8 - x) % 3
        newState = newState // 10

    for x in range(9):
        if oldState % 10 == 0:
            iOld = (8 - x) // 3
            jOld = (8 - x) % 3
        oldState = oldState // 10

    if iNew == iOld - 1:
        return "D"
    elif iNew == iOld + 1:
        return "U"
    elif jNew == jOld - 1:
        return "R"
    elif jNew == jOld + 1:
        return "L"
    else:
        return


def fileMaker(fileName, output, totalTime, algorithm, startBoard):
    fName = fileName.replace("Part2/", "")
    fName = fName.replace(".txt", "")
    fName = fName.replace("Part3/", "")
    fName = fName.replace("L8/", "")
    fName = fName.replace("L15/", "")
    fName = fName.replace("L24/", "")
    fPath = 'Output.txt'
    if not (os.path.isfile(fPath)):
        file = open('Output.txt', 'w')
        file.close()

    totalTimeS = totalTime // 1
    totalTimeMicroS = int(round(((totalTime - totalTimeS) * 1000000), 5) // 1)
    out1 = output[0]
    out2 = output[1]

    file = open('Output.txt', 'a')
    file.write('\n------------------------------' + "\n")
    file.write('\nRunning ' + algorithm + ' on ' + fName + '\n')
    file.write("Total nodes visited: " + str(out1) + "\n")
    file.write("Total time taken: " + str(int(totalTimeS)) + " sec " + str(totalTimeMicroS) + " microsec" + "\n")
    file.write("Path Length: " + str(len(out2.get_previous_states()) - 1) + "\n")
    file.write("Path: " + str((pathOutput(out2.get_previous_states(), startBoard.board))) + "\n")
    file.close()


def fileMakerNotSolvable(initBoard):
    file = open('Output.txt', 'a')
    file.write('\n------------------------------' + '\n')
    file.write("The inputted puzzle is not solvable:" + '\n')
    file.write(outputBoard(initBoard))
    file.close()


def fileMakerTimeOut(filename, algorithm):
    fName = filename.replace("Part2/", "")
    fName = fName.replace(".txt", "")
    fName = fName.replace("Part3/", "")
    fName = fName.replace("L8/", "")
    fName = fName.replace("L15/", "")
    fName = fName.replace("L24/", "")
    fPath = 'Output.txt'
    if not (os.path.isfile(fPath)):
        file = open('Output.txt', 'w')
        file.close()

    file = open('Output.txt', 'a')
    file.write('\n------------------------------' + "\n")
    file.write('\nRunning ' + algorithm + ' on ' + fName + '\n')
    file.write("Total nodes visited: " + "<<?>>" + "\n")
    file.write("Total time taken: " + ">15 min" + "\n")
    file.write("Path Length: " + "Timed out." + "\n")
    file.write("Path: " + "Timed out." + "\n")
    file.close()


def printOutput(output, totalTime, initialBoard):
    totalTimeS = totalTime // 1
    totalTimeMicroS = int(round(((totalTime - totalTimeS) * 1000000), 5) // 1)

    print('\n------------------------------')
    print("Total nodes visited:", output[0])
    print("Total time taken:", int(totalTimeS), " sec ", totalTimeMicroS, " microsec")
    print("Path Length: ", len(output[1].get_previous_states()) - 1)
    print("Path:", (pathOutput(output[1].get_previous_states(), initialBoard.board)))


def start():
    filename = sys.argv[1]
    algorithm = sys.argv[2]
    startState = readFile(filename)

    solvability = isSolvable(startState)
    if not solvability:
        fileMakerNotSolvable(startState)
        return

    initialBoard = Board(startState)
    startTime = time.time()

    if algorithm == "BFS":
        output = BFS(initialBoard, startTime)
    elif algorithm == "IDS":
        output = IDS(initialBoard, startTime)
    elif algorithm == "h1":
        output = h1(initialBoard, startTime)
    elif algorithm == "h2":
        output = h2(initialBoard, startTime)
    elif algorithm == "h3":
        output = h3(initialBoard, startTime)
    else:
        print("Use a valid algorithm: 'BFS', 'IDS', 'h1', 'h2', 'h3'")

    totalTime = time.time() - startTime

    if output == None:
        fileMakerTimeOut(filename, algorithm)
    else:
        fileMaker(filename, output, totalTime, algorithm, initialBoard)


if __name__ == "__main__":
    print("\n")
    start()
