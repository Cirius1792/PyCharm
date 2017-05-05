from TDP import util
from TDP.Progetto1.pkg_3.TextStatistics import TextStatistics
from TDP.Progetto1.TdP_collections.map.avl_tree import AVLTreeMap

if __name__ == '__main__':

    PATH_ALICE = "AliceNelPaeseDelleMeraviglie.txt"
    PATH_MOBI = "MobyDick.txt"

    print("\n\n#################>>TextStatistics<<#################")
    print("###################>>Moby Dick<<####################")

    t = TextStatistics(PATH_MOBI, AVLTreeMap())
    print("nume parole:\t", len(t))
    print("average:\t", t.average())
    print("deviazione standart:\t", t.devStd())
    print("primo quartile:\t\t", t.quartile(1))
    print("secondo quartile:\t\t", t.quartile(2))
    print("terzo quartile:\t\t", t.quartile(3))
    print("5 parole più frequenti:")
    mostFrequent = t.mostFrequent(5)
    for k in range(0, len(mostFrequent)):
        print('parola:\t\t', mostFrequent[k][t.WORD], '\toccorrenze:\t\t', mostFrequent[k][t.OCCURRENCES])

    del t
    print("\n\n########>>Alice Nel Paese Delle Meraviglie<<########")
    t = TextStatistics(PATH_ALICE, AVLTreeMap())
    print("nume parole:\t", len(t))
    print("average:\t", t.average())
    print("deviazione standart:\t", t.devStd())
    print("primo quartile:\t\t", t.quartile(1))
    print("secondo quartile:\t\t", t.quartile(2))
    print("terzo quartile:\t\t", t.quartile(3))
    print("5 parole più frequenti:")
    mostFrequent = t.mostFrequent(5)
    for k in range(0, len(mostFrequent)):
        print('parola:\t\t', mostFrequent[k][t.WORD], '\toccorrenze:\t\t', mostFrequent[k][t.OCCURRENCES])
    del t
