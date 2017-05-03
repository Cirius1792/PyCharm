from TDP.Progetto1.pkg_4.BenchTextStatistics import *
from TDP.Progetto1.pkg_3.TextStatistics import TextStatistics
from TDP.Progetto1.pkg_1.TwoDTreeMap import TwoDTreeMap
import time

BST = 'BST'
RB = 'RB'
AVL = 'AVL'
TFT = 'TFT'


if __name__ == '__main__':


    PATH_ALICE = "AliceNelPaeseDelleMeraviglie.txt"
    PATH_MOBI = "MobyDick.txt"

    performances = dict()
    # print("\n\n#################>>BST<<#################")
    # start = time.time()
    # t = TextStatistics(PATH_ALICE, BenchBST())
    # stop = time.time()
    # performances[BST] = round(stop-start, 5)
    # print("average:\t", t.average())
    # print("deviazione standart:\t", t.devStd())
    # print("5 parole più frequenti:\t", t.mostFrequent(5))
    # print("trasformations:\n", t._words.get_statistics())
    # del t
    #
    # print("\n\n#################>>AVL<<#################")
    # start = time.time()
    # t = TextStatistics(PATH_ALICE, BenchAVLTree())
    # stop = time.time()
    # performances[AVL] = round(stop-start, 5)
    # print("num parole:\t",len(t))
    # print("average:\t", t.average())
    # print("deviazione standart:\t", t.devStd())
    # print("5 parole più frequenti:\t", t.mostFrequent(5))
    # print("trasformations:\n", t._words.get_statistics())
    # del t
    # print("\n\n#################>>R-B<<#################")
    # t = TextStatistics(PATH_ALICE, BenchRBTree())
    # stop = time.time()
    # performances[RB] = round(stop-start, 5)
    # print("num parole:\t",len(t))
    # print("average:\t", t.average())
    # print("deviazione standart:\t", t.devStd())
    # print("5 parole più frequenti:\t", t.mostFrequent(5))
    # print("trasformations:\n", t._words.get_statistics())
    # del t

    print("\n\n#################>>24T<<#################")
    start = time.time()
    tree = TwoDTreeMap()
    flag = isinstance(tree, TreeMap)
    #t = TextStatistics(PATH_ALICE, TwoDTreeMap())
    t = TextStatistics(PATH_ALICE, TwoDTreeMap())
    stop = time.time()
    performances[TFT] = round(stop-start, 5)
    print("average:\t", t.average())
    print("deviazione standart:\t", t.devStd())
    print("5 parole più frequenti:\t", t.mostFrequent(5))
    print("trasformations:\n", t._words.get_statistics())
    del t
    print(performances)

    performances = dict()
    print("\n\n#################>>BST<<#################")
    start = time.time()
    t = TextStatistics(PATH_MOBI, BenchBST())
    stop = time.time()
    performances[BST] = round(stop-start, 5)
    print("average:\t", t.average())
    print("deviazione standart:\t", t.devStd())
    print("5 parole più frequenti:\t", t.mostFrequent(5))
    print("trasformations:\n", t._words.get_statistics())
    del t

    print("\n\n#################>>AVL<<#################")
    start = time.time()
    t = TextStatistics(PATH_MOBI, BenchAVLTree())
    stop = time.time()
    performances[AVL] = round(stop-start, 5)
    print("num parole:\t",len(t))
    print("average:\t", t.average())
    print("deviazione standart:\t", t.devStd())
    print("5 parole più frequenti:\t", t.mostFrequent(5))
    print("trasformations:\n", t._words.get_statistics())
    del t
    print("\n\n#################>>R-B<<#################")
    t = TextStatistics(PATH_MOBI, BenchRBTree())
    stop = time.time()
    performances[RB] = round(stop-start, 5)
    print("num parole:\t",len(t))
    print("average:\t", t.average())
    print("deviazione standart:\t", t.devStd())
    print("5 parole più frequenti:\t", t.mostFrequent(5))
    print("trasformations:\n", t._words.get_statistics())
    del t

    print("\n\n#################>>24T<<#################")
    start = time.time()
    t = TextStatistics(PATH_MOBI, TwoDTreeMap())
    stop = time.time()
    performances[TFT] = round(stop-start, 5)
    print("average:\t", t.average())
    print("deviazione standart:\t", t.devStd())
    print("5 parole più frequenti:\t", t.mostFrequent(5))
    print("trasformations:\n", t._words.get_statistics())
    del t
    print(performances)
