from TdP_collections.map.avl_tree import AVLTreeMap
from TdP_collections.map.binary_search_tree import TreeMap

class AVLTreeMapHW (AVLTreeMap):

    def at_index(self, i):
        j = 0
        tmp = None
        for e in self:
            if j > i:
                break
            j += 1
            tmp = e
        return tmp

    def index_of(self, p):
        j = 0
        i = self.first()
        while i is not None and i != p:
            i = self.after(i)
            j += 1
        return j


class MyTreeMap (TreeMap):

    class _Node:
        """Lightweight, nonpublic class for storing a node."""
        __slots__ = '_element', '_parent', '_left', '_right', '_rsons', '_lsons'  # streamline memory usage

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
            self._rsons = 0
            self._lsons = 0

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        if self.is_empty():
            leaf = self._add_root(self._Item(k, v))  # from LinkedBinaryTree
        else:
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                p.element()._value = v  # replace existing item's value
                self._rebalance_access(p)  # hook for balanced tree subclasses
                return
            else:
                item = self._Item(k, v)
                if p.key() < k:
                    leaf = self._add_right(p, item)  # inherited from LinkedBinaryTree
                else:
                    leaf = self._add_left(p, item)  # inherited from LinkedBinaryTree
                self._increase_sons(k)
        self._rebalance_insert(leaf)  # hook for balanced tree subclasses

    def _increase_sons(self, target_k):
        p = self.root()
        while p.key() != target_k:
            if target_k < p.key():
                p._node._lsons += 1
                p = self.left(p)
            elif target_k > p.key():
                p._node._rsons += 1
                p = self.right(p)

    def _decrease_sons(self, target_k):
        p = self.root()
        while p.key() != target_k:
            if target_k < p.key():
                p._node._lsons -= 1
                p = self.left(p)
            elif target_k > p.key():
                p._node._rsons -= 1
                p = self.right(p)

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            if k == p.key():
                self.delete(p)  # rely on positional version
                return  # successful deletion complete
            self._rebalance_access(p)  # hook for balanced tree subclasses
            self._decrease_sons(k)
        raise KeyError('Key Error: ' + repr(k))

    def at_index(self, i):
        p = self.root()
        while p is not None:
            if p._node._lsons == i:
                return p
            elif p._node._lsons > i:
                p = self.left(p)
            else:
                p = self.right(p)
        return None

    def index_of(self, p):
        pass

def test():
    b = MyTreeMap()

    b[10] = 12
    b[5] = 12
    b[14] = 12
    b[3] = 12
    b[90] = 12

    print('at_index(3)' + str(b.at_index(3).key()))

test()

