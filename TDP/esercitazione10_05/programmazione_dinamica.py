
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
    m, n = len(s1)+1, len(s2)+1
    v = [x for x in range(m)]

    for i in range(1, m):
        prev, v[0] = v[0], i
        
        for j in range(1, n):
            v[j] = min(min(v),prev if s1[i-1] == s2[j-1] else prev +1)

    return 0

def print_matrix(mtr):
    for a in mtr:
        ln = ""
        for i in a:
            ln += str(i) + " "
        print(ln)

mtr = edit_distance("winter","writers")
print_matrix(mtr)

dist = edit_distance2("writers","winter")
