import subprocess as sp


def clr_screen():
    clr = sp.call("clear", shell=True)


def cont():
    cont = input("Press enter to continue")


def isnum(n):
    return n >= "0" and n <= "9"


def list_to_int(x):
    y = 0
    fac = 1
    dec = []
    if len(x) > 2 and x[2] == ".":
        dec = x[:2]
        x = x[3:]
    for i in x:
        y = y + i * fac
        fac *= 10
    if dec:
        y += dec[1] / 10
        y += dec[0] / 100
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


def syntax_check(comm):
    # print("in syntax check we are checking ", comm)
    if len(comm) < 3:
        return False
    if not (isnum(comm[0]) or comm[0] == "-" or comm[0] == "+"):
        return False
    i = 1
    while i < len(comm) and isnum(comm[i]):
        i += 1
    if i == len(comm) or (i == 1 and not isnum(comm[0])):
        return False
    if not (
        comm[i] == "+"
        or comm[i] == "-"
        or comm[i] == "*"
        or comm[i] == "/"
        or comm[i] == "^"
        or comm[i] == "%"
    ):
        return False
    i += 1
    if i == len(comm):
        return False
    if not (isnum(comm[i]) or comm[i] == "-" or comm[i] == "+"):
        return False
    if comm[i - 1] == "^" and comm[i] == "-":
        return False
    if comm[i - 1] == "%" and (comm[0] == "-" or comm[i] == "-"):
        return False
    if not isnum(comm[i]):
        i += 1
    if i == len(comm):
        return False
    while i < len(comm) and isnum(comm[i]):
        i += 1
    if i != len(comm):
        return False
    return True
