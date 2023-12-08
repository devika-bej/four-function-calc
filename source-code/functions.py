import common as com


# x + y
def add(x, y):
    x, y = com.equalize(x, y)
    z = [0] * len(x)
    for i in range(0, len(x) - 1):
        t = x[i] + y[i] + z[i]
        if t < 10:
            z[i] = t
        else:
            z[i] = t % 10
            z[i + 1] += int(t / 10)
    return z


# x - y
def sub(x, y):
    rx = len(x)
    ry = len(y)
    x, y = com.equalize(x, y)
    z = [0] * len(x)
    s = 1
    ind = 0
    for i in range(0, len(x) - 1):
        if x[i] >= y[i]:
            z[i] = x[i] - y[i]
        else:
            pass


    return z, s


# x * y
def mul(x, y):
    pass


# x / y
def div(x, y):
    pass


# x ^ y
def exp(x, y):
    pass


# sqrt(x)
def sqrt(x):
    pass


# x % of y
def perc(x, y):
    pass
