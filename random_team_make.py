import random

TEAM_NUM = 3
STUDENTS = [
    "本川 倖多",
    "馬瀬 淳平",
    "秋葉 康太",
    "清水星磨",
    "平野 圭悟",
    "小野 功太",
    "太田 一颯",
    "森誠太朗",
    "森角望",
    "神山 貴志",
    "伊藤 翼",
    "平地 伸吾",
    "関口 匠弥",
    "菅野 那菜",
]


def random_team_make():
    random.shuffle(STUDENTS)
    teams = []
    for i in range(TEAM_NUM):
        teams.append(STUDENTS[i::TEAM_NUM])
    for i, team in enumerate(teams):
        print(f"[チーム{i+1}]")
        print("\n".join(team))
        print()


random_team_make()
