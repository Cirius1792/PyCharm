from TDP.TdP_collections.graphs.dijkstra import shortest_path_lengths
from TDP.TdP_collections.graphs.BellmanFord import BellmaFord
from TDP.TdP_collections.priority_queue.heap_priority_queue import HeapPriorityQueue
from TDP.TdP_collections.tree.linked_binary_tree import LinkedBinaryTree
from TDP.TdP_collections.graphs.graph import Graph

def all_pair_ss(g):
    n = len(g.vertices())
    d = {}
    pred = {}

    for v in g.vertices():                   #inizializzazione dei dizionari
        d[v] = {}
        pred[v] = {}

    for u in g.vertices():                   #Inizializzazione della matrice dei precedenti
        for v in g.vertices():
            p = g.get_edge(u, v)
            pred[u][v] = None
            if p is None:
                d[u][v] = float('inf') if u != v else 0
            else:
                d[u][v] = float(p.element())

    for k in g.vertices():
        for i in g.vertices():
            for j in g.vertices():
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    pred[i][j] = k
    return d, pred

def all_pair_ss_v1(g):
    n = len(g.vertices())
    pred = [[None for u in range(len(g.vertices()) + 1)] for i in range(len(g.vertices()) + 1)]
    d = [[0 for u in range(len(g.vertices())+1)] for i in range(len(g.vertices()) + 1)]
    for i in range(0, len(g.vertices())+1):
        d[i][0] = i
        pred[i][0] = i
    for i in range(0, len(g.vertices())+1):
        d[0][i] = i
        pred[0][i] = i

    for u in range(1, n+1):
        for v in range(1, n+1):
            u_v = g.find_vertex(str(u))
            v_v = g.find_vertex(str(v))
            if u_v and v_v:
                p = g.get_edge(u_v, v_v)
                if p is None:
                    d[u][v] = float('inf') if u != v else 0
                    pred[u][v] = None
                else:
                    d[u][v] = float(p.element())

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    pred[i][j] = k
    return d, pred

def print_path(pred, u, v):
    if pred[u][v] is None:
        print(u,"\t -> \t",v)
    else:
        print_path(pred, u, pred[u][v])
        print_path(pred, pred[u][v], v)

def huffman(x):
    q = HeapPriorityQueue()
    f = charFreq(x)
    count = 0
    tree = LinkedBinaryTree()
    for c in x:
        element = c
        T = tree._make_position(LinkedBinaryTree._Node(element))
        q.add(f[c], T)
    while len(q) > 1:
        f1, T1 = q.remove_min()
        f2, T2 = q.remove_min()
        element = f1 + f2
        T = tree._make_position(LinkedBinaryTree._Node(element))
        T._node._left = T1._node
        T._node._right = T2._node
        T1._node._parent = T._node
        T2._node._parent = T._node
        q.add(f1 + f2, T)
        count += 1
    f, T = q.remove_min()
    tree._root = T._node
    tree._size = count
    return tree

def cycle_free(G):
    d = {}
    cycle = False
    for s in G.vertices():                          #Eseguo l'algoritmo di Bellam-Ford per ogni vertice
        for v in G.vertices():
            d[v] = 0 if v == s else float('inf')
        for i in range(len(G.vertices())-1):
            for e in G.edges():
                u, v = e.endpoints()
                wgt = float(e.element())
                if d[u] + wgt < d[v]:
                    d[v] = d[u] + wgt

        for e in G.edges():                         #Se alla fine dell'algoritmo è ancora possibile rilassare
            u, v = e.endpoints()                    #un arco allora ci sono cicli di lunghezza negativa nel grafo
            wgt = float(e.element())
            if d[u] + wgt < d[v]:
                return True
    return cycle

