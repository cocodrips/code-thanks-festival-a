def partial_sum(table, r1, r2, c1, c2):
    s = table[r2][c2]
    if r1 > 0:
        s -= table[r1 - 1][c2]
    if c1 > 0:
        s -= table[r2][c1 - 1]
    if r1 > 0 and c1 > 0:
        s += table[r1 - 1][c1 - 1]
    return s


R, C, M = map(int, raw_input().split())
N = int(raw_input())

array = [[0 for _ in xrange(C)] for _ in xrange(R)]

rcs = []
for i in xrange(N):
    r1, r2, c1, c2 = map(int, raw_input().split())
    rcs.append([r1 - 1, r2 - 1, c1 - 1, c2 - 1])
    for r in xrange(r1 - 1, r2):
        for c in xrange(c1 - 1, c2):
            array[r][c] += 1

table_0 = [[0 for _ in xrange(C)] for _ in xrange(R)]
table_1 = [[0 for _ in xrange(C)] for _ in xrange(R)]

for r in xrange(R):
    for c in xrange(C):
        total_0 = 0
        total_1 = 0
        if c != 0:
            total_0 += table_0[r][c - 1]
            total_1 += table_1[r][c - 1]
        if r != 0:
            total_0 += table_0[r - 1][c]
            total_1 += table_1[r - 1][c]
        if c != 0 and r != 0:
            total_0 -= table_0[r - 1][c - 1]
            total_1 -= table_1[r - 1][c - 1]
        table_0[r][c] = total_0 + (1 if array[r][c] % 4 == 0 else 0)
        table_1[r][c] = total_1 + (1 if array[r][c] % 4 == 1 else 0)

base = table_0[R - 1][C - 1]
count = 0
for i, rc in enumerate(rcs):
    if base - partial_sum(table_0, rc[0], rc[1], rc[2], rc[3]) + partial_sum(table_1, rc[0], rc[1], rc[2], rc[3]) == M:
        print i + 1
