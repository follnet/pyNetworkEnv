def print_two(*args):
    # args实际为list
    # arg1, arg2 = args
    # print("arg1: %s, arg2: %s" % (arg1, arg2))
    print("arg1: %s, arg2: %s" % (args[0], args[1]))


def print_two_again(arg1, arg2):
    print("arg1: %s, arg2: %s" % (arg1, arg2))


def print_one(arg1):
    print("arg1: %s" % (arg1))


def print_none():
    print("I got nothin'.")


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
