from TDP.TdP_collections.map.binary_search_tree import TreeMap
from TDP.TdP_collections.priority_queue.heap_priority_queue import HeapPriorityQueue
from TDP.Progetto1.pkg_4.ReverseHeap import reverse_heap_priority_queue
import math
import time




class TextStatistics:
    """permette di elaborare statistiche su un insieme di stringhe. La classe deve utilizzare un albero binario di
    ricerca bilanciato i cui nodi contengono elementi (key, value) dove key è una stringa e value è il numero di
    occorrenze della stringa nel dataset. Il costruttore della classe deve prendere in input il nome di un file di testo
    che rappresenta il dataset."""


    __slots__ = 'words', 'word_lenght'

    def __init__(self, path, tree):

        self.words = tree
        self.word_lenght = 0
        f = open(path)
        for line in f:
            for word in line.split():
                self.add(word.lower())
        f.close()

    def add(self, key):
        if key in self.words:
            self.words[key] += 1
        else:
            self.words[key] = 1
            self.word_lenght += len(key)

    def delete(self, key):
        if key in self.words:
            if self.words[key] > 1:
                self.words[key] -= 1
            else:
                del self.words[key]
                self.word_lenght -= len(key)

    def __len__(self):
        return len(self.words)

    def average(self):
        """restituisce la lunghezza media delle key della mappa"""
        return self.word_lenght/len(self.words)

    def devStd(self):
        """restituisce la deviazione standard delle lunghezze delle key"""
        avg = self.average()
        t = 0
        for el in self.words:
            t += pow((len(el) - avg), 2)
        dev = math.sqrt(t/len(self.words))
        return dev

    def mostFrequent(self, j):
        """restituisce la lista delle j key più frequenti"""

        hp = reverse_heap_priority_queue()
        for key in self.words:
            hp.add((self.words[key]), key)
        l = []
        for i in range(1, j+1):
            tmp = hp.remove_min()
            t = str(tmp[1])+":"+str(tmp[0])
            l.append(t)
        return l

    def quartile(self, j = 1):
        """(FACOLTATIVO) restituisce il j-imo quartile, per j = 1, 2,
            3, delle lunghezze delle key;"""
        l = []
        for key in self.words:
            self._sorted_insert(l, len(key))
        quartile = 0
        if j == 1:
            quartile = self._qt(l[:int(len(l)/2)])
        elif j == 2:
            quartile = self._qt(l)
        elif j == 3:
            quartile = self._qt(l[int(len(l)/2):])
        return quartile

    def _qt(self, l):
        flag = (len(l) % 2)
        if flag:
            quartile = l[int(len(l) / 2)]
        else:
            quartile = (l[int(len(l) / 2)] + l[int(len(l) / 2) - 1]) / 2
        return quartile

    def _sorted_insert(self, l, obj):
        i = 0
        while i < len(l) and l[i] < obj:
            i += 1
        l.insert(i, obj)


start = time.time()
t = TextStatistics('/Users/CLT/Desktop/Text-2.txt', TreeMap())
stop = time.time()
# print("tempo richiesto per l'elaborazione: ", stop-start)
# print("numero parole: ",len(t))
print("average:\t", t.average())
print("deviazione standart:\t", t.devStd())
# #print("5 parole più frequenti:\t", t.mostFrequent(5))
print("quartile 1: ", t.quartile(1))
print("quartile 2: ", t.quartile(2))
print("quartile 3: ", t.quartile(3))
