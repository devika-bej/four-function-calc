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
    s = 1
    if rx < ry:
        t = x
        x = y
        y = t
        s = -1
    if rx == ry:
        i = rx - 1
        while i >= 0 and x[i] == y[i]:
            i -= 1
        if i >= 0 and x[i] < y[i]:
            t = x
            x = y
            y = t
            s = -1
    x, y = com.equalize(x, y)
    z = [0] * len(x)
    ind = 0
    for i in range(0, len(x) - 1):
        if x[i] >= y[i]:
            z[i] = x[i] - y[i]
        else:
            j = i + 1
            while j < rx and x[j] == 0:
                x[j] = 9
                j += 1
            x[j] -= 1
            x[i] += 10
            z[i] = x[i] - y[i]

    return z, s


# x * y
def mul(x, y):
    rx = len(x)
    ry = len(y)
    z = []
    i = 0
    while i < rx:
        t = [0] * (i + ry + 1)
        j = i
        for k in y:
            p = k * x[i]
            t[j] += p % 10
            t[j + 1] += int(p / 10)
            j += 1
        i += 1
        z = add(z, t)
    return z


# x / y
def div(x, y):
    z = []
    s = 1
    while s == 1:
        x, s = sub(x, y)
        if s == 1:
            z = add(z, [1])
    return z


# x ^ y
def exp(x, y):
    z = [1]
    while com.list_to_int(y) > 0:
        y, s = sub(y, [1])
        if com.list_to_int(y) >= 0:
            z = mul(x, z)
    return z


# x % of y
def perc(x, y):
    pass
