import os

argsExamples = [
    "Examples/S1.txt", "Examples/S2.txt", "Examples/S3.txt", "Examples/S4.txt", "Examples/S5.txt"
    ]

argsExamples2L8 = [
    "Examples2/L8/152.txt", "Examples2/L8/154.txt", "Examples2/L8/158.txt", "Examples2/L8/160.txt", "Examples2/L8/164.txt", "Examples2/L8/193.txt",
    "Examples2/L8/195.txt", "Examples2/L8/198.txt", "Examples2/L8/208.txt", "Examples2/L8/210.txt", "Examples2/L8/224.txt", "Examples2/L8/225.txt",
    "Examples2/L8/234.txt", "Examples2/L8/236.txt", "Examples2/L8/238.txt", "Examples2/L8/239.txt", "Examples2/L8/250.txt", "Examples2/L8/253.txt",
    "Examples2/L8/256.txt", "Examples2/L8/258.txt"
    ]

argsExamples2L15 = [
    "Examples2/L15/4767.txt", "Examples2/L15/4768.txt", "Examples2/L15/4771.txt", "Examples2/L15/4773.txt", "Examples2/L15/4775.txt",
    "Examples2/L15/4778.txt", "Examples2/L15/4780.txt", "Examples2/L15/4784.txt", "Examples2/L15/4789.txt", "Examples2/L15/4793.txt",
    "Examples2/L15/4798.txt", "Examples2/L15/4800.txt", "Examples2/L15/5108.txt", "Examples2/L15/5109.txt", "Examples2/L15/5115.txt",
    "Examples2/L15/5120.txt", "Examples2/L15/5123.txt", "Examples2/L15/5126.txt", "Examples2/L15/5127.txt", "Examples2/L15/5130.txt"
    ]

argsExamples2L24 = [
    "Examples2/L24/131248.txt", "Examples2/L24/131256.txt", "Examples2/L24/131264.txt", "Examples2/L24/131271.txt", "Examples2/L24/131274.txt",
    "Examples2/L24/131279.txt", "Examples2/L24/131286.txt", "Examples2/L24/131304.txt", "Examples2/L24/131311.txt", "Examples2/L24/131324.txt",
    "Examples2/L24/131345.txt", "Examples2/L24/131370.txt", "Examples2/L24/131374.txt", "Examples2/L24/131378.txt", "Examples2/L24/131394.txt",
    "Examples2/L24/131400.txt", "Examples2/L24/131406.txt", "Examples2/L24/131425.txt", "Examples2/L24/131449.txt", "Examples2/L24/131455.txt"
    ]

#Part 2
for arg in argsExamples:
    print("_____________Processing_" + arg + "____________")
    os.system("python Run.py {} BFS".format(arg))
    print("     >BFS Complete")
    os.system("python Run.py {} IDS".format(arg))
    print("     >IDS Complete")
    os.system("python Run.py {} h1".format(arg))
    print("     >h1(Tiles) Complete")
    os.system("python Run.py {} h2".format(arg))
    print("     >h2(Manhattan) Complete")
    os.system("python Run.py {} h3".format(arg))
    print("     >h3(Euclidian) Complete")


#PART 3 L8
for arg in argsExamples2L8:
    print("_____________Processing_" + arg + "____________")
    os.system("python Run.py {} BFS".format(arg))
    print("     >BFS Complete")

for arg in argsExamples2L8:
    print("_____________Processing_" + arg + "____________")
    os.system("python Run.py {} IDS".format(arg))
    print("     >IDS Complete")

for arg in argsExamples2L8:
    print("_____________Processing_" + arg + "____________")
    os.system("python Run.py {} h1".format(arg))
    print("     >h1 Complete")

for arg in argsExamples2L8:
    print("_____________Processing_" + arg + "____________")
    os.system("python Run.py {} h2".format(arg))
    print("     >h2 Complete")

for arg in argsExamples2L8:
    print("_____________Processing_" + arg + "____________")
    os.system("python Run.py {} h3".format(arg))
    print("     >h3 Complete")


#PART 3 L15
for arg in argsExamples2L15:
    print("_____________Processing_" + arg + "____________")
    os.system("python Run.py {} BFS".format(arg))
    print("     >BFS Complete")

for arg in argsExamples2L15:
    print("_____________Processing_" + arg + "____________")
    os.system("python Run.py {} IDS".format(arg))
    print("     >IDS Complete")

for arg in argsExamples2L15:
    print("_____________Processing_" + arg + "____________")
    os.system("python Run.py {} h1".format(arg))
    print("     >h1 Complete")

for arg in argsExamples2L15:
    print("_____________Processing_" + arg + "____________")
    os.system("python Run.py {} h2".format(arg))
    print("     >h2 Complete")

for arg in argsExamples2L15:
    print("_____________Processing_" + arg + "____________")
    os.system("python Run.py {} h3".format(arg))
    print("     >h3 Complete")


#PART 3 L24
for arg in argsExamples2L24:
    print("_____________Processing_" + arg + "____________")
    os.system("python Run.py {} BFS".format(arg))
    print("     >BFS Complete")

for arg in argsExamples2L24:
    print("_____________Processing_" + arg + "____________")
    os.system("python Run.py {} IDS".format(arg))
    print("     >IDS Complete")

for arg in argsExamples2L24:
    print("_____________Processing_" + arg + "____________")
    os.system("python Run.py {} h1".format(arg))
    print("     >h1 Complete")

for arg in argsExamples2L24:
    print("_____________Processing_" + arg + "____________")
    os.system("python Run.py {} h2".format(arg))
    print("     >h2 Complete")

for arg in argsExamples2L24:
    print("_____________Processing_" + arg + "____________")
    os.system("python Run.py {} h3".format(arg))
    print("     >h3 Complete")





