import math
n = int(input("enter no of nodes: "))
scores = []
for i in range(n):
    scores.append(int(input("enter node value: ")))


def minmax(cur_depth, node_index, max_turn, scores, target_depth):
    if cur_depth == target_depth:
        return scores[node_index]
    if max_turn:
        return max(minmax(cur_depth + 1, node_index * 2, False, scores, target_depth), minmax(cur_depth + 1, node_index * 2 + 1, False, scores, target_depth))
    else:
        return min(minmax(cur_depth + 1, node_index * 2, True, scores, target_depth), minmax(cur_depth + 1, node_index * 2 + 1, True, scores, target_depth))


tree_depth = math.log(len(scores), 2)
print(minmax(0, 0, True, scores, tree_depth))
