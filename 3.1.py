import requests
fileurl = "https://pastebin.com/raw/r7XDY9sk"


ord_diff_upper = 38
ord_diff_lower = 96


def parse_file():
    content = requests.get(fileurl)
    return content.text.splitlines()


def main():
    lines = parse_file()
    score = 0
    for l in lines:
        first, second = set(l[:len(l)//2]), set(l[len(l)//2:])
        symbol = list(first.intersection(second))[0]
        if symbol.lower() == symbol:
            # lowercase
            difff = ord_diff_lower
        else:
            # uppercase
            difff = ord_diff_upper
        score += ord(symbol) - difff

    print(score)


if __name__ == "__main__":
    main()
