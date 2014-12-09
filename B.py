if __name__ == "__main__":
    n = int(raw_input())
    a = int(raw_input())
    b = int(raw_input())
    c = int(raw_input())
    m = [a,b,c]
    m.sort(reverse=True)
    t = 0
    nn = 0
    while nn < n:
        nn += m[t % 3]
        t += 1
    print t