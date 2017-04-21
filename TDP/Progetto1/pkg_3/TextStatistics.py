from TdP_collections.map.binary_search_tree import TreeMap
from TdP_collections.map.avl_tree import AVLTreeMap
from TdP_collections.map.red_black_tree import RedBlackTreeMap
from TdP_collections.priority_queue.heap_priority_queue import HeapPriorityQueue
import math
from heapq import nlargest



class TextStatistics:
    """permette di elaborare statistiche su un insieme di stringhe. La classe deve utilizzare un albero binario di
    ricerca bilanciato i cui nodi contengono elementi (key, value) dove key è una stringa e value è il numero di
    occorrenze della stringa nel dataset. Il costruttore della classe deve prendere in input il nome di un file di testo
    che rappresenta il dataset."""

    __slots__ = 'words', 'size', 'word_lenght'

    def _factory(self):
        self.words = TreeMap()
    def __init__(self, path):

        self._factory()
        self.size = 0
        self.word_lenght = 0

        f = open(path)
        txt = f.read()
        f.close()
        dataset = txt.split()
        for w in dataset:
            self.add(w)

    def add(self, key):
        if key in self.words:
            self.words[key] += 1
        else:
            self.words[key] = 1
            self.size += 1
            self.word_lenght += len(key)

    def delete(self, key):
        if key in self.words:
            if self.words[key] > 1:
                self.words[key] -= 1
            else:
                del self.words[key]
                self.word_lenght -= len(key)

    def __len__(self):
        return self.size

    def average(self):
        """restituisce la lunghezza media delle key della mappa"""
        return self.word_lenght/self.size

    def devStd(self):
        """restituisce la deviazione standard delle lunghezze delle key"""
        avg = self.average()
        t = 0
        for el in self.words:
            t += pow((len(el) - avg), 2)
        dev = math.sqrt(t/self.size)
        return dev

    def mostFrequent(self, j):
        """restituisce la lista delle j key più frequenti"""
        #l = nlargest(j, self.words, key=self.words.get)
        hp = HeapPriorityQueue()
        for key in self.words:
            hp.add(-(self.words[key]), key)
        l = []
        for i in range(1, j+1):
            l.append(hp.remove_min()[1])
        return l

    def quartile(self, j = 1):
        """(FACOLTATIVO) restituisce il j-imo quartile, per j = 1, 2,
            3, delle lunghezze delle key;"""
        pass


t = TextStatistics("/Users/CLT/Desktop/Text-1.txt")
print("average:\t", t.average())
print("deviazione standart:\t", t.devStd())
print("5 parole più frequenti:\t", t.mostFrequent(5))