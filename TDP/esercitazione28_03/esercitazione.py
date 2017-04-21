from TdP_collections.map.avl_tree import AVLTreeMap

class AVLTreeMapHW (AVLTreeMap):
    #esercizio 1
    def __iadd__(self, a):
        for e in a:
            self[e] = a[e]
        return self

    #Esercizio 2
    def at_index(self, i):
        j = 0
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

    def keys_in_range(self, start, stop):
        l = list()
        for i in range(start,stop+1):
            l.append(self.at_index(i))
        return l

    #Esercizio 3
    def index_set(self):
        s = dict()
        index = 0
        for e in self:
            s[index] = self[e]
            index += 1
        return s

    # Esercizio 4
    def at_index_2(self, i):
        pass

    def index_of(self, p):
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

    t1 = AVLTreeMapHW()
    t1[4] = 1
    t1[2] = 12
    t1[19] = 6
    #b += t1
    del b[5]
    #print(b[2])
    l = b.inorder()
    print('\n')
    for e in l:
        print(e.key())
    print('\n')
    
    print(b.at_index(2))
    print(b.index_of(b.find_position(13)))
    l = b.keys_in_range(3, 5)
    print(l)
    print(b.index_set())

test2()


