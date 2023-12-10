import common as com
import functions as fun
import re

while 1:
    com.clr_screen()

    comm = input("Let me do the calculation you want <3 ")

    if comm == "0":
        com.clr_screen()
        print("Buh bye <3")
        break

    comm = [*comm]
    comm = [i for i in comm if i != " "]
    sx = 1
    x = []
    sy = 1
    y = []
    f = []
    i = 0

    if not com.syntax_check(comm):
        print("Sorry, I don't get what you mean")
        print("I think you entered the wrong syntax or broke the restriction :(")
        print("The correct syntax is x <symbol> y")
        print("Please read the note in the end of the README.md for restrictions")
        com.cont()
        continue

    if comm[i] == "-":
        sx = -1
        i += 1
    elif comm[i] == "+":
        sx = 1
        i += 1
    while i < len(comm) and com.isnum(comm[i]):
        x.append(int(comm[i]))
        i += 1
    f.append(comm[i])
    i += 1
    if comm[i] == "-":
        sy = -1
        i += 1
    elif comm[i] == "+":
        sy = 1
        i += 1
    while i < len(comm):
        y.append(int(comm[i]))
        i += 1
    x.reverse()
    y.reverse()

    s = 1
    match f[0]:
        case "+":
            z, s = fun.add(x, sx, y, sy)
        case "-":
            z, s = fun.sub(x, sx, y, sy)
        case "*":
            z, s = fun.mul(x, sx, y, sy)
        case "/":
            z, s = fun.div(x, sx, y, sy)
        case "^":
            z, s = fun.exp(x, sx, y)
        case "%":
            z = fun.perc(x, y)
    if s != 0:
        z = com.list_to_int(z)
        z *= s
        print(f"Your answer is {z}")
    else:
        print("Your answer is NaN")

    f = 1
    while 1:
        more = input("Do you want to do more calculations? (y/n) ")
        if more == "y":
            f = 0
            break
        elif more == "n":
            com.clr_screen()
            print("Buh bye <3")
            break
        else:
            print("Sorry, what do you mean?")
    if f:
        break
