from TdP_collections.map.avl_tree import AVLTreeMap


class AVLTreeMapHW(AVLTreeMap):
    def __contains__(self, k):
        """Restituisce True se è presente un elemento con chiave k"""
        if self.is_empty():
            return True
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)  # hook for balanced tree subclasses
            if k != p.key():
                return False
            return True

    def __iadd__(self, t2):
        """t1 += t2, aggiunge tutti gli elementi (chiave, valore) dell’albero t2 all’albero t1. Se una chiave
        dell’albero t2 è già presente in t1, il valore dell’elemento in t1 deve essere preservato. Assicurarsi che le
        chiavi di t2 siano dello stesso tipo delle chiavi di t1"""
        key = self.root().key()
        for el in t2:
            if el.__class__.__name__ != key.__class__.__name__:
                raise KeysMismatch('keys mismatch: ')
            elif el not in self:
                self[el] = t2[el]
        return self

    def __lt__(self, other):
        """t1 < t2, restituisce True se le chiavi dell’albero t1 sono contenute nell’albero t2"""

        for el in self:
            if el not in other:
                return False
        return True

    def __truediv__(self, other):
        """t1 \ t2, rimuove da t1 tutti gli elementi le cui chiavi sono presenti in t2"""
        l = []
        for el in other:
            if el in self:
                del self[el]
        return self

    def __str__(self):
        """La stringa output deve avere il seguente formato:
            <(chiave, valore, altezza), . . . , (chiave, valore, altezza)>
            Le triple sono elencate per ordine crescente di chiave."""

        txt = "<"
        txt = self._get_str(self.root(), txt)
        txt = txt[:- 2] + "> "
        return txt

    def same_heigth(self, h):
        """Restituisce un dizionario contente le coppie (chiave, valore) contenuti nei nodi che hanno altezza h.
        Valutare la complessità di tempo del metodo."""
        #Complessità: O(log(h))
        d = dict()
        self._find_h(self.root(), d, h)
        return d

    def out_by_heigth(self):
        """Restituisce una stringa secondo il seguente seguente formato: <(chiave, valore, altezza), . . . ,
        ( chiave, valore, altezza)>
        Le triple sono elencate per ordine crescente di altezza. Valutare la complessità di tempo del metodo."""
        #Complessità: O(nlog(n))
        txt = "<"
        if not self.is_empty():
            flag = True
            h = 1
            while flag:
                d = self.same_heigth(h)
                if d:
                    for el in d:
                        txt += "("+str(el)+", "+str(d[el])+", "+str(h)+"), "
                else:
                    flag = False
                h += 1
        txt = txt[:len(txt)-2] + "> "
        return txt

    def parenthesize(self, empty=False):
        """Restituisce una stringa che rappresenta la versione parentesizzata degli elementi contenuti nell’albero. """
        st = []
        if empty:
            self._parenthesize_my_tree_with_empty_nodes(self.root(), st)
        else:
            self._parenthesize_my_tree(self.root(), st)
        txt = ""
        for e in st:
            txt += e
        return txt

    def n_balanced(self, p=None):
        """restituisce True se il sotto-albero radicato in p è bilanciato rispetto al numero dei nodi (se p=None il
         controllo deve essere eseguito su tutto l’albero). Valutare la complessità di tempo del metodo."""
        #Complessità: O(log(n))
        if p is None:
            p = self.root()
        left = 0
        right = 0

        if self.left(p) is not None:
            left = self._node_counter(p)
        if self.right(p) is not None:
            right = self._node_counter(p)
        if abs(left - right) <= 1:
            return True
        return False

    def _node_counter(self, p):
        n = 1
        if self.left(p) is not None:
            n += self._node_counter(self.left(p))
        if self.right(p) is not None:
            n += self._node_counter(self.right(p))
        return n

    def _get_str(self, p, t, h=0):

        if self.left(p) is not None:
            t = self._get_str(self.left(p), t, h + 1)
        t += '(' + str(p.key()) + ', ' + str(p.value()) + ', ' + str(h) + '), '
        if self.right(p) is not None:
            t = self._get_str(self.right(p), t, h + 1)
        return t

    def _find_h(self, p, d, target_h):

        if target_h == p._node._height:
            d[p.key()] = p.value()
        else:
            if self.left(p) is not None:
                self._find_h(self.left(p), d, target_h)
            if self.right(p) is not None:
                self._find_h(self.right(p), d, target_h)

    def _parenthesize_my_tree(self, p, st=[]):
        st.append('('+str(p.key()))
        if self.left(p) is not None:
            self._parenthesize_my_tree(self.left(p), st)
        if self.right(p) is not None:
            self._parenthesize_my_tree(self.right(p), st)
        st.append(')')

    def _parenthesize_my_tree_with_empty_nodes(self, p, st=[]):
        st.append('(' + str(p.key()))
        left = True if (self.left(p) is not None) else False
        right = True if (self.right(p) is not None) else False
        if left or right:
            if left:
                self._parenthesize_my_tree_with_empty_nodes(self.left(p), st)
            else:
                st.append('()')
            if right:
                self._parenthesize_my_tree_with_empty_nodes(self.right(p), st)
            else:
                st.append('()')
        st.append(')')


class KeysMismatch(Exception):
    pass

def test2():
    b = AVLTreeMapHW()
    b[9] = 0
    b[3] = 1
    b[12] = 2
    b[10] = 3
    b[1] = 4
    b[4] = 5
    b[5] = 6
    b[13] = 7
    b[15] = 92

    t1 = AVLTreeMapHW()
    t1[4] = 1
    t1[2] = 12
    t1[19] = 6
    b += t1
    t2 = AVLTreeMapHW()
    t2[90] = 23
    print(b[4])  # risultato atteso: 5
    print(t1 < b)  # risultato atteso: True
    print(t2 < b)  # risultato atteso: False
    print("truediv")
    print( "b: ",b)
    print("t1: ",t1)
    print(" b/t1")
    b /= t1
    print(b)
    print("")
    print("toString:")
    print(b)
    b.inorder()

    print("same_heigth(2):")
    print(b.same_heigth(2))  # risultato atteso: {1: 4, 4: 5, 10: 3, 13: 7}
    print("by heigth:")
    print(b.out_by_heigth())

    print("parenthesize:")
    print(b.parenthesize())
    print("parenthesize with empty nodes:")
    print(b.parenthesize(True))

    print("n_balanced:")
    print(b.n_balanced())


test2()
