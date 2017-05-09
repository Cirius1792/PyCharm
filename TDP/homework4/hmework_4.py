from TDP.TdP_collections.graphs.dfs import *

class Graph:
    """Representation of a simple graph using an adjacency map."""

    # ------------------------- nested Vertex class -------------------------
    class Vertex:
        """Lightweight vertex structure for a graph."""
        __slots__ = '_element'

        def __init__(self, x):
            """Do not call constructor directly. Use Graph's insert_vertex(x)."""
            self._element = x

        def element(self):
            """Return element associated with this vertex."""
            return self._element

        def __hash__(self):  # will allow vertex to be a map/set key
            return hash(id(self))

        def __str__(self):
            return str(self._element)

    # ------------------------- nested Edge class -------------------------
    class Edge:
        """Lightweight edge structure for a graph."""
        __slots__ = '_origin', '_destination', '_element'

        def __init__(self, u, v, x):
            """Do not call constructor directly. Use Graph's insert_edge(u,v,x)."""
            self._origin = u
            self._destination = v
            self._element = x

        def endpoints(self):
            """Return (u,v) tuple for vertices u and v."""
            return (self._origin, self._destination)

        def opposite(self, v):
            """Return the vertex that is opposite v on this edge."""
            if not isinstance(v, Graph.Vertex):
                raise TypeError('v must be a Vertex')
            if v is self._origin:
                return self._destination
            elif v is self._destination:
                return self._origin
            raise ValueError('v not incident to edge')

        def element(self):
            """Return element associated with this edge."""
            return self._element

        def __hash__(self):  # will allow edge to be a map/set key
            return hash((self._origin, self._destination))

        def __str__(self):
            return '({0},{1},{2})'.format(self._origin, self._destination, self._element)

    # ------------------------- Graph methods -------------------------
    def __init__(self, directed=False):
        """Create an empty graph (undirected, by default).
    
        Graph is directed if optional paramter is set to True.
        """
        self._outgoing = {}
        # only create second map for directed graph; use alias for undirected
        self._incoming = {} if directed else self._outgoing

    def _validate_vertex(self, v):
        """Verify that v is a Vertex of this graph."""
        if not isinstance(v, self.Vertex):
            raise TypeError('Vertex expected')
        if v not in self._outgoing:
            raise ValueError('Vertex does not belong to this graph.')

    def is_directed(self):
        """Return True if this is a directed graph; False if undirected.
    
        Property is based on the original declaration of the graph, not its contents.
        """
        return self._incoming is not self._outgoing  # directed if maps are distinct

    def vertex_count(self):
        """Return the number of vertices in the graph."""
        return len(self._outgoing)

    def vertices(self):
        """Return an iteration of all vertices of the graph."""
        return self._outgoing.keys()

    def edge_count(self):
        """Return the number of edges in the graph."""
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        # for undirected graphs, make sure not to double-count edges
        return total if self.is_directed() else total // 2

    def edges(self):
        """Return a set of all edges of the graph."""
        result = set()  # avoid double-reporting edges of undirected graph
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())  # add edges to resulting set
        return result

    def get_edge(self, u, v):
        """Return the edge from u to v, or None if not adjacent."""
        self._validate_vertex(u)
        self._validate_vertex(v)
        return self._outgoing[u].get(v)  # returns None if v not adjacent

    def degree(self, v, outgoing=True):
        """Return number of (outgoing) edges incident to vertex v in the graph.
    
        If graph is directed, optional parameter used to count incoming edges.
        """
        self._validate_vertex(v)
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
        """Return all (outgoing) edges incident to vertex v in the graph.
    
        If graph is directed, optional parameter used to request incoming edges.
        """
        self._validate_vertex(v)
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, x=None):
        """Insert and return a new Vertex with element x."""
        v = self.Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}  # need distinct map for incoming edges
        return v

    def insert_edge(self, u, v, x=None):
        """Insert and return a new Edge from u to v with auxiliary element x.
    
        Raise a ValueError if u and v are not vertices of the graph.
        Raise a ValueError if u and v are already adjacent.
        """
        if self.get_edge(u, v) is not None:  # includes error checking
            raise ValueError('u and v are already adjacent')
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e

    def remove_edge(self, e):
        u, v = e.endpoints()
        del self._outgoing[u][v]
        del self._incoming[v][u]
            
    def remove_vertex(self, v):
        if self.is_directed():
            edges = self.incident_edges(v, False)
            for e in edges:
                del self._outgoing[e.opposite(v)][v]
            del self._incoming[v]
        edges = self.incident_edges(v)
        for e in edges:
            del self._incoming[e.opposite(v)][v]
        del self._outgoing[v]





    def print_edges(self):
        for e in self.edges():
            print(e)

#Esercizio 1
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

#Esercizio 3
def components(g):
    """preso in input un grafo non diretto g, restituisce un dizionario in cui le chiavi sono
     i vertici del grafo ed i valori sono interi che identificano la componente connessa a cui
      il vertice appartiene"""
    if g.is_directed():
        raise DirectedGraphError("La funzione supporta solo grafi non diretti")
    dfs_trees = DFS_complete(g)
    comp = {}
    comp_count = 0
    for tree in dfs_trees:
        if dfs_trees[tree] is None:
            comp_count += 1
        comp[tree] = comp_count
    return comp

