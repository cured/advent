import requests
from textwrap import wrap
fileurl = "https://pastebin.com/raw/PrKCuwDE"


def parse_file():
    content = requests.get(fileurl)
    return content.text.splitlines()


def in_sprite(crt, sprite_position):
    return sprite_position - 1 <= crt <= sprite_position + 1


def to_draw(crt, sprite_position):
    return "#" if in_sprite(crt, sprite_position) else "."


def main():
    cycle = 0
    lines = parse_file()
    in_addx = False
    result_string = ["."]*240
    sprite_position = 1
    while lines or in_addx:
        crt = cycle % 40
        row = cycle // 40
        cycle += 1
        result_string[row * 40 + crt] = to_draw(crt, sprite_position)
        if in_addx:
            sprite_position += number
            in_addx = False
            continue
        line = lines.pop(0)
        command, *number = line.split()
        if command == "noop":
            continue
        if command == "addx":
            in_addx = True
            number = int(number.pop())

    for_printing = wrap("".join(result_string), 40)
    for i in for_printing:
        print(i)


if __name__ == "__main__":
    main()
