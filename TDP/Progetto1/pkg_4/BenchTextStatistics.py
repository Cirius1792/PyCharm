from TDP.TdP_collections.map.binary_search_tree import TreeMap
from TDP.TdP_collections.map.avl_tree import AVLTreeMap
from TDP.TdP_collections.map.red_black_tree import RedBlackTreeMap
from TDP.Progetto1.pkg_3.TextStatistics import TextStatistics

class TextStatisticsAVL(TextStatistics):

    def _factory(self):
        self.words = BenchAVLTree()


class BenchAVLTree(AVLTreeMap):

    rebalancingOp = 0

    def _rebalance(self, p):
        self.rebalancingOp += 1
        super()._rebalance(p)


class TextStatisticsRB(TextStatistics):

    def _factory(self):
        self.words = RedBlackTreeMap()




# print("#################>>BST<<#################")
# t = TextStatistics("C:\\Users\CiroLucio\Desktop\\test2.txt")
# print("average:\t", t.average())
# print("deviazione standart:\t", t.devStd())
# print("5 parole più frequenti:\t", t.mostFrequent(5))

print("#################>>AVL<<#################")
t = TextStatisticsAVL("C:\\Users\CiroLucio\Desktop\\test2.txt")
print("average:\t", t.average())
print("deviazione standart:\t", t.devStd())
print("5 parole più frequenti:\t", t.mostFrequent(5))
print("ribilanciamenti:\t",t.words.rebalancingOp)

print("#################>>R-B<<#################")