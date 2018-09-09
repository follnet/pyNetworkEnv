print("Let's practice everything.")
print("You\'d need to know \'bout escapes with \\ that do:")
print("\n newlines and \t tabs.")

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of lovely
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("-----------------------")
print(poem)
print("-----------------------")


five = 10 - 2 + 3 - 6
print("This should be five: %s" % (five))


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    cartes = jars / 100
    return jelly_beans, jars, cartes


start_point = 10000
# 函数return多个值，可以赋值给多个变量。变量的数量必须和return的数量一致
beans, jars, crates = secret_formula(start_point)

# remember that is another way to format a cooked_string
print("With a starting point of: {}".format(start_point))
print("We'd have %s beans, %s jars, and %s crates." % (beans, jars, crates))

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# format方法可以直接引用函数return的值
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
