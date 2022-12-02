import requests
fileurl = "https://pastebin.com/raw/y0rrJUzH"


win_pairs = (
    ("A", "Y"),
    ("B", "Z"),
    ("C", "X")
)

choice_score = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

LOSE = 0
DRAW = 3
WIN = 6


def parse_file():
    content = requests.get(fileurl)
    return content.text.splitlines()


def result_score(opp, you):
    if (ord(you) - ord(opp)) == 23:
        return DRAW + choice_score[you]
    
    if (opp, you) in win_pairs:
        return WIN + choice_score[you]

    return choice_score[you]


def main():
    lines = parse_file()
    score = 0
    for l in lines:
        opp, you = l.split(' ')
        score += result_score(opp, you)

    print(score)



if __name__ == "__main__":
    main()
