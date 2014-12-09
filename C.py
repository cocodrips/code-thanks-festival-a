if __name__ == "__main__":
    n, m = map(int, raw_input().split())
    score = map(int, raw_input().split())
    ans = map(int, raw_input().split())

    s = 0
    for a in ans:
        s += score[a - 1]

    print s
