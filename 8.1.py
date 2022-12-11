import requests
fileurl = "https://pastebin.com/raw/3AY6CRV1"


def parse_file():
    content = requests.get(fileurl)
    return content.text.splitlines()


def main():
    file_lines = parse_file()
    lines = []
    for i, line in enumerate(file_lines):
        lines.append([])
        for j, l in enumerate(line):
            lines[i].append(int(l))
    width = len(lines[0])
    height = len(lines)
    result_matrix = [[0 for j in range(height)] for i in range(width)]
    i = 0
    while i < width:
        j = 0
        while j < height:
            curr = int(lines[i][j])
            if i == 0 or j == 0 or i == width - 1 or j == height - 1:
                result_matrix[i][j] = 1
            if result_matrix[i][j] == 0:
                # check_width_visibility
                if max(lines[i][:j]) < curr or max(lines[i][j+1:]) < curr:
                    result_matrix[i][j] = 1 
                # check_height_visibility
                if result_matrix[i][j] == 0:
                    column = [lines[k][j] for k in range(width)]
                    if max(column[:i]) < curr or max(column[i+1:]) < curr:
                        result_matrix[i][j] = 1 
            j += 1
        i += 1

    counter = 0
    for i in range(width):
        for j in range(height):
            if result_matrix[i][j] == 1:
                counter += 1

    print(counter)


if __name__ == "__main__":
    main()
