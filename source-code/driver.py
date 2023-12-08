import common as com
import functions as fun
import re

while 1:
    com.clr_screen()

    comm = input("Enter the calculation you want me to do :) ")
    comm = [*comm]
    comm = [i for i in comm if i != " "]
    x = []
    y = []
    f = []
    i = 0

    while i < len(comm) and com.isnum(comm[i]):
        x.append(int(comm[i]))
        i += 1
    f.append(comm[i])
    i += 1
    while i < len(comm):
        y.append(int(comm[i]))
        i += 1
    x.reverse()
    y.reverse()

    s = 1
    match f[0]:
        case "+":
            z = fun.add(x, y)
        case "-":
            z, s = fun.sub(x, y)
        case "*":
            z = fun.mul(x, y)
        case "/":
            z = fun.div(x, y)
        case "^":
            z = fun.exp(x, y)
        case "%":
            z = fun.perc(x, y)

    z = com.list_to_int(z)
    z *= s
    print(f"You answer is {z}")

    more = input("Do you want to do more calculations? (y/n) ")
    if more == "y":
        continue
    else:
        com.clr_screen()
        print("Buh bye <3")
        break
