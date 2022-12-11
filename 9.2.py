import requests
from dataclasses import dataclass
from typing import List, Tuple, Optional, Set
from enum import Enum
fileurl = "https://pastebin.com/raw/963KBHDB"


DONT_MOVE_THE_TAIL = (None, None)


def parse_file():
    content = requests.get(fileurl)
    return content.text.splitlines()


class DirectionEnum(Enum):
    U = "U"
    D = "D"
    L = "L"
    R = "R"


@dataclass
class Dot:
    x: int
    y: int


@dataclass
class Head(Dot):
    tail: "Head"
    path: Set[Tuple[int, int]]
    number: int

    def move(self, direction):
        match (DirectionEnum(direction)):
            case DirectionEnum.U:
                self.y += 1
            case DirectionEnum.D:
                self.y -= 1
            case DirectionEnum.R:
                self.x += 1
            case DirectionEnum.L:
                self.x -= 1
        
        dir_x, dir_y = self.where_is_tail()
        if (dir_x, dir_y) != DONT_MOVE_THE_TAIL:
            self.tail.move_as_tail(dir_x, dir_y)

    def where_is_tail(self) -> Tuple[DirectionEnum, DirectionEnum]:
        diff_x = self.x - self.tail.x
        diff_y = self.y - self.tail.y

        direction_hor = None
        if diff_x >= 1:
            direction_hor = DirectionEnum.R
        elif diff_x <= -1:
            direction_hor = DirectionEnum.L

        direction_ver = None
        if diff_y >= 1:
            direction_ver = DirectionEnum.U
        elif diff_y <= -1:
            direction_ver = DirectionEnum.D

        if abs(diff_x) > 1 or abs(diff_y) > 1:
            return direction_hor, direction_ver
        
        return None, None

    def move_as_tail(self, direction_x, direction_y):
        if direction_x == DirectionEnum.R:
            self.x += 1
        if direction_x == DirectionEnum.L:
            self.x -= 1
        if direction_y == DirectionEnum.U:
            self.y += 1
        if direction_y == DirectionEnum.D:
            self.y -= 1
        if self.is_last:
            self.path.add((self.x, self.y))
        else:
            dir_x, dir_y = self.where_is_tail()
            if (dir_x, dir_y) != DONT_MOVE_THE_TAIL:
                self.tail.move_as_tail(dir_x, dir_y)

    @property
    def is_last(self):
        return not self.tail


def main():
    lines = parse_file()
    
    head = Head(0, 0, None, set((0, 0)), 0)
    i = 0
    curr = head
    while i <= 8:
        tail = Head(0, 0, None, set((0, 0)), i + 1)
        curr.tail = tail
        curr = tail
        i += 1
        
    for l in lines:
        direction, number = l.split()
        for i in range(int(number)):
            head.move(direction)

    while head.tail:
        head = head.tail
    print(len(head.path))


if __name__ == "__main__":
    main()
