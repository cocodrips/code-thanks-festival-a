if __name__ == "__main__":
    n, m = map(int, raw_input().split())
    # rank = range(n)
    win = [set() for i in xrange(n)]
    for i in xrange(m):
        a, b = map(int, raw_input().split())
        win[a - 1].add(b - 1)

    for k in xrange(n):
        for i in xrange(n):
            w_set = set()
            for w in win[i]:
                for ww in win[w]:
                    if ww != i:
                        w_set.add(ww)
            if w_set:
                win[i] |= w_set

    # print win

    rank = 1
    for i in xrange(1, n):
        if 0 in win[i]:
            rank += 1

    print rank
