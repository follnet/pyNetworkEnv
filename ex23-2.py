def main(languages):
    line = languages.readline()

    if line:
        printLine(line)
        return main(languages)


def printLine(line):
    lang = line.strip()
    # python3默认的string类型为unicode。
    # 编码格式默认为utf-8,对于英文兼容ascii。
    # 所以 "cisco".encode()结果为b'cisco'。
    # unicode.encode()为utf-8, utf-8.decode()为unicode
    # bytes是一种比特流，它的存在形式是01010001110这种。我们无论是在写代码，还是阅读文章的过程中，
    # 肯定不会有人直接阅读这种比特流，它必须有一个编码方式，使得它变成有意义的比特流，而不是一堆晦涩难懂的01组合。
    raw = lang.encode()
    cook = raw.decode()
    print(raw, '<===>', cook)


file = open("lang_test.txt")
main(file)
