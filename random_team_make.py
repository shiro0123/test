import random

TEAM_NUM = 3
STUDENTS = []


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
