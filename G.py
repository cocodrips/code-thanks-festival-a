# -*- coding: utf-8 -*-
if __name__ == "__main__":
    N, K = map(int, raw_input().split())

    pp = []
    for i in xrange(N):
        pp.append(int(raw_input()))

    dp = [[[0.0 for _ in xrange(K + 1)] for _ in xrange(K + 1)] for _ in xrange(N + 1)]
    dp[1][1][0] = 1.0

    for n in xrange(1, N):
        for j in xrange(K + 1):
            for i in xrange(j / 2 + 1):
                if dp[n][j][i] == 0: # これないとTLE
                    continue
                #seat
                p = pp[n] / 100.0
                if i > 0:
                    dp[n + 1][j][i - 1] += p * dp[n][j][i]
                elif j + 1 <= K:
                    dp[n + 1][j + 1][i] += p * dp[n][j][i]

                #skip
                if j + 2 <= K:
                    dp[n + 1][j + 2][i + 1] += (1 - p) * dp[n][j][i]
                else:
                    dp[n + 1][j][i] += (1 - p) * dp[n][j][i]

    s = 0
    # print dp[N]
    for i in xrange(K + 1):
        for j in xrange(K + 1):
            p = (i + K - j) * dp[N][j][i]
            s += p
    print s