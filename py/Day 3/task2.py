def solution(s):
    X = []
    k = 0
    for i in range(0, len(s), 2):
        k += 1
        a = ''
        b = '_'
        try:
            b = s[i+1]
        except:
            pass
        X.append(''.join([s[i], b]))

    return X
