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

    constructionTime = dict()
    mostFrequentTime = dict()
    devStdTime = dict()
    print("\n\n########>>Alice Nel Paese Delle Meraviglie<<########")
    print("#################>>BST<<#################")
    start = time.time()
    t = TextStatistics(PATH_ALICE, BenchBST())
    stop = time.time()
    constructionTime[BST] = round(stop - start, 5)
    print("nume parole:\t", len(t))
    print("average:\t", t.average())
    print("deviazione standart:\t", t.devStd())
    start = time.time()
    mostFrequent = t.mostFrequent(5)
    stop = time.time()
    mostFrequentTime[BST] = round(stop - start, 5)
    for k in range(0, len(mostFrequent)):
        print('parola:\t\t', mostFrequent[k][t.WORD], '\toccorrenze:\t\t', mostFrequent[k][t.OCCURRENCES])
    print("trasformations:\n", t._words.get_statistics())
    del t

    print("\n\n#################>>AVL<<#################")
    start = time.time()
    t = TextStatistics(PATH_ALICE, BenchAVLTree())
    stop = time.time()
    constructionTime[AVL] = round(stop - start, 5)
    print("num parole:\t",len(t))
    print("average:\t", t.average())
    print("deviazione standart:\t", t.devStd())
    start = time.time()
    mostFrequent = t.mostFrequent(5)
    stop = time.time()
    mostFrequentTime[AVL] = round(stop - start, 5)
    for k in range(0, len(mostFrequent)):
        print('parola:\t\t', mostFrequent[k][t.WORD], '\toccorrenze:\t\t', mostFrequent[k][t.OCCURRENCES])
    print("trasformations:\n", t._words.get_statistics())
    del t
    print("\n\n#################>>R-B<<#################")
    t = TextStatistics(PATH_ALICE, BenchRBTree())
    stop = time.time()
    constructionTime[RB] = round(stop - start, 5)
    print("num parole:\t",len(t))
    print("average:\t", t.average())
    print("deviazione standart:\t", t.devStd())
    start = time.time()
    mostFrequent = t.mostFrequent(5)
    stop = time.time()
    mostFrequentTime[RB] = round(stop - start, 5)
    for k in range(0, len(mostFrequent)):
        print('parola:\t\t', mostFrequent[k][t.WORD], '\toccorrenze:\t\t', mostFrequent[k][t.OCCURRENCES])
    print("trasformations:\n", t._words.get_statistics())
    del t

    print("\n\n#################>>24T<<#################")
    start = time.time()
    tree = TwoDTreeMap()
    t = TextStatistics(PATH_ALICE, BenchTwoDTreeMap())
    stop = time.time()
    constructionTime[TFT] = round(stop - start, 5)
    print("nume parole:\t", len(t))
    print("average:\t", t.average())
    print("deviazione standart:\t", t.devStd())
    start = time.time()
    mostFrequent = t.mostFrequent(5)
    stop = time.time()
    mostFrequentTime[TFT] = round(stop - start, 5)
    for k in range(0, len(mostFrequent)):
        print('parola:\t\t', mostFrequent[k][t.WORD], '\toccorrenze:\t\t', mostFrequent[k][t.OCCURRENCES])
    print("trasformations:\n", t._words.get_statistics())

    del t
    print("Tempo impiegato dal costruttore:")
    print(constructionTime)
    print("Tempo impiegato per le j parle più frequenti:")
    print(mostFrequentTime)

    constructionTime = dict()
    mostFrequentTime = dict()
    print("\n\n#################>>Moby Dick<<#################")
    print("#################>>BST<<#################")
    start = time.time()
    t = TextStatistics(PATH_MOBI, BenchBST())
    stop = time.time()
    constructionTime[BST] = round(stop - start, 5)
    print("nume parole:\t", len(t))
    print("average:\t", t.average())
    print("deviazione standart:\t", t.devStd())
    start = time.time()
    mostFrequent = t.mostFrequent(5)
    stop = time.time()
    mostFrequentTime[BST] = round(stop - start, 5)
    for k in range(0, len(mostFrequent)):
        print('parola:\t\t', mostFrequent[k][t.WORD], '\toccorrenze:\t\t', mostFrequent[k][t.OCCURRENCES])
    print("trasformations:\n", t._words.get_statistics())
    del t

    print("\n\n#################>>AVL<<#################")
    start = time.time()
    t = TextStatistics(PATH_MOBI, BenchAVLTree())
    stop = time.time()
    constructionTime[AVL] = round(stop - start, 5)
    print("num parole:\t",len(t))
    print("average:\t", t.average())
    print("deviazione standart:\t", t.devStd())
    start = time.time()
    mostFrequent = t.mostFrequent(5)
    stop = time.time()
    mostFrequentTime[AVL] = round(stop - start, 5)
    for k in range(0, len(mostFrequent)):
        print('parola:\t\t', mostFrequent[k][t.WORD], '\toccorrenze:\t\t', mostFrequent[k][t.OCCURRENCES])
    print("trasformations:\n", t._words.get_statistics())
    del t
    print("\n\n#################>>R-B<<#################")
    t = TextStatistics(PATH_MOBI, BenchRBTree())
    stop = time.time()
    constructionTime[RB] = round(stop - start, 5)
    print("num parole:\t",len(t))
    print("average:\t", t.average())
    print("deviazione standart:\t", t.devStd())
    start = time.time()
    mostFrequent = t.mostFrequent(5)
    stop = time.time()
    mostFrequentTime[RB] = round(stop - start, 5)
    for k in range(0, len(mostFrequent)):
        print('parola:\t\t', mostFrequent[k][t.WORD], '\toccorrenze:\t\t', mostFrequent[k][t.OCCURRENCES])
    print("trasformations:\n", t._words.get_statistics())
    del t

    print("\n\n#################>>24T<<#################")
    start = time.time()
    t = TextStatistics(PATH_MOBI, BenchTwoDTreeMap())
    stop = time.time()
    constructionTime[TFT] = round(stop - start, 5)
    print("nume parole:\t", len(t))
    print("average:\t", t.average())
    print("deviazione standart:\t", t.devStd())
    start = time.time()
    mostFrequent = t.mostFrequent(5)
    stop = time.time()
    mostFrequentTime[TFT] = round(stop - start, 5)
    for k in range(0, len(mostFrequent)):
        print('parola:\t\t', mostFrequent[k][t.WORD], '\toccorrenze:\t\t', mostFrequent[k][t.OCCURRENCES])
    print("trasformations:\n", t._words.get_statistics())

    del t
    print("Tempo impiegato dal costruttore:")
    print(constructionTime)
    print("Tempo impiegato per le j parle più frequenti:")
    print(mostFrequentTime)

