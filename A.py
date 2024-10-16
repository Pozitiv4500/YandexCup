from decimal import Decimal

p = dict()
s = Decimal("0")

while True:
    string = str(input()).strip()

    if string == "!":
        exit()

    if string[0] == "+":
        _, id_, t = string.split()
        p[id_] = Decimal(t)
        s += p[id_]

    if string[0] == "-":
        _, id_ = string.split()
        if id_ in p.keys():
            s -= p[id_]
            p.pop(id_)

    if string[0] == "~":
        _, id_, t = string.split()
        if id_ in p.keys():
            s -= p[id_]
            p[id_] = Decimal(t)
            s += p[id_]

    if string[0] == "?":
        if len(p) == 0:
            print(0.0, flush=True)
        else:
            print(round(s / Decimal(str(len(p))), 10), flush=True)
