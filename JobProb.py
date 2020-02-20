def chanceMoreThan(dict, value, distribute):
    s = 0
    c = 0
    for i in dict[distribute].keys():
        if float(i) > value:
            s = s + dict[distribute][i]
        c = c + dict[distribute][i]
    return {"sum": s, "total": c, "prob": s/c}

def chanceLowerThan(dict, value, distribute):
    s = 0
    c = 0
    for i in dict[distribute].keys():
        if float(i) < value:
            s = s + dict[distribute][i]
        c = c + dict[distribute][i]
    return {"sum": s, "total": c, "prob": s/c}

def average(dict, distribute):
    s = 0
    c = 0
    for i in dict[distribute].keys():
        s = s + (dict[distribute][i] * float(i))
        c = c + dict[distribute][i]
    return s/c