#Esercizio 4
def find_cycle(g, u):
    discovered = {}
    DFS(g, u, discovered)
    cycle = []
    for e in g.incident_edges(u):
        path = construct_path(e.opposite(u), u, discovered)
        if path:
            for i in range(len(path)):
                cycle.append(g.get_edge(path[i-1],path[i]))
            return cycle
        return None

class DirectedGraphError(Exception):

    def __init__(self, value):
        self._value = value

    def __str__(self):
        print(str(self._value))

#Funzione sviluppata a fini di test
def find_vertex(g, lbl):
    """Funzione sviluppata a fini di test. Restituisce il vertice del grafo con la label lbl, None se il vertice 
    non è stato trovato"""
    for v in g.vertices():
        if v.element() == lbl:
            return v
    return None


if __name__ == '__main__':
    GRAPH = 'graph_undir.txt'
    HUBS = 'hubs_dir.txt'
    RHESUS = 'rhesus_edges.txt'
    ZEBRA =  'zebra_edges.txt'

    print('----------------graph_undir.txt----------------')
    graph_undir = load_graph(open(GRAPH))

    for e in graph_undir.edges():
        print(e)
    print('vertex:', graph_undir.vertex_count())
    print('edge: ', graph_undir.edge_count())

    print('----------------hubs_dir.txt----------------')
    hubs_dir = load_graph(open(HUBS), True)

    for e in hubs_dir.edges():
        print(e)
    print('edge: ', hubs_dir.edge_count())
    print('vertex:', hubs_dir.vertex_count())

    print('----------------rhesus_edges.txt----------------')
    rhesus_edges = load_graph(open(RHESUS), True)

    for e in rhesus_edges.edges():
        print(e)
    print('vertex:', rhesus_edges.vertex_count())
    print('edge: ', rhesus_edges.edge_count())

    print('----------------zebra_edges.txt----------------')
    zebra_edges = load_graph(open(ZEBRA))

    for e in zebra_edges.edges():
        print(e)
    print('vertex:', zebra_edges.vertex_count())
    print('edge: ', zebra_edges.edge_count())

    print('\n\n----------------Test Esercizio 2----------------')

    print("Test su grafo INDIRETTO")
    a = find_vertex(graph_undir, 'A')
    b = find_vertex(graph_undir, 'B')
    toRemove = graph_undir.get_edge(a,b)
    print("eliminazione di: ", toRemove)
    graph_undir.remove_edge(toRemove)
    print("Edge eliminato con successo: ", toRemove not in graph_undir.edges())


    toRemove = find_vertex(graph_undir,'A')
    print("\n Eliminazione Vertice", toRemove)
    graph_undir.remove_vertex(toRemove)
    print("Vertice eliminato con successo: ", toRemove not in graph_undir.vertices())

    print("\n\nTest su grafo DIRETTO")
    a = find_vertex(hubs_dir, "BOS")
    b = find_vertex(hubs_dir, "JFK")
    toRemove = hubs_dir.get_edge(a,b)
    hubs_dir.remove_edge(toRemove)
    print("eliminazione di: ", toRemove)
    print("Edge eliminato con successo: ", toRemove not in hubs_dir.edges())

    toRemove = find_vertex(hubs_dir, 'JFK')
    print("\n Eliminazione Vertice", toRemove)
    hubs_dir.remove_vertex(toRemove)
    print("Vertice eliminato con successo: ", toRemove not in hubs_dir.vertices())

    print('\n\n----------------Test Esercizio 3----------------')
    print("\n\n Componenti connesse di graph_undir")
    c = components(graph_undir)
    for k in c:
        print(c[k], k)
    print("\n\n Componenti connesse di zebra_edges")
    c = components(zebra_edges)
    for k in c:
        print(c[k], k)
    print('\n\n----------------Test Esercizio 4----------------')

    rhesus_edges = load_graph(open(RHESUS), True)
    print("ricerca ciclo in rhesus_edges:")
    cycle = find_cycle(rhesus_edges, find_vertex(rhesus_edges,'6'))
    print("Ciclo trovato: ", cycle is not None)
    if cycle is not None:
        for el in range(0,len(cycle)):
            print(cycle[el])

    hubs_dir = load_graph(open(HUBS), True)
    vertex = find_vertex(hubs_dir, 'JFK')
    print("ricerca ciclo in hubs_dir per ",vertex)
    cycle = find_cycle(hubs_dir, vertex)
    print("Ciclo trovato: ", cycle is not None)
    if cycle is not None:
        for el in range(0,len(cycle)):
            print(cycle[el])
    print('Eliminazione vertice BOS e ricerca di un nuovo ciclo')
    hubs_dir.remove_vertex(find_vertex(hubs_dir,'BOS'))
    print("Ciclo trovato: ", find_cycle(hubs_dir, vertex) is not None)

    vertex = find_vertex(hubs_dir, 'LAX')
    print("ricerca ciclo in hubs_dir per ",vertex)
    cycle = find_cycle(hubs_dir, vertex)
    print("Ciclo trovato: ", cycle is not None)
    if cycle is not None:
        for el in range(0,len(cycle)):
            print(cycle[el])