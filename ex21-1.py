def math(a, b, c, d):
    return a + b * c - d


def math2(a, b, *argv):
    print(len(argv))
    return a + b * argv[0] - argv[1]


reslut = math(100, 200, 300, 400)
print(reslut)

reslut2 = math2(100, 200, 300, 400, 500)
print(reslut2)
