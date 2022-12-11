import requests
fileurl = "https://pastebin.com/raw/3AY6CRV1"


def parse_file():
    content = requests.get(fileurl)
    return content.text.splitlines()


def coeff_count(el_direction, coeff_direction, curr) -> (int, bool):
    if el_direction < curr:
        return coeff_direction + 1, False
    else:
        return coeff_direction + 1, True


def main():
    file_lines = parse_file()
    lines = []
    for i, line in enumerate(file_lines):
        lines.append([])
        for j, l in enumerate(line):
            lines[i].append(int(l))
    width = len(lines[0])
    height = len(lines)
    i = 0
    max_coeff = 0
    while i < width:
        j = 0
        while j < height:
            curr = int(lines[i][j])
            # get coefficient
            # check to the left
            left_coeff = 0
            for left in lines[i][:j][::-1]:
                left_coeff, to_break = coeff_count(left, left_coeff, curr)
                if to_break:
                    break
            # check to the right
            right_coeff = 0
            for right in lines[i][j+1:]:
                right_coeff, to_break = coeff_count(right, right_coeff, curr)
                if to_break:
                    break
            column = [lines[k][j] for k in range(width)]
            # check to the up
            top_coeff = 0
            for top in column[:i][::-1]:
                top_coeff, to_break = coeff_count(top, top_coeff, curr)
                if to_break:
                    break
            # check to the bottom
            bottom_coeff = 0
            for bottom in column[i+1:]:
                bottom_coeff, to_break = coeff_count(bottom, bottom_coeff, curr)
                if to_break:
                    break
            coeff = left_coeff * right_coeff * top_coeff * bottom_coeff
            if max_coeff < coeff:
                max_coeff = coeff
            j += 1
        i += 1

    print(max_coeff)


if __name__ == "__main__":
    main()
