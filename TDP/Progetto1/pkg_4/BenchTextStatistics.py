from TDP.TdP_collections.map.binary_search_tree import TreeMap
from TDP.TdP_collections.map.avl_tree import AVLTreeMap
from TDP.TdP_collections.map.red_black_tree import RedBlackTreeMap
from TDP.Progetto1.pkg_3.TextStatistics import TextStatistics
import time


class BenchBST(TreeMap):

    def __init__(self):
        self._nRotations = 0
        return super().__init__()

    def _rotate(self, p):
        self._nRotations += 1
        return super()._rotate(p)


    def get_statistics(self):
        return {'height':self.height(),'rotations':self._nRotations}

class BenchAVLTree(AVLTreeMap):

    def __init__(self):
        self._nTransformations = 0
        self._nRotations = 0
        return super().__init__()

    def _rotate(self, p):
        self._nRotations += 1

        return super()._rotate(p)

    def _restructure(self, x):
        self._nTransformations += 1
        return super()._restructure(x)

    def get_statistics(self):
        return {'height':self.height(),'rotations': self._nRotations, 'transformations': self._nTransformations}


class BenchRBTree(RedBlackTreeMap):

    def __init__(self):
        self._nRotations = 0
        self._nTransformations = 0
        self._nColor = 0
        return super().__init__()

    def _set_red(self, p):
        self._nColor += 1
        return super()._set_red(p)

    def _set_black(self, p):
        self._nColor += 1
        return super()._set_black(p)

    def _rotate(self, p):
        self._nRotations += 1
        return super()._rotate(p)

    def _restructure(self, x):
        self._nTransformations += 1
        return super()._restructure(x)

    def get_statistics(self):
        return {'height':self.height(),'rotations':self._nRotations, 'transformations': self._nTransformations, 'color_changes': self._nColor}

if __name__ == '__main__':
    performances = dict()
    print("\n\n#################>>BST<<#################")
    start = time.time()
    t = TextStatistics("/Users/CLT/Downloads/AliceNelPaeseDelleMeraviglie.txt", BenchBST())
    stop = time.time()
    performances['BST'] = round(stop-start, 5)
    print("average:\t", t.average())
    print("deviazione standart:\t", t.devStd())
    print("5 parole più frequenti:\t", t.mostFrequent(5))
    print("trasformations:\n", t._words.get_statistics())
    del t

    print("\n\n#################>>AVL<<#################")
    start = time.time()
    t = TextStatistics("/Users/CLT/Downloads/AliceNelPaeseDelleMeraviglie.txt", BenchAVLTree())
    stop = time.time()
    performances['AVL'] = round(stop-start, 5)
    print("num parole:\t",len(t))
    print("average:\t", t.average())
    print("deviazione standart:\t", t.devStd())
    print("5 parole più frequenti:\t", t.mostFrequent(5))
    print("trasformations:\n", t._words.get_statistics())
    del t
    print("\n\n#################>>R-B<<#################")
    t = TextStatistics("/Users/CLT/Downloads/AliceNelPaeseDelleMeraviglie.txt", BenchRBTree())
    stop = time.time()
    performances['RB'] = round(stop-start, 5)
    print("num parole:\t",len(t))
    print("average:\t", t.average())
    print("deviazione standart:\t", t.devStd())
    print("5 parole più frequenti:\t", t.mostFrequent(5))
    print("trasformations:\n", t._words.get_statistics())
    del t

    print(performances)

    performances = dict()
    print("\n\n#################>>BST<<#################")
    start = time.time()
    t = TextStatistics("/Users/CLT/Downloads/MobyDick.txt", BenchBST())
    stop = time.time()
    performances['BST'] = round(stop-start, 5)
    print("average:\t", t.average())
    print("deviazione standart:\t", t.devStd())
    print("5 parole più frequenti:\t", t.mostFrequent(5))
    print("trasformations:\n", t._words.get_statistics())
    del t

    print("\n\n#################>>AVL<<#################")
    start = time.time()
    t = TextStatistics("/Users/CLT/Downloads/MobyDick.txt", BenchAVLTree())
    stop = time.time()
    performances['AVL'] = round(stop-start, 5)
    print("num parole:\t",len(t))
    print("average:\t", t.average())
    print("deviazione standart:\t", t.devStd())
    print("5 parole più frequenti:\t", t.mostFrequent(5))
    print("trasformations:\n", t._words.get_statistics())
    del t
    print("\n\n#################>>R-B<<#################")
    t = TextStatistics("/Users/CLT/Downloads/MobyDick.txt", BenchRBTree())
    stop = time.time()
    performances['RB'] = round(stop-start, 5)
    print("num parole:\t",len(t))
    print("average:\t", t.average())
    print("deviazione standart:\t", t.devStd())
    print("5 parole più frequenti:\t", t.mostFrequent(5))
    print("trasformations:\n", t._words.get_statistics())
    del t

    print(performances)
