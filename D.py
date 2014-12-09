# -*- coding: utf-8 -*-
if __name__ == "__main__":
    N, Q = map(int, raw_input().split())
    for i in xrange(Q):
        a,b,s,t =  map(int, raw_input().split())

        if s <= a <= t and s <= b <= t:
            print ((t - s) - (b - a)) * 100
        elif a <= s and s <= b <= t:
            print (t - b) * 100
        elif s <= a <= t and t <= b:
            print (a - s) * 100
        elif a <= s and t <= b:
            print 0
        else:
            print (t - s) * 100

# もっときれいなの
#         max(o, min(b,t) - max(a,s))