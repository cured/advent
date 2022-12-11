import requests
import re

from collections import defaultdict
fileurl = "https://pastebin.com/raw/61UT0r4y"


def parse_file():
    content = requests.get(fileurl)
    return content.text.splitlines()


# possible operations
def move(quantity, from_stack, to_stack):
    print(quantity, from_stack, to_stack)
    from_stack = ''.join(from_stack)
    els_to_move = from_stack[:quantity][::-1]
    to_stack = els_to_move + "".join(to_stack)

    from_stack = from_stack[quantity:]
    a, b = list(from_stack), list(to_stack)
    print(a, b)
    return a, b


def main():
    stacks = defaultdict(list)
    crates = []
    lines = parse_file()
    # parse stacks, organize in a list of lists
    for l in lines[:8]:
        crates.append(re.findall('.(.)..?', l))
    
    for el in crates:
        for i, e in enumerate(el):
            if e.strip():
                stacks[i+1].append(e)
    
    for stack in stacks.items():
        print(stack)

    for operation in lines[10:]:
        quantity, from_, to = map(int, re.findall("move (\d+) from (\d) to (\d)", operation)[0])
        stacks[from_], stacks[to] = move(quantity, stacks[from_], stacks[to])
    
    final_str = ""
    for i in sorted(stacks.keys()):
        print(i, stacks[i])
        final_str = final_str + stacks[i][0]
        
    print(final_str)


if __name__ == "__main__":
    main()
