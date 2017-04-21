class Stack:
  """Classe astratta che implementa l'ADT Queue."""

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
