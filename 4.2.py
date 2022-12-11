import requests
fileurl = "https://pastebin.com/raw/dFv5tTMw"


def parse_file():
    content = requests.get(fileurl)
    return content.text.splitlines()


def main():
    lines = parse_file()
    counter = 0
    for l in lines:
        first_int, second_int = l.split(',')
        first_start, first_finish = first_int.split('-')
        second_start, second_finish = second_int.split('-')
        first_start, first_finish, second_start, second_finish = map(int, [first_start, first_finish, second_start, second_finish])
        first = set(range(first_start, first_finish + 1))
        second = set(range(second_start, second_finish + 1))
        if first.intersection(second):
            counter += 1

    print(counter)


if __name__ == "__main__":
    main()
