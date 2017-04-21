from ADT.Queue.AbstractQueue import Queue


class ArrayQueue(Queue):

    def __init__(self, dim=20):
        """inizializza la coda"""
        self._data = [None] * dim
        self._size = 0
        self._front = 0
        self._N = dim

    def enqueue(self, e):
        """aggiunge l'elemento e alla coda"""

        if self._size == self._N:
            self._resize()

        self._data[(self._front + self._size) % self._N] = e
        self._size += 1

    def dequeue(self):
        """rimuove e restituisce l'elemento in testa alla coda"""

        if self.is_empty():
            raise Empty('Queue is empty')

        e = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._N
        self._size -= 1
        return e

    def __len__(self):
        """restituisce le dimensioni della coda"""

        return self._size

    def is_empty(self):
        """restituisce true se la coda è vuota"""

        return self._size == 0

    def first(self):
        """restituisce l'elemento in testa alla coda, senza rimuoverlo"""

        return self._data[self._front]

    def _resize(self):
        """funzione privata per il ridimensionamento della coda, una volta piena"""

        data_n = [None] * (2 * self._N)
        for i in range(0, self._size):
            data_n[i] = self._data[(self._front + i) % self._N]
        self._data = data_n
        self._N *= 2
        self._front = 0

    def print_elements(self):
        l = [None] * self._size
        for i in range(0, self._size):
            l[i] = self._data[(self._front + i) % self._N]
        print(l)


class Empty(Exception):
    pass
