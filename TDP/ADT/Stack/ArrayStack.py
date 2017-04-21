from ADT.Stack.AbstractStack import Stack

class ArrayStack(Stack):

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


def test():
    stack = ArrayStack(5)
    print('is empty? ',stack.is_empty())

    print('push: 1')
    stack.push(1)
    print('push: 2')
    stack.push(2)
    print('push: 3')
    stack.push(3)

    print('top: ',stack.top())

    print('pop: ',stack.pop())

    print('top: ', stack.top())

    print('test resize')
    stack.push(4)
    stack.push(5)
    stack.push(6)
    stack.push(7)
    print(stack.top())
    print(stack.print_elements())
