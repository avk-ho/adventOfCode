# https://adventofcode.com/2022/day/2

import random

# win 6pt, draw 3pt, loss 0pt
# playing rock 1pt, paper 2pt, scissors 3pt

def calculate_rps_score(guide):
    rps = {
        "X": {  # rock
            "A": "draw", # rock
            "B": "lose", # paper
            "C": "win", # scissors
            "score": 1
        }, 
        "Y": {  # paper
            "A": "win",
            "B": "draw",
            "C": "lose",
            "score": 2
        }, 
        "Z": {  # scissors
            "A": "lose",
            "B": "win",
            "C": "draw",
            "score": 3
        }, 
    }
    results_score = {
        "win": 6,
        "draw": 3,
        "lose": 0
    }

    total_score = 0
    for round in guide:
        opponent_choice = round[0]
        player_choice = round[1]
        score = rps[player_choice]["score"] + results_score[rps[player_choice][opponent_choice]]
        total_score += score
        # print(score)

    return total_score

# guide = [["A", "Y"], ["B", "X"], ["C", "Z"]]
# print(calculate_rps_score(guide))

opponent_choices = ["A", "B", "C"]
player_choices = ["X", "Y", "Z"]

guide = []
for i in range(5):
    opp_pick = random.choice(opponent_choices)
    play_pick = random.choice(player_choices)
    guide.append([opp_pick, play_pick])

print(guide)
print(calculate_rps_score(guide))