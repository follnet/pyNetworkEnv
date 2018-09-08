def main(languages):
    line = languages.readline()

    if line:
        printLine(line)
        return main(languages)


def printLine(line):
    lang = line.strip()
    raw = bytes(lang, 'ascii')
    cook = str(raw, 'ascii')
    print(raw, '<===>', cook)


file = open("lang_test.txt")
main(file)
