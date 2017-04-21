from TdP_collections.text.find_boyer_moore import find_boyer_moore

def find_brute_all(T, P):
  """Restituisce l'inizio di ogni occorrenza del pattern P in T"""

  n, m = len(T), len(P)                      # introduce convenient notations
  l = []                                     # list of founded occurrences
  for i in range(n-m+1):                     # try every potential starting index within T
    k = 0                                    # an index into pattern P
    while k < m and T[i + k] == P[k]:        # kth character of P matches
      k += 1
    if k == m:                               # if we reached the end of pattern,
      l.append(i)                            # substring T[i:i+m] matches P
  return l                                   # failed to find a match starting with any i

def find_boyer_moore_all(T, P):
  """Return the lowest index of T at which substring P begins (or else -1)."""
  n, m = len(T), len(P)                   # introduce convenient notations
  if m == 0: return 0                     # trivial search for empty string
  last = {}                               # build 'last' dictionary
  occurrences = []
  for k in range(m):
    last[ P[k] ] = k                      # later occurrence overwrites
  # align end of pattern at index m-1 of text
  i = m-1                                 # an index into T
  k = m-1                                 # an index into P
  flag = -1
  while i < n:
      if T[i] == P[k]:  # a matching character
          if flag == -1:
              flag = i + 1
          if k == 0:
              if i not in occurrences:
                occurrences.append(i)  # add to the list the index of the beginngin of the ocurrence
              i = flag
              k = m - 1
              flag = -1
          else:
              i -= 1  # examine previous character
              k -= 1  # of both T and P
      else:
          j = last.get(T[i], -1)  # last(T[i]) is -1 if not found
          i += m - min(k, j + 1)  # case analysis for jump step
          k = m - 1                           # restart at end of pattern
  return occurrences

def find_kmp_all(T, P):
    """Return the lowest index of T at which substring P begins (or else -1)."""
    n, m = len(T), len(P)  # introduce convenient notations
    if m == 0: return 0  # trivial search for empty string
    fail = compute_kmp_fail(P)  # rely on utility to precompute
    j = 0  # index into text
    k = 0  # index into pattern
    while j < n:
        if T[j] == P[k]:  # P[0:1+k] matched thus far
            if k == m - 1:  # match is complete
                return j - m + 1
            j += 1  # try to extend match
            k += 1
        elif k > 0:
            k = fail[k - 1]  # reuse suffix of P[0:k]
        else:
            j += 1
    return -1
def compute_kmp_fail(P):
  """Utility that computes and returns KMP 'fail' list."""
  m = len(P)
  fail = [0] * m                   # by default, presume overlap of 0 everywhere
  j = 1
  k = 0
  while j < m:                     # compute f(j) during this pass, if nonzero
    if P[j] == P[k]:               # k + 1 characters match thus far
      fail[j] = k + 1
      j += 1
      k += 1
    elif k > 0:                    # k follows a matching prefix
      k = fail[k-1]
    else:                          # no match found starting at j
      j += 1
  return fail

def test():
    txt = "occhiocchiociccioporcamiseriaocchiali"
    pattern = "occhi"
    print("testo:\t\t",txt)
    print("pattern:\t\t", pattern)
    l = find_brute_all(txt,pattern)
    print("brute:\n", l)
    l = find_boyer_moore_all(txt,pattern)
    print("boyer-moore:\n", l)
    l = find_kmp_all(txt,pattern)
    print("Knuth-Morris-Pratt:\n", l)

test()