import requests


fileurl = "https://pastebin.com/raw/vUpahANh"

def parse_file():
    content = requests.get(fileurl)
    return content.text.splitlines()

def is_max(three, current):
    if three[0] >= current:
        return False
    return True

def append_to_max(three, current):
    if current < three[1]:
        return (current, *three[1:])
    if three[1] < current < three[2]:
        return (three[1], current, three[2])
    return (*three[1:], current)

def main():
    weights = parse_file()
    three_max_weights = (0, 0, 0)
    current_elf_weight = 0
    for weight in weights:
        if weight:
            current_elf_weight += int(weight)
        else:
            if is_max(three_max_weights, current_elf_weight):
                three_max_weights = append_to_max(three_max_weights, current_elf_weight)
                print(three_max_weights)

            current_elf_weight = 0
    
    if is_max(three_max_weights, current_elf_weight):
        append_to_max(three_max_weights, current_elf_weight)

    print(sum(three_max_weights))


if __name__ == "__main__":
    main()
