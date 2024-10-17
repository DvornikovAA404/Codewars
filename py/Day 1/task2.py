import re
def order(sentence):
    a = []
    line = sentence
    if line == "":
        return ""
    else:
        s = line.split()
        for i in s:
            numbers = re.findall(r'\d', str(i))
            a.append([numbers[0], str(i)])

        print(a)
        a.sort()
        s = ""
        for i in range(len(a)):
            s += a[i][1] + " "
        return s[:-1]

print(order("a1 a2 z3") + "!")