def inverses(x):
    a = str(x)
    b = list(a)
    c = b[len(b)::-1]
    j = int(''.join(str(i) for i in c))
    return j


print(inverses(88406546))