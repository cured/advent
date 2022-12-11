import requests
fileurl = "https://pastebin.mozilla.org/UEY5rSuL/raw"


def parse_file():
    content = requests.get(fileurl)
    return content.text


def main():
    each_four_symbols = []
    i = 1
    found = 0
    for i, symbol in enumerate(parse_file()):
        if len(each_four_symbols) < 4:
            if symbol not in each_four_symbols:
                each_four_symbols.append(symbol)
            else:
                former = "".join(each_four_symbols)
                each_four_symbols = []
                start_fill = False
                for s in former:
                    if start_fill:
                        each_four_symbols.append(s)
                    if s == symbol:
                        start_fill = True
                each_four_symbols.append(symbol)
            if len(each_four_symbols) == 4:
                found = i+1
                break

    print(found)


if __name__ == "__main__":
    main()
