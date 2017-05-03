from TDP.Progetto1.TdP_collections.map.map_base import MapBase
from TDP.Progetto1.TdP_collections.map.binary_search_tree import TreeMap


class OrderException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class TwoDTreeMap(TreeMap, MapBase):
    # -------------------------- nested Position class --------------------------
    class Position(TreeMap.Position):
        """An abstraction representing the location of a single element."""
        __slots__ = '_elem_index'  # index of the element within the position

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            super().__init__(container, node)
            self._elem_index = 0

        def element(self):
            """Return the element stored at this Position."""
            return self._node.get_element(self._elem_index)

        def set_index(self, index):
            self._elem_index = index

        def get_index(self):
            return self._elem_index

    # -------------------------- nested _Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a node."""
        __slots__ = '_elements', '_parent', '_children', '_order'

        def __init__(self, order, parent=None):
            self._order = order
            self._elements = []  # array of data
            self._parent = parent
            self._children = []  # array of children

        def connect_child(self, child_index, child):
            """Connect a child to the node at the given index."""
            self._children.insert(child_index, child)
            child._parent = self

        def disconnect_child(self, child_index):
            """Disconnect a child from the node at the given index."""
            return self._children.pop(child_index)

        def get_child(self, child_index):
            """Return the child _Node at the given index."""
            return self._children[child_index]

        def is_empty(self):
            """Return True if the node contains no elements."""
            return len(self._elements) == 0

        def is_full(self):
            """Return True if the node contains all the elements."""
            return len(self._elements) == self._order - 1

        def get_element(self, index):
            """Return the element _Item at the given index."""
            return self._elements[index]

        def find_element(self, key):
            """Return the index within the node corresponding to the given key.

            Return None if the node does not contain the key."""
            index = 0
            for elem in self._elements:
                if elem._key < key:
                    index += 1
                elif elem._key == key:
                    return index
                else:
                    return None

        def insert_element(self, elem):
            """Insert the given element _Item in the node.

            Return the index of elem within the list of elements.
            """
            self._elements.append(elem)
            self._elements.sort()
            return self._elements.index(elem)

        def remove_element(self, index=None):
            """Remove the element at the given index from the node.

            If index is None, remove the last element from the node.
            """
            return self._elements.pop(index) if index is not None else self._elements.pop(-1)

        def __str__(self):
            """Display the keys of the node in the format: key1-key2-...-key_n."""
            string = ''
            for j in range(len(self._elements)):
                string += str(self.get_element(j)._key)
                if (j != len(self._elements) - 1):
                    string += '-'
            return '|' + string + '| '

    # -------------------------- (2, d) Tree ------------------------------
    def __init__(self, order=None):
        if order is None:
            order = 4
        if 3 < order < 9:
            super().__init__()
            self._order = order
        else:
            raise OrderException('The order is out of range [4,8]')

    # -------------------------- public accessors --------------------------
    def get_child(self, p, key):
        """Return the Position of p's child at the left of the given key."""
        node = p._node
        for i in range(len(node._elements)):
            if node._elements[i]._key > key:
                return self._make_position(node.get_child(i))
        return self._make_position(node.get_child(i + 1))

    def num_children(self, p):
        """Return the number of children of Position p."""
        node = self._validate(p)
        return len(node._children)

    def num_elements(self, p):
        """Return the number of elements of Position p."""
        node = self._validate(p)
        return len(node._elements)

    # ------------------------------- nonpublic utilities -------------------------------
    def _subtree_search(self, p, k):
        """Return Position of p's subtree having key k, or last node searched."""
        while True:
            elem_index = p._node.find_element(k)
            if elem_index is not None:
                p.set_index(elem_index)
                return p
            elif self.is_leaf(p):
                p.set_index(0)
                return p
            else:
                p = self.get_child(p, k)

    # --------------------- public methods providing "positional" support ---------------------

    def left(self, p):
        """Return the Position of p's left child (or None if no left child)."""
        return self._make_position(p._node.get_child(p.get_index())) if not self.is_leaf(p) else None

    def right(self, p):
        """Return the Position of p's right child (or None if no right child)."""
        return self._make_position(p._node.get_child(p.get_index() + 1)) if not self.is_leaf(p) else None

    def before(self, p):
        """Return the Position just before p in the natural order.
    
        Return None if p is the first position.
        """
        self._validate(p)
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            if p.get_index() == 0:
                if self.is_root(p):
                    return None
                walk = p
                above = self.parent(walk)
                above.set_index(self.num_elements(above) - 1)

                while above.key() > p.key() and above.get_index() != 0:
                    above.set_index(above.get_index() - 1)
                while above is not None and above.key() > p.key():
                    walk = above
                    above = self.parent(walk)
                    if above is None:
                        return None
                    above.set_index(self.num_elements(above) - 1)
                    while above.key() > p.key() and above.get_index() != 0:
                        above.set_index(above.get_index() - 1)

                return above
            else:
                p.set_index(p.get_index() - 1)
                return p

    def after(self, p):
        """Return the Position just after p in the natural order.
    
        Return None if p is the last position.
        """
        self._validate(p)
        if self.right(p):  # se la position un sottoalbero destro,
            return self._subtree_first_position(self.right(p))  # cercare la prima posizione in tale sottoalbero
        else:  # se invece sono in una foglia
            if self.num_elements(p) - 1 == p.get_index():  # se k è l'ultima chiave in p,
                if self.is_root(p):
                    return None
                walk = p
                above = self.parent(walk)  # prendere il parent

                # scorrimento da sinistra in above per cercare una chiave maggiore di k
                while above.key() < p.key() and above.get_index() != self.num_elements(above) - 1:
                    above.set_index(above.get_index() + 1)

                # se la chiave non è stata trovata, salire di un livello ed effettuare lo stesso scorrimento precedente;
                # Se si ariva alla radice, l'after non esiste
                while above is not None and above.key() < p.key():
                    walk = above
                    above = self.parent(walk)
                    if above is None:
                        return None

                    while above.key() < p.key() and above.get_index() != self.num_elements(above) - 1:
                        above.set_index(above.get_index() + 1)

                return above
            else:  # se k non è l'ultimo elemento, prendo quello successivo
                p.set_index(p.get_index() + 1)
                return p

    def delete(self, p):
        """Remove the item at given Position."""
        index = p.get_index()
        # Caso in cui l'elemento è in una foglia. Se l'elemento esiste lo cancello e poi verifico l'underflow
        if self.is_leaf(p):
            p._node.remove_element(index)
            successor = p
            self._size -= 1
            if self.num_elements(p) == 0 and self.is_root(p):
                return
        # Caso in cui l'elemento NON è in una foglia.
        else:
            # dato il successore, rimuove il primo elemento, lo inserisce in p e rimuove da p l'elemento k
            successor = self.after(p)
            p._node.remove_element(p.get_index())
            p._node.insert_element(successor.element())
            successor._node.remove_element(0)
            self._size -= 1

        # Gestione underflow propagati.
        # Partendo dal successore e salendo di livello, fintanto che il nodo corrente è vuoto, in base al numero di elementi all'interno del
        # sibling, chiamo transfer o fusion.
        # NB in caso di transfer non è possibile avere ulteriori underflow.
        while successor._node.is_empty():
            sibling, succ_index, flag = self.get_sibling(successor)
            if self.num_elements(sibling) > 1:
                self.transfer(successor, sibling, succ_index, flag)
                return
            else:
                self.fusion(successor, sibling, succ_index, flag)
                if self.is_root(sibling):
                    return
                successor = self.parent(successor)

    def get_sibling(self, p):
        """Return the Position of the left sibling of p, the index of p and a flag set to 'left'.

        Return the Position of the right sibling of p, the index of p and a flag set to 'right' if p has no left siblings.
        """
        parent = self.parent(p)
        index = 0
        # cerco l'indice di p all'interno del parent
        while parent._node.get_child(index) != p._node:
            index += 1

        # se p è il figlio più a sinistra, ritorna direttamente il suo fratello destro
        if index == 0:
            flag = 'right'
            sibling = self._make_position(parent._node.get_child(index + 1))

        # se p è il figlio più a destra, ritorna direttamente il suo fratello sinistro
        elif index == self.num_children(parent) - 1:
            flag = 'left'
            sibling = self._make_position(parent._node.get_child(index - 1))

        # se p ha sia un fratello destro che uno sinistro,
        else:
            left_sibling = self._make_position(parent._node.get_child(index - 1))
            right_sibling = self._make_position(parent._node.get_child(index + 1))
            left_elems = self.num_elements(left_sibling)
            right_elems = self.num_elements(right_sibling)

            # ritorna il fratello con più elementi; in condizioni di parità ritorna il fratello sinistro
            if right_elems > left_elems:
                flag = 'right'
                sibling = right_sibling
            else:
                flag = 'left'
                sibling = left_sibling

        return sibling, index, flag

    def fusion(self, p, sibling, p_index, flag):
        """Perform the fusion operation between p and sibling in case of underflow.

        The parameter p_index is the index of p within the children of its parent.
        The parameter flag must be 'left'/'right' depending on if sibling is left/right sibling of p.
        """
        parent = self.parent(p)
        parent._node.disconnect_child(p_index)  # disconnetto il nodo da fondere dal parent
        if flag == 'left':  # se p ha un sibling sinistro
            new_elem = parent._node.remove_element(
                p_index - 1)  # rimuovo dal parent l'elemento di sui p è il figlio destro
            if not self.is_leaf(p):
                child = p._node.disconnect_child(0)  # disconnetto l'unico figlio (essendo un 1-nodo)
                sibling._node.connect_child(self.num_children(sibling), child)  # e lo connetto al fratello di p
        else:
            # (sibling destro) speculare al caso precedente
            new_elem = parent._node.remove_element(0)
            if not self.is_leaf(p):
                child_p = p._node.disconnect_child(0)
                sibling._node.connect_child(0, child_p)

        sibling._node.insert_element(new_elem)  # inserimento di new_elem

        # se il parent rimane vuoto ed è la root, il sibling diventa la nuova root
        if self.num_elements(parent) == 0 and self.is_root(parent):
            self._root = sibling._node
            sibling._node._parent = None

    def transfer(self, p, sibling, p_index, flag):
        """Perform the transfer operation between p, sibling and their parent in case of underflow.

        The parameter p_index is the index of p within the children of its parent.
        The parameter flag must be 'left'/'right' depending on if sibling is left/right sibling of p.
        """
        parent = self.parent(p)
        if flag == 'left':
            # se p ha un sibling sinistro:
            # 1) rimuovo l'elemento padre di sibling e p dal parent e lo inserisco in p
            # 2) rimuovo l'ultimo elemento di sibling e lo inserisco nel parent
            # 3) rimuovo l'ultimo figlio di siblin e lo inserisco come primo figlio di p
            parent_elem = parent._node.remove_element(p_index - 1)
            sibling_elem = sibling._node.remove_element(self.num_elements(sibling) - 1)
            parent._node.insert_element(sibling_elem)
            p._node.insert_element(parent_elem)
            if not self.is_leaf(p):
                child = p._node.disconnect_child(0)
                p._node.connect_child(1, child)
                child = sibling._node.disconnect_child(self.num_children(sibling) - 1)
                p._node.connect_child(0, child)
        else:
            # se p ha un sibling destro, le operazioni sono speculari alle precedente
            parent_elem = parent._node.remove_element(p_index)
            sibling_elem = sibling._node.remove_element(0)
            parent._node.insert_element(sibling_elem)
            p._node.insert_element(parent_elem)
            if not self.is_leaf(p):
                child = p._node.disconnect_child(self.num_children(p) - 1)
                p._node.connect_child(0, child)
                child = sibling._node.disconnect_child(0)
                p._node.connect_child(1, child)

    def split(self, p):
        """Perform the split operation of p in case p is full, thus preventing overflow."""
        node = p._node
        last_elem = node.remove_element()
        second_last_elem = node.remove_element()
        if not self.is_leaf(p):
            last_child = node.disconnect_child(-1)
            second_last_child = node.disconnect_child(-1)

        n_right = self._Node(self._order)  # costruzione del nuovo nodo

        if node == self._root:  # se il nodo da splittare è la root,
            self._root = self._Node(self._order)  # si crea una nuova root
            parent = self._root  # la nuova root diventa il parent del nodo corrent
            self._root.connect_child(0, node)  # il nodo corrente viene connesso al parent
        else:  # se il nodo corrente non è la root,
            parent = node._parent  # si prende il parent.

        # gestione del parent
        elem_index = parent.insert_element(second_last_elem)  # si inserisce il penultimo elemento nel parent

        # connessioe del nuovo nodo al parent
        parent.connect_child(elem_index + 1, n_right)

        # inserimento dell'ultimo elemento e dei figli nel nuovo nodo
        n_right.insert_element(last_elem)
        if not self.is_leaf(p):
            n_right.connect_child(0, second_last_child)
            n_right.connect_child(1, last_child)

    def overflow(self, p):
        return self.num_elements(p) == self._order

    # --------------------- public methods for (standard) map interface ---------------------
    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        new_item = self._Item(k, v)

        if self.is_empty():
            self._root = self._Node(self._order)
            self._root.insert_element(new_item)
        else:
            p = self.find_position(k)
            p._node.insert_element(new_item)
            while p is not None and self.overflow(p):
                self.split(p)
                p = self.parent(p)
        self._size += 1

    # --------------------- methods for displaying the tree ---------------------
    def children(self, p):
        for i in range(self.num_children(p)):
            yield self._make_position(p._node._children[i])

    def _beautify(self, lst):
        max_l = len(lst[-1])

        for i in range(len(lst) - 1):
            tmp = ''
            for j in range((max_l - len(lst[i])) // 2):
                tmp += ' '
            lst[i] = tmp + lst[i] + tmp

    def display_tree(self):
        if not self.is_empty():
            p_list = []
            next_level_nodes = 0
            i = 0
            stop = 1
            tmp_str = ''
            for p in self.breadthfirst():
                next_level_nodes += self.num_children(p)
                tmp_str += str(p._node)
                i += 1
                if i == stop:
                    p_list.append(tmp_str)
                    tmp_str = ''
                    i = 0
                    stop = next_level_nodes
                    next_level_nodes = 0

            self._beautify(p_list)
            for level in p_list:
                print(level)
        else:
            print('Albero vuoto!')


