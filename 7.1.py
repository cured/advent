import requests
from dataclasses import dataclass
from typing import List, Optional, Iterable
fileurl = "https://pastebin.com/raw/WdG5KDgm"


@dataclass
class Node:
    name: str
    is_dir: bool
    size: int
    children: List["Node"] = None
    parent: "Node" = None
    level: Optional[int] = 0

    def add(self, child: "Node"):
        child.level = self.level + 1
        self.children.append(child)
        return self

    def p(self):
        print(" "*self.level, "- ",self.name, self.is_dir, self.size)
        for ch in self.children:
            ch.p()

    def answer(self, counter = 0):
        if self.is_dir and self.size <= 100000:
            counter += self.size
        for ch in self.children:
            counter = ch.answer(counter)
        return counter

    def set_size(self):
        for ch in self.children:
            if ch.is_dir:
                self.size += ch.set_size()
            else:
                self.size += ch.size
        return self.size


def handle_cd(dir, node: Node = None):
    if dir == "..":
        return node.parent
    else:
        return next(filter(lambda x: x.name == dir, node.children))


def handle_ls(parent_node: Node, folder_content: Iterable):
    pass


def parse_file():
    content = requests.get(fileurl)
    return content.text.splitlines()


def main():
    lines = parse_file()

    active_node = Node(
        name="/",
        is_dir=True,
        size=0,
        children=[]
    )
    current_node = active_node
    i = 1
    while i < len(lines):
        l = lines[i]
        cmd_line = l.split()
        if cmd_line and cmd_line[0] == "$":
            match cmd_line[1]:
                case "cd":
                    current_node = handle_cd(cmd_line[2], current_node)
                case "ls":
                    cmd_line = lines[i + 1].split()
                    while cmd_line and (cmd_line[0] != "$"):
                        current_node.add(
                            Node(
                                name=cmd_line[1],
                                level=current_node.level + 1,
                                is_dir=(True if cmd_line[0] == "dir" else False),
                                size=(int(cmd_line[0]) if cmd_line[0] != "dir" else 0),
                                children=[],
                                parent=current_node
                            )
                        )
                        i += 1
                        try:
                            cmd_line = lines[i + 1].split()
                        except Exception as e:
                            print(e)
                            break
                    continue

        i += 1


    active_node.set_size()
    active_node.p()

    print(active_node.answer())



if __name__ == "__main__":
    main()
