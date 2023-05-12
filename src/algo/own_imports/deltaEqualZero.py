def oneResultData(a, b, c):
    delta = b*b - 4 * a * c
    x0 = -b / (2*a)
    x0 = round(x0, 2)
    result = f"Delta wynosi: {delta}\nx0 wynosi: {x0}"
    return result