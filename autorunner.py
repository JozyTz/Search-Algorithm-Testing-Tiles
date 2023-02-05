import os

argsPart2 = [
    "Examples/S1.txt", "Examples/S2.txt", "Examples/S3.txt", "Examples/S4.txt", "Examples/S5.txt"
    ]

argsPart3L8 = [
    "Part3/L8/152.txt", "Part3/L8/154.txt", "Part3/L8/158.txt", "Part3/L8/160.txt", "Part3/L8/164.txt", "Part3/L8/193.txt",
    "Part3/L8/195.txt", "Part3/L8/198.txt", "Part3/L8/208.txt", "Part3/L8/210.txt", "Part3/L8/224.txt", "Part3/L8/225.txt",
    "Part3/L8/234.txt", "Part3/L8/236.txt", "Part3/L8/238.txt", "Part3/L8/239.txt", "Part3/L8/250.txt", "Part3/L8/253.txt",
    "Part3/L8/256.txt", "Part3/L8/258.txt"
    ]

argsPart3L15 = [
    "Part3/L15/4767.txt", "Part3/L15/4768.txt", "Part3/L15/4771.txt", "Part3/L15/4773.txt", "Part3/L15/4775.txt",
    "Part3/L15/4778.txt", "Part3/L15/4780.txt", "Part3/L15/4784.txt", "Part3/L15/4789.txt", "Part3/L15/4793.txt",
    "Part3/L15/4798.txt", "Part3/L15/4800.txt", "Part3/L15/5108.txt", "Part3/L15/5109.txt", "Part3/L15/5115.txt",
    "Part3/L15/5120.txt", "Part3/L15/5123.txt", "Part3/L15/5126.txt", "Part3/L15/5127.txt", "Part3/L15/5130.txt"
    ]

argsPart3L24 = [
    "Part3/L24/131248.txt", "Part3/L24/131256.txt", "Part3/L24/131264.txt", "Part3/L24/131271.txt", "Part3/L24/131274.txt",
    "Part3/L24/131279.txt", "Part3/L24/131286.txt", "Part3/L24/131304.txt", "Part3/L24/131311.txt", "Part3/L24/131324.txt",
    "Part3/L24/131345.txt", "Part3/L24/131370.txt", "Part3/L24/131374.txt", "Part3/L24/131378.txt", "Part3/L24/131394.txt",
    "Part3/L24/131400.txt", "Part3/L24/131406.txt", "Part3/L24/131425.txt", "Part3/L24/131449.txt", "Part3/L24/131455.txt"
    ]

#Part 2
for arg in argsPart2:
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
for arg in argsPart3L8:
    print("_____________Processing_" + arg + "____________")
    os.system("python Run.py {} BFS".format(arg))
    print("     >BFS Complete")

for arg in argsPart3L8:
    print("_____________Processing_" + arg + "____________")
    os.system("python Run.py {} IDS".format(arg))
    print("     >IDS Complete")

for arg in argsPart3L8:
    print("_____________Processing_" + arg + "____________")
    os.system("python Run.py {} h1".format(arg))
    print("     >h1 Complete")

for arg in argsPart3L8:
    print("_____________Processing_" + arg + "____________")
    os.system("python Run.py {} h2".format(arg))
    print("     >h2 Complete")

for arg in argsPart3L8:
    print("_____________Processing_" + arg + "____________")
    os.system("python Run.py {} h3".format(arg))
    print("     >h3 Complete")


#PART 3 L15
for arg in argsPart3L15:
    print("_____________Processing_" + arg + "____________")
    os.system("python Run.py {} BFS".format(arg))
    print("     >BFS Complete")

for arg in argsPart3L15:
    print("_____________Processing_" + arg + "____________")
    os.system("python Run.py {} IDS".format(arg))
    print("     >IDS Complete")

for arg in argsPart3L15:
    print("_____________Processing_" + arg + "____________")
    os.system("python Run.py {} h1".format(arg))
    print("     >h1 Complete")

for arg in argsPart3L15:
    print("_____________Processing_" + arg + "____________")
    os.system("python Run.py {} h2".format(arg))
    print("     >h2 Complete")

for arg in argsPart3L15:
    print("_____________Processing_" + arg + "____________")
    os.system("python Run.py {} h3".format(arg))
    print("     >h3 Complete")


#PART 3 L24
for arg in argsPart3L24:
    print("_____________Processing_" + arg + "____________")
    os.system("python Run.py {} BFS".format(arg))
    print("     >BFS Complete")

for arg in argsPart3L24:
    print("_____________Processing_" + arg + "____________")
    os.system("python Run.py {} IDS".format(arg))
    print("     >IDS Complete")

for arg in argsPart3L24:
    print("_____________Processing_" + arg + "____________")
    os.system("python Run.py {} h1".format(arg))
    print("     >h1 Complete")

for arg in argsPart3L24:
    print("_____________Processing_" + arg + "____________")
    os.system("python Run.py {} h2".format(arg))
    print("     >h2 Complete")

for arg in argsPart3L24:
    print("_____________Processing_" + arg + "____________")
    os.system("python Run.py {} h3".format(arg))
    print("     >h3 Complete")





