import requests
fileurl = "https://pastebin.com/raw/y0rrJUzH"


win_pairs = {
    "A": "B",
    "B": "C",
    "C": "A"
}

lose_pairs = {
    "A": "C",
    "C": "B",
    "B": "A"
}

choice_score = {
    "X": 0,
    "Y": 3,
    "Z": 6
}


def parse_file():
    content = requests.get(fileurl)
    return content.text.splitlines()


def result_score(opp, you):
    # draw
    if you == "Y":
        # ord("A") == 65
        return choice_score[you] + ord(opp) - 65 + 1
    
    # lose
    if you == "X":
        return choice_score[you] + ord(lose_pairs[opp]) - 65 + 1
    
    # win
    if you == "Z":
        return choice_score[you] + ord(win_pairs[opp]) - 65 + 1


def main():
    lines = parse_file()
    score = 0
    for l in lines:
        opp, you = l.split(' ')
        score += result_score(opp, you)

    print(score)



if __name__ == "__main__":
    main()
