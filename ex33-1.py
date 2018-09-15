def whileLoop(a, b):
    numbers = []
    while a < b:
        print("At the top a is %s" % (a))
        numbers.append(a)
        # a += 1
        a = add(a, 2)
        print("Numbers now: ", numbers)
        print("At the bottom a is ", a)
    return numbers


def add(c, d):
    return c + d


numbers = whileLoop(0, 6)

print("======")
print(numbers)
