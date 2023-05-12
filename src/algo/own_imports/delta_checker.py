def deltaBelowZeroChecker(a, b, c):
    delta = b*b - 4 * a * c
    if delta < 0:
        return 0
    if delta == 0:
        return 1
    if delta > 0:
        return 2 