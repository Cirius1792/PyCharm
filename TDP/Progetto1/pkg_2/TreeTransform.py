from TDP.Progetto1.TdP_collections.map.red_black_tree import RedBlackTreeMap
from TDP.Progetto1.pkg_1.TwoDTreeMap import TwoDTreeMap


class TreeTransform(RedBlackTreeMap, TwoDTreeMap):

    class Position(TwoDTreeMap.Position):
        """An abstraction representing the location of a single element."""

        def element(self):
            """Return the element stored at this Position."""
            if isinstance(self._node, RedBlackTreeMap._Node):
                return self._node._element
            else:
                return self._node.get_element(self._elem_index)

    __slots__ = '_rb'

    def __init__(self, rb=True):
        self._rb = rb
        if rb:
            RedBlackTreeMap.__init__(self)
        else:
            TwoDTreeMap.__init__(self)

    def __setitem__(self, k, v):
        return RedBlackTreeMap.__setitem__(self, k, v) if self._rb else TwoDTreeMap.__setitem__(self, k, v)

    def children(self, p):
        return RedBlackTreeMap.children(self, p) if self._rb else TwoDTreeMap.children(self, p)

    def after(self, p):
        return RedBlackTreeMap.after(self, p) if self._rb else TwoDTreeMap.after(self, p)

    def num_children(self, p):
        return RedBlackTreeMap.num_children(self, p) if self._rb else TwoDTreeMap.num_children(self, p)

    def left(self, p):
        return RedBlackTreeMap.left(self, p) if self._rb else TwoDTreeMap.left(self, p)

    def delete(self, p):
        return RedBlackTreeMap.delete(self, p) if self._rb else TwoDTreeMap.delete(self, p)

    def right(self, p):
        return RedBlackTreeMap.right(self, p) if self._rb else TwoDTreeMap.right(self, p)

    def _subtree_search(self, p, k):
        return RedBlackTreeMap._subtree_search(self, p, k) if self._rb else TwoDTreeMap._subtree_search(self, p, k)

    def _subtree_last_position(self, p):
        return RedBlackTreeMap._subtree_last_position(self, p) if self._rb else TwoDTreeMap._subtree_last_position(self,
                                                                                                                   p)

    def before(self, p):
        return RedBlackTreeMap.before(self, p) if self._rb else TwoDTreeMap.before(self, p)

    def _make_position(self, node):
        return RedBlackTreeMap._make_position(self, node) if self._rb else TwoDTreeMap._make_position(self, node)

    def _validate(self, p):
        return RedBlackTreeMap._validate(self, p) if self._rb else TwoDTreeMap._validate(self, p)

    def transform(self):
        if self._rb:
            self._rb2td(self.root())
            self._rb = False
        else:
            self._td2rb(self.root())
            self._rb = True

    def _rb2td(self, p):
        node = TwoDTreeMap._DNode()
        node.insert_element(p.element())
        node._parent = p._node._parent
        left = self.left(p)
        right = self.right(p)
        i = 0
        if left:
            if self._is_red(left):
                node.insert_element(left.element())
                if left._node._left:
                    node.connect_child(i, left._node._left)
                    i += 1
                if left._node._right:
                    node.connect_child(i, left._node._right)
                    i += 1
            else:
                node.connect_child(i, left._node)
                i += 1
        if right:
            if self._is_red(right):
                node.insert_element(right.element())
                if right._node._left:
                    node.connect_child(i, right._node._left)
                    i += 1
                if right._node._right:
                    node.connect_child(i, right._node._right)
            else:
                node.connect_child(i, right._node)
        if self.is_root(p):
            self._root = node
        p = TwoDTreeMap._make_position(self, node)
        for i in range(len(p._node._children)):
            new_p = self._rb2td(RedBlackTreeMap._make_position(self, p._node._children[i]))
            p._node.disconnect_child(i)
            p._node.connect_child(i, new_p._node)
        return p

    def _td2rb(self, p):
        l = self.num_elements(p)
        c = self.num_children(p)
        if l == 1:
            node = RedBlackTreeMap._Node(p._node._elements[0], p._node._parent)
            node._red = False
            node._right = p._node._children[1] if c != 0 else None
            node._left = p._node._children[0] if c != 0 else None
            if c != 0:
                new_p_left = self._td2rb(TwoDTreeMap._make_position(self, node._left))
                new_p_right = self._td2rb(TwoDTreeMap._make_position(self, node._right))
                node._left = new_p_left._node
                node._right = new_p_right._node
                node._left._parent = node
                node._right._parent = node
        elif l == 2:
            node = RedBlackTreeMap._Node(p._node._elements[0], p._node._parent)
            node._red = False
            node._left = p._node._children[0] if c != 0 else None
            node_red = RedBlackTreeMap._Node(p._node._elements[1], node)
            node._right = node_red
            node_red._right = p._node._children[2] if c != 0 else None
            node_red._left = p._node._children[1] if c != 0 else None
            if c != 0:
                new_p_left = self._td2rb(TwoDTreeMap._make_position(self, node._left))
                new_child_left = self._td2rb(TwoDTreeMap._make_position(self, node_red._left))
                new_child_right = self._td2rb(TwoDTreeMap._make_position(self, node_red._right))
                node._left = new_p_left._node
                node._right._right = new_child_right._node
                node._right._left = new_child_left._node
                node._right._right._parent = node._right
                node._right._left._parent = node._right
                node._left._parent = node
                node._right._parent = node
        elif l == 3:
            node = RedBlackTreeMap._Node(p._node._elements[1], p._node._parent)
            node._red = False
            child_red_right = RedBlackTreeMap._Node(p._node._elements[2], node)
            child_red_left = RedBlackTreeMap._Node(p._node._elements[0], node)
            node._right = child_red_right
            node._left = child_red_left
            child_red_left._right = p._node._children[1] if c != 0 else None
            child_red_left._left = p._node._children[0] if c != 0 else None
            child_red_right._right = p._node._children[3] if c != 0 else None
            child_red_right._left = p._node._children[2] if c != 0 else None
            if c != 0:
                new_left_left = self._td2rb(TwoDTreeMap._make_position(self, child_red_left._left))
                new_left_right = self._td2rb(TwoDTreeMap._make_position(self, child_red_left._right))
                new_right_left = self._td2rb(TwoDTreeMap._make_position(self, child_red_right._left))
                new_right_right = self._td2rb(TwoDTreeMap._make_position(self, child_red_right._right))
                node._left._right = new_left_right._node
                node._left._left = new_left_left._node
                node._right._right = new_right_right._node
                node._right._left = new_right_left._node

                node._left._left._parent = node._left
                node._left._right._parent = node._left
                node._right._left._parent = node._right
                node._right._right._parent = node._right

                node._left._parent = node
                node._right._parent = node
        if self.is_root(p):
            self._root = node
        p = RedBlackTreeMap._make_position(self, node)

        return p
