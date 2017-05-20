from TDP.TdP_collections.tree.linked_binary_tree import LinkedBinaryTree
from TDP.TdP_collections.priority_queue.heap_priority_queue import HeapPriorityQueue
from TDP.TdP_collections.graphs.graph import Graph

def huffman(x):
    q = HeapPriorityQueue()

    f = charFreq(x)
    count = 0
    tree = LinkedBinaryTree()
    for c in x:
        element = c
        T = tree._make_position( LinkedBinaryTree._Node(element))
        q.add(f[c], T)
    while len(q) > 1:
        f1, T1 = q.remove_min()
        f2, T2 = q.remove_min()
        element = f1+f2
        T = tree._make_position( LinkedBinaryTree._Node(element))
        T._node._left = T1._node
        T._node._right = T2._node
        T1._node._parent = T._node
        T2._node._parent = T._node
        q.add(f1+f2, T)
        count += 1
    f, T = q.remove_min()
    tree._root = T._node
    tree._size = count
    return tree


def charFreq(X):

    d = {}
    for c in X:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d


def to_dict(ct):
    dct = {}
    _get_code(ct, dct)
    return dct


def _get_code(ct, dct, p=None, c_str=""):
    if p is None:
        p = ct.root()
    left = ct.left(p)
    right = ct.right(p)
    if left is not None:
        left_str = c_str + "0"
        _get_code(ct, dct,left, left_str)
    if right is not None:
        right_str = c_str + "1"
        _get_code(ct, dct, right, right_str)
    else:
        dct[p.element()] = c_str



def load_graph(file, directed=False):
    """legge da file un grafo rappresentato dalla lista dei suoi archi e costruisce (e restituisce) un oggetto 
    della classe Graph. Gli archi sono rappresentati come triple (sorgente, destinazione, elemento=1), 
    dove elemento è inizializzato per default a 1 se non presente."""
    g = Graph(directed)
    for line in file:
        edge = line.split()
        u = None
        v = None
        if len(edge) > 1:
            for k in g.vertices():
                if edge[0] == k.element():
                    u = k
                elif edge[1] == k.element():
                    v = k
                if u is not None and v is not None:
                    break

            if u is None:
                u = g.insert_vertex(edge[0])
            if v is None:
                v = g.insert_vertex(edge[1])
            if len(edge) == 3:
                g.insert_edge(u, v, edge[2])
            else:
                g.insert_edge(u,v,1)
    return g



def test_huffman():
    x = "abracadabra"
    T = huffman(x)
    dct = to_dict(T)
    for k in dct:
        print("key:\t\t",k,"\tcode:\t\t",dct[k])


def test_graph():


if __name__ == '__main__':
    test_huffman()