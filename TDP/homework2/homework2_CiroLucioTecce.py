#HOMEWORK 2 -   CIRO LUCIO TECCE
#Le classi presenti nella prima parte dello script sono state utilizzate per lo svolgimento della traccia assegnata.


class Stack:
  """Classe astratta che descrive l'ADT Stack."""

  def __len__(self):
    """Restituisce il numero di elementi nello stack."""
    raise NotImplementedError('deve essere implementato dalla sottoclasse.')

  def is_empty(self):
    """Restituisce True se lo stack è vuoto."""
    raise NotImplementedError('deve essere implementato dalla sottoclasse.')

  def top(self):
    """Restituisce (ma non rimuove) l'elemento al top dello stack.
        Raise Empty exception se lo stack è vuoto."""
    raise NotImplementedError('deve essere implementato dalla sottoclasse.')

  def pop(self):
    """Rimuove e restituisce l'elemento al top dello stack.
        Raise Empty exception se lo stack è vuoto"""
    raise NotImplementedError('deve essere implementato dalla sottoclasse.')

  def push(self, e):
    """Aggiunge un elemento in top allo stack"""
    raise NotImplementedError('deve essere implementato dalla sottoclasse.')


class ArrayStack(Stack):
    """Implementazione di uno stack tramite Array"""

    def __init__(self, dim=20):
        """inizializza lo stack"""
        self._data = [None] * dim
        self._size = 0
        self._front = 0
        self._N = dim

    def push(self, e):
        """inserisce l'elemento nello stack"""
        if self._size == self._N:
            self._resize()

        self._front = ( self._front + self._N - 1) % self._N
        self._data[self._front] = e
        self._size += 1

    def pop(self):
        """rimuove l'elemento al top dallo stack e lo restituisce"""
        if self.is_empty():
            raise Empty('Queue is empty')

        e = self._data[self._front]
        self._data[self._front] = None
        self._front = ( self._front + self._N + 1) % self._N
        self._size -= 1
        return e

    def __len__(self):
        """restituisce le dimensioni dello stack"""
        return self._size

    def is_empty(self):
        """restituisce True se lo stack è vuoto"""
        return self._size == 0

    def top(self):
        """restituisce, senza rimuoverlo, l'elemento al top dello stack"""
        return self._data[self._front]

    def _resize(self):
        """funzione privata per il ridimensionamento dello stack, una volta pieno"""
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

# Svolgimento homework 2
class Dequeue():
    """Struttura dati misto fra coda e stack"""

    def add_first(self, e):
        raise NotImplementedError('deve essere implementato dalla sottoclasse.')

    def delete_first(self):
        raise NotImplementedError('deve essere implementato dalla sottoclasse.')

    def add_last(self, e):
        raise NotImplementedError('deve essere implementato dalla sottoclasse.')

    def delete_last(self):
        raise NotImplementedError('deve essere implementato dalla sottoclasse.')

    def first(self):
        raise NotImplementedError('deve essere implementato dalla sottoclasse.')

    def last(self):
        raise NotImplementedError('deve essere implementato dalla sottoclasse.')

    def is_empty(self):
        raise NotImplementedError('deve essere implementato dalla sottoclasse.')

    def __len__(self):
        raise NotImplementedError('deve essere implementato dalla sottoclasse.')


class ArrayDequeue(Dequeue):
    """implementa una Dequeue tramite  Array """

    DEFAULT_DIMENSION = 10

    def __init__(self, dim = DEFAULT_DIMENSION):
        """Inizializza la struttura dati, viene utilizzato un valore di default se non diversamente specificato"""
        self._data = [None] * dim
        self._size = 0
        self._front = 0
        self._N = dim

    def add_first(self, e):
        """aggiunge	l’elemento	e	al	front	della	coda"""

        if self._size == self._N:
            self._resize()

        self._front = ( self._front + self._N - 1) % self._N
        self._data[self._front] = e
        self._size += 1

    def delete_first(self):
        """restituisce	e	rimuove	l’elemento	al	front;	lancia	un	errore	se	la	coda
            è	vuota"""
        if self.is_empty():
            raise Empty('Queue is empty')

        e = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._N
        self._size -= 1
        return e

    def add_last(self, e):
        """aggiunge l’elemento e al back della coda"""
        if self._size == self._N:
            self._resize()

        self._data[(self._front + self._size) % self._N] = e
        self._size += 1

    def delete_last(self):
        """restituisce e rimuove l’elemento al back; lancia un errore se la coda è vuota"""
        if self.is_empty():
            raise Empty('Queue is empty')

        e = self._data[( self._front + self._size -1) % self._N]
        self._data[( self._front + self._size) % self._N] = None
        self._size -= 1
        return e

    def first(self):
        """restituisce, ma non rimuove, l’elemento al front della coda"""
        return self._data[self._front]

    def last(self):
        """restituisce, ma non rimuove, l’elemento al back della coda"""
        return self._data[ (self._front + self._size - 1) % self._N]

    def is_empty(self):
        """restituisce True se la coda è vuota"""
        return self._size == 0

    def __len__(self):
        """restituisce il numero di elementi presenti nella coda"""
        return self._size

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


def span(l):

    s = list()
    s.append(1)
    t = ArrayStack(len(l))
    t.push(0)

    for i in range(1, len(l)):
        while not t.is_empty() and l[t.top()] <= l[i]:
            t.pop()
        if t.is_empty():
            s.append(i + 1)
        else:
            s.append(i - t.top())
        t.push(i)
    return s


def test_dequeue():
    print("Test Dequeue")
    d = ArrayDequeue(10)
    print('add_last(5)')
    d.add_last(5)
    d.print_elements()
    print('add_first(3)')
    d.add_first(3)
    d.print_elements()
    print('add_first(7)')
    d.add_first(7)
    d.print_elements()

    print('first: ', d.first())
    print('delete_last: ', d.delete_last())
    print('len: ', len(d))
    print('delete_last: ', d.delete_last())
    print('delete_last: ', d.delete_last())

    print('add_first(6)')
    d.add_first(6)
    d.print_elements()
    print('last: ', d.last())
    print('add_first(8)')
    d.add_first(8)
    d.print_elements()
    print('is empty? ', d.is_empty())
    print('last: ', d.last())

    print('fine test dequeue\n\n')


def test_span():
    print('test span')
    l1 = [1, 4, 8, 7, 5, 10, 15, 12, 3, 9, 4, 5]
    s1 = span(l1)
    print(l1,'\nspan:')
    print(s1)


test_dequeue()
test_span()