def bf_cycle_check(G, s):
    d = {}
    cycle = False
    for v in G.vertices():
        d[v] = 0 if v == s else float('inf')
    for i in range(len(G.vertices())-1):
        for e in G.edges():
            u, v = e.endpoints()
            wgt = float(e.element())
            if d[u] + wgt < d[v]:
                d[v] = d[u] + wgt
    for e in G.edges():
        u, v = e.endpoints()
        wgt = float(e.element())
        if d[u] + wgt < d[v]:
            cycle = True
    return cycle

def charFreq(X):
    "Restituisce un dizionario in cui la chiave è il carattere ed il valore è il numero di occorrenze"
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
    """Scorre l'albero ricorsivamente per ricostruire il codice associato al carattere"""
    if p is None:
        p = ct.root()
    left = ct.left(p)
    right = ct.right(p)
    if left is not None:
        left_str = c_str + "0"
        _get_code(ct, dct, left, left_str)
    if right is not None:
        right_str = c_str + "1"
        _get_code(ct, dct, right, right_str)
    else:
        dct[p.element()] = c_str

#Funzioni utilizzate per lo svolgimento dei test------------------------------------------------
def print_matrix(mtr):
    for a in mtr:
        ln = ""
        for i in a:
            ln += str(i) + " \t\t"
        print(ln)


def print_dic(d):
    for i in d:
        txt = ""
        for j in d[i]:
            txt += str(d[i][j])+" \t\t\t"
        print(txt)


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
                g.insert_edge(u, v, 1)
    return g

#Funzioni di Test--------------------------------------------------------------------------------
def test_huffman():
    x = "abracadabra"
    print("parola: ",x)
    T = huffman(x)
    dct = to_dict(T)
    l = 0
    for k in dct:
        print("key:\t\t", k, "\tcode:\t\t", dct[k])
        l += len(dct[k])
    print("lunghezza media parola codice: ", round(l/len(dct),2))

    x = "aiuola"
    print("parola: ",x)
    T = huffman(x)
    dct = to_dict(T)
    l=0
    for k in dct:
        print("key:\t\t", k, "\tcode:\t\t", dct[k])
        l += len(dct[k])
    print("lunghezza media parola codice: ", round(l/len(dct),2))

    x = "tre tigri contro tre tigri"
    print("parola: ",x)
    T = huffman(x)
    dct = to_dict(T)
    l=0
    for k in dct:
        print("key:\t\t", k, "\tcode:\t\t", dct[k])
        l += len(dct[k])
    print("lunghezza media parola codice: ", round(l/len(dct),2))


def test_graph():
    print("########################Grafo1########################")
    grp = load_graph(open('grafo1.txt'), True)
    print("numero di nodi:\t\t", len(grp.vertices()))
    print("numero di archi:\t\t", len(grp.edges()))
    print("has cycle?\t", cycle_free(grp))

    print("########################Grafo2########################")
    grp = load_graph(open('grafo2.txt'), False)
    print("numero di nodi:\t\t", len(grp.vertices()))
    print("numero di archi:\t\t", len(grp.edges()))
    print("has cycle?\t", cycle_free(grp))

    print("########################Grafo3########################")
    grp = load_graph(open('grafo3.txt'), True)
    print("numero di nodi:\t\t", len(grp.vertices()))
    print("numero di archi:\t\t", len(grp.edges()))
    print("has cycle?\t", cycle_free(grp))

    print("########################Grafo4########################")
    grp = load_graph(open('grafo4.txt'), True)
    print("numero di nodi:\t\t", len(grp.vertices()))
    print("numero di archi:\t\t", len(grp.edges()))
    print("has cycle?\t", cycle_free(grp))


def test_FW():

    print("\n\n########################All_Pair_ss########################")
    print("########################Test Grafo1########################")
    g = load_graph(open('grafo_slide.txt'), True)
    d, pred = all_pair_ss(g)

    u = g.find_vertex('3')
    v = g.find_vertex('4')
    print("percorso da u = ",u," a v = ",v,":")
    print_path(pred, u,v)

if __name__ == '__main__':
    print("########################Test Grafi########################")
    test_graph()
    test_FW()
    print("########################Test Huffman########################")
    test_huffman()
