from ADT.Map.binary_search_tree import TreeMap


class myTreeMap(TreeMap):
    def count_range(self, start, stop):
        count = 0
        if not self.is_empty():
            if start is None:
                # se start non è stato passato, parto dalla radice
                p = self.first()
            else:
                p = self.find_position(start)
                if p.key() < start:
                    p = self.after(p)
            while p is not None and (stop is None or p.key() < stop):
                # yield (p.key(), p.value())
                count += 1
                p = self.after(p)
        return count

    def common_ancestor(self, p1, p2):
        p = self.root()
        ancestor = None
        while p is not None and ancestor is None:
            if p1 < p.key() and p2 < p.key():
                p = self.left(p)
            elif p1 > p.key() and p2 > p.key():
                p = self.right(p)
            elif p.key() == p1:
                ancestor = p1
            elif p.key() == p2:
                ancestor = p2
            else:
                ancestor = p.key()
        return ancestor

def test1():
    print('test BST')
    B = myTreeMap()
    print(B.is_empty())
    B['Reti di Calcolatori'] = 26
    B['Basi di Dati'] = 28
    B['Programmazione a Oggetti'] = 30
    B['Calcolatori Elettronici'] = 25
    B['Circuiti Digitali'] = 26
    B['Reti Logiche'] = 28
    print("numedo di nodi nell'albero: ", len(B))
    start = "A"
    stop = "O"
    print("numero di nodi compresi tra ", start, 'e ', stop, ': ', B.count_range(start, stop))


def test2():
    b = myTreeMap()
    b[9] = 0
    b[3] = 1
    b[12] = 2
    b[10] = 3
    b[1] = 4
    b[4] = 5
    b[5] = 6
    b[13] = 7
    p1 = 4
    p2 = 5
    print('antenato comune fra ', p1, ' e ', p2)
    print(b.common_ancestor(p1, p2))

test2()
