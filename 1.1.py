from typing import List

import requests


fileurl = "https://pastebin.com/raw/vUpahANh"

def parse_file():
    content = requests.get(fileurl)
    return content.text.splitlines()

def main():
    weights = parse_file()
    current_elf_weight = 0
    max_weight = 0
    for weight in weights:
        if weight:
            current_elf_weight += int(weight)
        else:
            if max_weight < current_elf_weight:
                max_weight = current_elf_weight
            
            current_elf_weight = 0

    print(max(current_elf_weight, max_weight))


if __name__ == "__main__":
    main()
