from TDP.TdP_collections.priority_queue.adaptable_priority_queue import AdaptableHeapPriorityQueue
from TDP.TdP_collections.graphs.graph import Graph
def BellmaFord(G,s):

    d = {}

    for v in G.vertices():
        if v is s:
            d[v] = 0
        else:
            d[v] = float('inf')
        for i in range(len(G.vertices())-1):
            for e in G.edges():
                u, v =  e.endpoints()
                wgt = e.element()
                if d[u] + wgt < d[v]:
                    d[v] = d[u] + wgt