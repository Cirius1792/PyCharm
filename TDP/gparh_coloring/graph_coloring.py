from TDP.TdP_collections.graphs.graph import Graph
from TDP.TdP_collections.priority_queue.heap_priority_queue import HeapPriorityQueue
from TDP.gparh_coloring.ReverseHeap import reverse_heap_priority_queue
from TDP.TdP_collections.priority_queue.adaptable_priority_queue import AdaptableHeapPriorityQueue


def graph_coloring(G):

    color = {}
    pq = HeapPriorityQueue()
    for v in G.vertices():
        degv = G.degree(v) + G.degree(v,False) if G.is_directed() else G.degree(v)
        #degv = G.degree(v)
        pq.add(degv, v)                         #Riordino i vertici per grado decrescente

    ku = set()
    k = 0
    while not pq.is_empty():
        deg, u = pq.remove_min()
        used = set()                            #ad ogni iterazione controllo se il vertice corrente
        for v in color:                         #è adiacente ad uno di quelli già nella soluzione. Se
            if G.get_edge(u, v):                #questo è vero, tolgo dal set dei possibili colori che posso assegnare
                used.add(color[v])              #a quel vertice il colore assegnato al vertice adicente
            if G.is_directed() and G.get_edge(v,u):
                used.add(color[v])
        unused = ku.difference(used)
        if unused:
            color[u] = unused.pop()
        else:
            k += 1
            ku.add(k)
            color[u] = k
    return color, len(ku)

def print_coloring(colors, g):
    pass

def check_colors(G, color):
    for u in G.vertices():
        for e in G.incident_edges(u):
            v = e.opposite(u)
            if color[u] == color[v]:
                print(u,'\t',v)
                return False
    return True


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

def max_degree(G):
    max_deg = 0
    for v in G.vertices():
        degv = G.degree(v)
        max_deg = max(max_deg, degv)

    return max_deg


if __name__ == '__main__':
    g = load_graph(open('grafo1.txt'), True)
    color, k = graph_coloring(g)
    D = max_degree(g)
    for v in color:
        print("vertice:\t ",v,"\t\t colore:\t ", color[v])
    print("check colors: ", check_colors(g, color))
    print("max degree:\t\t",D)
    print("colors:\t\t\t",k)
    print("k<D+1?\t\t",k<=D+1)