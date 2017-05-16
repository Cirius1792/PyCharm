
def edit_distance(s1, s2):
    m, n = len(s1)+1, len(s2)+1
    d = [[0 for x in range(n)] for y in range(m)]
    for i in range(m):
        d[i][0] = i
    for j in range(n):
        d[0][j] = j
    for i in range(1, m):
        for j in range(1, n):
            d[i][j] = min(d[i-1][j-1] if s1[i-1] == s2[j-1] else (d[i-1][j-1] + 1),
                          d[i-1][j] + 1,
                          d[i][j-1] + 1)
    return d

def edit_distance2(s1, s2):
#    if len(s2) > len(s1):
#        return edit_distance2(s2,s1)
    m, n = len(s1)+1, len(s2)+1
    v = [x for x in range(n)]
    for i in range(1, m):
        prev, v[0] = v[0], i
        for j in range(1, n):
            v[j], prev = min(prev if s1[i - 1] == s2[j - 1] else prev + 1,
                             v[j - 1] + 1,
                             v[j] + 1), v[j]
    return v[-1]

def print_edit_transfer(d):
    I = 'I'
    R = 'R'
    D = 'D'
    M = 'M'
    i, j = len(d)-1, len(d[0])-1
    cur = d[i][j]
    stk = []
    while cur != 0:
        if d[i-1][j] < cur:
            stk.append(D)
            i -= 1
        elif d[i][j-1] < cur:
            stk.append(I)
            j -= 1
        elif d[i-1][j-1] < cur:
            stk.append(R)
            j -= 1
            i -= 1
        else:
            stk.append(M)
            j -= 1
            i -= 1
        cur = d[i][j]
    transcript = ""
    for i in range(len(stk)):
        transcript += stk.pop()
    return transcript

def coin_change(amount_rem, coin_combinations=[50, 20, 10, 5, 2, 1]):

    #coin_combinations = [6, 2]
    coin_list = []
    for coin_val in coin_combinations:
        coin_count = amount_rem//coin_val
        coin = coin_val * coin_count
        for i in range(int(coin_count)):
            coin_list.append(coin_val)
        amount_rem = round(amount_rem - coin_val * coin_count, 2)
        if amount_rem == 0:
            return coin_list
    if amount_rem > 0:
        return []

def original_coin_change(amount_rem):
    coin_combinations = [50, 20, 10, 5, 2, 1]  # coin_combina9ons = [6, 2]
    coin_list = []
    for coin_val in coin_combinations:
        coin_count = amount_rem // coin_val
        coin_list += [coin_val] * coin_count
        amount_rem -= coin_val * coin_count
    if amount_rem == 0:
        return coin_list
    if amount_rem > 0:
        return []

def knapsak(x, v, P):
    n = len(x)
    d = [[0] * P for x in range(0, n)]
    a = [0 for i in range(0,n)]
    for i in range(1,n):
        for j in range(1, P):
            if j >= x[i-1]:
                if d[i - 1][j] > d[i - 1][j - x[i - 1]] + v[i - 1]:
                    d[i][j] = d[i - 1][j]
                    a[i - 1] = 0
                else:
                    d[i][j] = d[i - 1][j - x[i - 1]] + v[i - 1]
                    a[i - 1] = 1
            else:
                d[i][j] = d[i-1][j]
                a[i-1] = 0
    return d, a

def print_matrix(mtr):
    for a in mtr:
        ln = ""
        for i in a:
            ln += str(i) + " "
        print(ln)
def test1():
    s2 = "writers"
    s1 = "vintner"
    mtr = edit_distance(s1, s2)
    print_matrix(mtr)

    dist = edit_distance2(s1, s2)
    print(dist)

    r = print_edit_transfer(mtr)
    print(r)
    print("\n\nCoin Change:")
    money = 2.99
    print("resto di",money, ':', coin_change(money, [2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]))
    #print("resto di", money, ':', coin_change(money))

def test_knapsak():

    x = [3, 4, 5, 8, 10]
    p = [2, 3, 4, 5, 9]
    W = 20
    d, a = knapsak(x, p, W)
    print("matrice:")
    print_matrix(d)
    print("peso:\t\t\t",x)
    print("valore:\t\t\t", p)
    print("presi:\t\t\t", a)



if __name__ == "__main__":
    test_knapsak()