class Empty(Exception):
  pass

class ArrayStack:
  """Implmentazione di ADT Stack che utilizza un oggetto list di Python per la memorizzazione."""

  def __init__(self):
    """Crea uno stack vuoto."""
    self._data = []                       # instanza di list non pubblica

  def __len__(self):
    """Restituisce il numero di elementi nello stack."""
    return len(self._data)

  def is_empty(self):
    """Restituisce True se lo stack è vuoto."""
    return len(self._data) == 0

  def push(self, e):
    """Aggiunge l'elemento e al top dello stack."""
    self._data.append(e)                  # il nuovo elemento è aggiunto in coda alla list

  def top(self):
    """Restituisce (m anon rimuove) l'elemento al top dello stack.
       Raise Empty exception se lo stack è vuoto."""
    if self.is_empty():
      raise Empty('lo stack è vuoto')
    return self._data[-1]                 # legge l'ultimo elemento della list

  def pop(self):
    """Rimuove e restituisce l'elemento al top dello stack.
       Raise Empty exception se lo stack è vuoto."""
    if self.is_empty():
      raise Empty('lo stack è vuoto')

    return self._data.pop()               # rimuove l'ultimo elemento della list

if __name__ == '__main__':
    S = ArrayStack()                 # contents: [ ]
    try:
      S.pop()
    except Empty as e:
      print(e)
    S.push(5)                        # contents: [5]
    S.push(3)                        # contents: [5, 3]
    print(len(S))                    # contents: [5, 3];    outputs 2
    print(S.pop())                   # contents: [5];       outputs 3
    print(S.is_empty())              # contents: [5];       outputs False
    print(S.pop())                   # contents: [ ];       outputs 5
    print(S.is_empty())              # contents: [ ];       outputs True
    S.push(7)                        # contents: [7]
    S.push(9)                        # contents: [7, 9]
    print(S.top())                   # contents: [7, 9];    outputs 9
    S.push(4)                        # contents: [7, 9, 4]
    print(len(S))                    # contents: [7, 9, 4]; outputs 3
    print(S.pop())                   # contents: [7, 9];    outputs 4
    S.push(6)                        # contents: [7, 9, 6]
    S.push(8)                        # contents: [7, 9, 6, 8]
    print(S.pop())                   # contents: [7, 9, 6]; outputs 8

