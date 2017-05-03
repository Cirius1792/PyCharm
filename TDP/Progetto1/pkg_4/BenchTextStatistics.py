from TDP.Progetto1.TdP_collections.map.binary_search_tree import TreeMap
from TDP.Progetto1.TdP_collections.map.avl_tree import AVLTreeMap
from TDP.Progetto1.TdP_collections.map.red_black_tree import RedBlackTreeMap



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

