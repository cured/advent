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
        if first_start >= second_start and first_finish <= second_finish:
            print('1', first_start, '-', first_finish, ' ', second_start, '-', second_finish)
            counter += 1
            continue
        elif second_start >= first_start and second_finish <= first_finish:
            counter += 1
            print('2', first_start, '-', first_finish, ' ', second_start, '-', second_finish)

    print(counter)


if __name__ == "__main__":
    main()
