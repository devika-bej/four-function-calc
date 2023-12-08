import subprocess as sp


def clr_screen():
    clr = sp.call("clear", shell=True)


def cont():
    cont = input("press enter to continue")


def isnum(n):
    return n >= "0" and n <= "9"


def list_to_int(x):
    y = 0
    fac = 1
    for i in x:
        y = y + i * fac
        fac *= 10
    return y


def equalize(x, y):
    i = 0
    while i < max(len(x), len(y)):
        if i < len(x) and i < len(y):
            i += 1
            continue
        if i < len(x):
            y.append(0)
            i += 1
            continue
        if i < len(y):
            x.append(0)
            i += 1
            continue
    x.append(0)
    y.append(0)
    return x, y


def deci_complement(x, ind):
    for i in range(0, ind):
        x[i] = 10 - x[i]
    return x