from TDP.TdP_collections.map.binary_search_tree import TreeMap
from TDP.TdP_collections.map.avl_tree import AVLTreeMap
from TDP.TdP_collections.map.red_black_tree import RedBlackTreeMap
from TDP.Progetto1.pkg_3.TextStatistics import TextStatistics


class TextStatisticsBST(TextStatistics):

    def _factory(self):
        self.words = BenchBST()

    def getTransformations(self):
        return self.words._nRotations

class TextStatisticsAVL(TextStatistics):

    def _factory(self):
        self.words = BenchAVLTree()

    def getTransformations(self):
        return self.words._nTransformations

class TextStatisticsRB(TextStatistics):

    def _factory(self):
        self.words = BenchRBTree()

    def getTransformations(self):

        return {'rotations':self.words._nRotations, 'transformations':self.words._nTransformations}

class BenchBST(TreeMap):

    def __init__(self):
        self._nRotations = 0
        return super().__init__()

    def _rotate(self, p):
        self._nRotations += 1
        return super()._rotate(p)

class BenchAVLTree(AVLTreeMap):

    def __init__(self):
        self._nTransformations = 0
        return super().__init__()

    def _restructure(self, x):
        self._nTransformations += 1
        return super()._restructure(x)

class BenchRBTree(RedBlackTreeMap):

    def __init__(self):
        self._nRotations = 0
        self._nTransformations = 0
        self._nRecolorations = 0
        return super().__init__()

    def _rotate(self, p):
        self._nRotations += 1
        return super()._rotate(p)

    def _restructure(self, x):
        self._nTransformations += 1
        return super()._restructure(x)




print("#################>>BST<<#################")
t = TextStatisticsBST("/Users/CLT/Desktop/Text-2.txt")
print("average:\t", t.average())
print("deviazione standart:\t", t.devStd())
print("5 parole più frequenti:\t", t.mostFrequent(5))
print("numero rotazioni:\t", t.getTransformations())
del t

print("#################>>AVL<<#################")
t = TextStatisticsAVL("/Users/CLT/Desktop/Text-2.txt")
print("num parole:\t",len(t))
print("average:\t", t.average())
print("deviazione standart:\t", t.devStd())
print("5 parole più frequenti:\t", t.mostFrequent(5))
print("numero trasformazioni:\t", t.getTransformations())
del t
print("#################>>R-B<<#################")
t = TextStatisticsRB("/Users/CLT/Desktop/Text-2.txt")
print("num parole:\t",len(t))
print("average:\t", t.average())
print("deviazione standart:\t", t.devStd())
print("5 parole più frequenti:\t", t.mostFrequent(5))
print("numero trasformazioni:\t", t.getTransformations())
del t
