import common as com


# x + y
def add(x, sx, y, sy):
    if sx == sy:
        x, y = com.equalize(x, y)
        z = [0] * len(x)
        for i in range(0, len(x) - 1):
            t = x[i] + y[i] + z[i]
            t = str(t)
            t = [*t]
            t = [int(k) for k in t]
            if len(t) == 1:
                z[i] = t[0]
            else:
                z[i] = t[1]
                z[i + 1] += t[0]
        return z, sx
    else:
        z, s = sub(x, 1, y, 1)
        if sx == 1:
            return z, s
        else:
            return z, -s


# x - y
def sub(x, sx, y, sy):
    if sx == sy:
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
        return z, s * sx
    else:
        z, s = add(x, 1, y, 1)
        return z, sx


# x * y
def mul(x, sx, y, sy):
    rx = len(x)
    ry = len(y)
    z = []
    i = 0
    while i < rx:
        t = [0] * (i + ry + 1)
        j = i
        for k in y:
            p = k * x[i]
            p = str(p)
            p = [*p]
            if len(p) == 1:
                t[j] += p[0]
            else:
                t[j] += p[1]
                t[j + 1] += p[0]
            j += 1
        i += 1
        z, s = add(z, 1, t, 1)
    return z, sx * sy


# x / y
def div(x, sx, y, sy):
    z = []
    sd = 1
    while sd == 1:
        x, sd = sub(x, 1, y, 1)
        if sd == 1:
            z, s = add(z, 1, [1], 1)
    if sx == sy:
        return z, 1
    else:
        z, s = add(z, 1, [1], 1)
        return z, -1


# x ^ y
def exp(x, sx, y):
    z = [1]
    while com.list_to_int(y) > 0:
        y, s = sub(y, 1, [1], 1)
        if com.list_to_int(y) >= 0:
            z = mul(x, 1, z, 1)
    if y % 2 == 0:
        s = 1
    else:
        s = sx
    return z, s


# x % of y
def perc(x, y):
    z = mul(x, y)
    z.insert(2, ".")
    return z
