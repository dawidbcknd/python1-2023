def twoResultData(a, b, c):
    delta = b*b - 4 * a * c
    x1 = (-b - delta) / (2*a)
    x2 = (-b + delta) / (2*a)
    x1 = round(x1, 2)
    x2 = round(x2, 2)
    result = f"Delta wynosi: {delta}\nx1 wynosi: {x1}\nx2 wynosi: {x2}"
    return result