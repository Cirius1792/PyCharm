from random import randint

def fib1(n):
    """returns the nth element of the sequence of Fibonacci numbers"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib1(n - 1) + fib1(n - 2)


def fib2(n, l=[]):
    """returns a list containing the sequence of Fibonacci numbers from 0 to n"""

    if n == 0:
        l.append(0)
        return l
    elif n == 1:
        fib2(n - 1, l)
        l.append(1)
        return l
    else:
        fib2(n - 1, l)
        v = l[n - 1] + l[n - 2]
        l.append(v)
        return l


def rimuovi(L):
    """removes all the duplicated elements in L"""

    tmp = []
    for e in L:
        if e not in tmp:
            tmp.append(e)
    L.clear()
    L.extend(tmp)


def espandi(L):
    """starting from the list L, the function returns a new list containing all the elements of L, followed
    by the sum of all the previous elements"""
    tmp = []
    for i in range(0, len(L)):
        v = 0
        tmp.append(L[i])
        for j in range(0, i + 1):
            v += L[j]
        tmp.append(v)
    return tmp


def frequenza(s):
    """for the given string s, the function creates a dictionary containing the number of the occurrence for
    each character"""
    occorrenze = dict()

    for c in s:
        v = occorrenze.get(c, 0)
        occorrenze.update({c: v + 1})
    return occorrenze


def mischia(L):
    """the function provides a random sorting for the string L"""
    for i in range(0,len(L)):
        r = randint(i, len(L)-1)
        L[i], L[r] = L[r], L[i]


def media(libretto, corso_laurea = {'TDP': 9,'CCA': 9, 'ENS': 6, 'I': 5 }):
    """the function provides the weighted average basing on the grades for each exam and its CFU, according to
    the default dictionary"""
    s = libretto.keys()
    media = 0;
    cfu = 0;
    for e in s:
        media += libretto[e]*corso_laurea[e]
        cfu += corso_laurea[e]
    media_pesata = media/cfu
    return media_pesata




# Fibonacci
print('Funzioni Fibonacci:')
print('fib(2)= ', fib1(2), '\nfib1(9) = ', fib1(9), '\nfib1(10) = ', fib1(10))
# sequenza di Fibonacci
print('fib2(6) = ', fib2(6))

# Funzione Rimuovi
L = [1, 1, 3, 4, 7, 3, 4, 1]
E = []
print('\n\nFunzione Rimuovi:')
print(L)
rimuovi(L)
print(L)
rimuovi(E)

# Espandi
L = [1, 3, 7, 4]
print('\n\nFunzione Espandi:')
print(L)
L2 = espandi(L)
print(L2)
espandi(E)

#Frequenza
print("\n\nFunzione Frequenza: \nparola: aiuola")
print(frequenza('aiuola'))

# mischia
print("\n\nFunzione Mischia:")
L = [1, 2, 3, 4, 5, 6, 7]
L1 = [8, 9, 10, 11]
print(L)
print(L1)
mischia(L)
mischia(L1)
print(L)
print(L1)
mischia(E)

#Media
print('\n\nFunzione Media:')
libretto = {'TDP': 30,'CCA': 22, 'ENS': 27, 'I': 28 } #media pesata: 26.55 media: 26.75
libretto2 = {'TDP': 30, 'ENS': 27, 'I': 28 }
libretto3 = {'TDP': 30 }
print('libretto: ',libretto)
print('media ponderata: ',media(libretto))
print('libretto: ',libretto2)
print('media ponderata: ',media(libretto2))
print('libretto: ',libretto3)
print('media ponderata: ',media(libretto3))


