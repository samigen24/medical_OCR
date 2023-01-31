#
#
# with open("like.txt", "a") as f:
#     f.write("Prove it to me")
#
#
# with open("like.txt", "r") as f:
#     for line in f:
#         print(line)
#

player_scores = {}
with open("scores.csv", "r") as f:
    for line in f:
        player, score = line.split(',')
        score = int(score)
        # let's create a dictionary for this data
        if player in player_scores:
            player_scores[player].append(score)
            # this will ensure to add more score for the player
        else:
            player_scores[player] = [score]

for player, score_list in player_scores.items():
    print(player, score_list)
    min_score = min(score_list)
    max_score = max(score_list)
    Avg_score = sum(score_list)/len(score_list)
    print(f'{player} ==> Min: {min_score}, Max: {max_score}, Avg: {Avg_score}')
    print(" ")
