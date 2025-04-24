def order_weight(strng):
    numbers = strng.split()
    weights = []
    for i in numbers:
        s = 0
        for j in i:
            s += int(j)
        weights.append([s, i])
    x = [i[1] for i in sorted(weights)]
    res = ''
    for i in x:
        if res == '':
            res = i
        else:
            res = res + ' ' + i
    return res
