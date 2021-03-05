def square_root(sq):
    sq = float(sq)
    x = sq/2
    while True:
        y = (x + sq/x) / 2
        if x == y:
            break
        x = y
    return x

