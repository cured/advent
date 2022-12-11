import requests
fileurl = "https://pastebin.com/raw/PrKCuwDE"


def parse_file():
    content = requests.get(fileurl)
    return content.text.splitlines()


def main():
    cycle = 0
    counter = 1
    lines = parse_file()
    in_addx = False
    number = 0
    cycle_counters = []
    while lines or in_addx:
        cycle += 1
        if (cycle % 40 == 20 and cycle <= 220):
            cycle_counters.append(cycle * counter)
        if in_addx:
            counter += number
            in_addx = False
            continue
        line = lines.pop(0)
        command, *number = line.split()
        if command == "noop":
            continue
        if command == "addx":
            in_addx = True
            number = int(number.pop())

    print(cycle_counters)
    print(sum(cycle_counters))


if __name__ == "__main__":
    main()
