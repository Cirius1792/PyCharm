from TDP.Progetto1.TdP_collections.map.binary_search_tree import TreeMap
from TDP.Progetto1.TdP_collections.map.avl_tree import AVLTreeMap
from TDP.Progetto1.TdP_collections.map.red_black_tree import RedBlackTreeMap
from TDP.Progetto1.pkg_1.TwoDTreeMap import TwoDTreeMap



class BenchBST(TreeMap):
    """Classe creata ad hoc per la raccolta di statistiche sulle trasformazioni effettuate
    della classe padre"""
    __slots__ = '_nRotations'

    def __init__(self):
        self._nRotations = 0
        return super().__init__()

    def _rotate(self, p):
        self._nRotations += 1
        return super()._rotate(p)

    """Metodo utilizzato per la restituizione delle statistiche raccolte durante le operazioni svolte
    sulla struttura dati. Il valore di ritorno è composto da un dizionario contenente le informazioni 
    di interesse"""
    def get_statistics(self):
        return {'height':self.height(),'rotations':self._nRotations}

class BenchAVLTree(AVLTreeMap):
    """Classe creata ad hoc per la raccolta di statistiche sulle trasformazioni effettuate
    della classe padre"""
    __slots__ = '_nRotations', '_nTransformations'

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

    """Metodo utilizzato per la restituizione delle statistiche raccolte durante le operazioni svolte
    sulla struttura dati. Il valore di ritorno è composto da un dizionario contenente le informazioni 
    di interesse"""
    def get_statistics(self):
        return {'height':self.height(),'rotations': self._nRotations, 'transformations': self._nTransformations}


class BenchRBTree(RedBlackTreeMap):
    """Classe creata ad hoc per la raccolta di statistiche sulle trasformazioni effettuate
    della classe padre"""
    __slots__ = '_nRotations', '_nTransformations', '_nColor'

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

    """Metodo utilizzato per la restituizione delle statistiche raccolte durante le operazioni svolte
    sulla struttura dati. Il valore di ritorno è composto da un dizionario contenente le informazioni 
    di interesse"""
    def get_statistics(self):
        return {'height': self.height(), 'rotations': self._nRotations, 'transformations': self._nTransformations, 'color_changes': self._nColor}


class BenchTwoDTreeMap(TwoDTreeMap):
    """Classe creata ad hoc per la raccolta di statistiche sulle trasformazioni effettuate
    della classe padre"""

    __slots__ = '_split', '_fusion', '_transfer'

    def __init__(self, order=None):
        self._fusion = 0
        self._transfer = 0
        self._split = 0
        super().__init__(order)

    def fusion(self, p, sibling, p_index, flag):
        self._fusion += 1
        super(TwoDTreeMap, self).fusion(p, sibling, p_index, flag)

    def transfer(self, p, sibling, p_index, flag):
        self._transfer += 1
        super(TwoDTreeMap, self).transfer(p, sibling, p_index, flag)


    def split(self, p):
        self._split += 1
        super().split(p)


    """Metodo utilizzato per la restituizione delle statistiche raccolte durante le operazioni svolte
    sulla struttura dati. Il valore di ritorno è composto da un dizionario contenente le informazioni 
    di interesse"""
    def get_statistics(self):
        return {'height': self.height(),'split':self._split, 'fusion': self._fusion, 'transfer': self._transfer}

