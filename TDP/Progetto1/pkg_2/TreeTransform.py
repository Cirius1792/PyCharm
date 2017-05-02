from TDP.TdP_collections.map.binary_search_tree import TreeMap
from TDP.TdP_collections.map.red_black_tree import RedBlackTreeMap
from TDP.Progetto1.pkg_1.TwoDTreeMap import TwoDTreeMap
from TDP.TdP_collections.tree.linked_binary_tree import LinkedBinaryTree
from TDP import util


class TreeTransform(TwoDTreeMap, RedBlackTreeMap):

    # class Position(TwoDTreeMap.Position):
    #
    #     def key(self, j=0):
    #         """Return key of map's key-value pair."""
    #         return self.element()[j]._key
    #
    #     def value(self, j=0):
    #         """Return value of map's key-value pair."""
    #         return self.element()[j]._value

    class _Node(TwoDTreeMap._Node):

        __slots__ = '_red', '_left', '_right'

        def __init__(self, param1=None, parent=None, left=None, right=None):
            if isinstance(param1, int):
                TwoDTreeMap._Node.__init__(self, param1, parent)
            else:
                TwoDTreeMap._Node.__init__(self, 2, parent)
                self.insert_element(param1)
            self._right = None
            self._left = None
            self._red = True  # new node red by default
            if left is not None:
                self._set_left(left)
            if right is not None:
                self._set_right(right)

        def connect_child(self, child_index,child):
            if child_index == 0:
                self._left = child
            elif child_index == 1:
                self._right = child
            super().connect_child( child_index, child)

        def disconnect_child(self, child_index):
            if child_index == 0:
                self._left = None
            elif child_index == 1:
                self._right = None
            super().disconnect_child(child_index)

        def _get_left(self):
            return self._left

        def _get_right(self):
            return self._right

        def _set_left(self, child):
            self.connect_child(0, child)
            self._left = child

        def _set_right(self, child):
            self.connect_child(1, child)
            self._right = child

    __slots__ = "_rb", "_order"

    def __init__(self, rb=True):
        self._rb = rb
        if self._rb:
            RedBlackTreeMap.__init__(self)
            self._order = 2
        else:
            TwoDTreeMap.__init__(self)

    def __delitem__(self, k):
        if self._rb:
           RedBlackTreeMap.__delitem__(self, k)
        else:
            TwoDTreeMap.__delitem__(self, k)

    def __setitem__(self, k, v):
        if self._rb:
            RedBlackTreeMap.__setitem__(self, k, v)
        else:
            TwoDTreeMap.__setitem__(self, k, v)

    def __iter__(self):
        if self._rb:
            return RedBlackTreeMap.__iter__(self)
        else:
            return TwoDTreeMap.__iter__(self)


    def _add_left(self, p, e):
        """Create a new left child for Position p, storing element e.

         Return the Position of new node.
         Raise ValueError if Position p is invalid or p already has a left child.
         """
        node = self._validate(p)
        if node._get_left() is not None:
            raise ValueError('Left child exists')
        self._size += 1
        node._set_left(self._Node(e, node))  # node is its parent
        return self._make_position(node._get_left())

    def _add_right(self, p, e):
        node = self._validate(p)
        if node._get_right() is not None:
            raise ValueError('Left child exists')
        self._size += 1
        node._set_right(self._Node(e, node))  # node is its parent
        return self._make_position(node._get_right())

    def _relink(self, parent, child, make_left_child):
        """Relink parent node with child node (we allow child to be None)."""
        if make_left_child:  # make it a left child
            #parent._left = child
            parent._set_left(child)
        else:  # make it a right child
            #parent._right = child
            parent._set_right(child)
        if child is not None:  # make child point to parent
            child._parent = parent

    # def _subtree_search(self, p, k):
    #     if p._node.find_element(k) or p._node.leftmost_child():
    #         return p
    #     k_min = p._node.get_element(0)._key
    #     k_max = p._node.get_element(p._node._n_elements - 1)._key
    #     if k < k_min:
    #         return self._subtree_search(self.Position(self, p._node.get_child(0)), k)
    #     elif k < k_max:
    #         i = 0
    #         while i < p._node._n_elements - 1:
    #             if k < p._node.get_element(i)._key:
    #                 return self._subtree_search(self.Position(self, p._node.get_child(i)), k)
    #             i += 1
    #     else:
    #         return self._subtree_search(self.Position(self, p._node.get_child(p._node._n_children - 1)), k)


if __name__ == '__main__':

    pTree = TreeTransform()
    dTree = TwoDTreeMap()
    dic = util.rand_dict(100, 1, 100)

    pTree[11] = 1
    pTree[2] = 1
    pTree[14] = 1
    pTree[1] = 1
    pTree[7] = 1
    pTree[15] = 1
    pTree[5] = 1
    pTree[8] = 1
#    for key in dic:
#        pTree[key] = dic.get(key)


    for k in pTree:
        print('key:',k ,' value:',pTree[k])
    print('len:',len(pTree))

