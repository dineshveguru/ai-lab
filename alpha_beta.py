import math
max_val, min_val = 1000, -1000


def minmax(depth, node_index, max_turn, scores, alpha, beta, target_depth):
    if depth == target_depth:
        return scores[node_index]

    if max_turn:
        best = min_val
        for i in range(2):
            val = minmax(depth + 1, node_index * 2 + i, False,
                         scores, alpha, beta, target_depth)
            best = max(val, best)
            alpha = max(alpha, best)
            if alpha >= beta:
                break
        return best

    else:
        best = max_val
        for i in range(2):
            val = minmax(depth + 1, node_index * 2 + i, True,
                         scores, alpha, beta, target_depth)
            best = min(best, val)
            beta = min(best, beta)
            if alpha >= beta:
                break
        return best


scores = []
for i in range(int(input("enter no of nodes: "))):
    scores.append(int(input("enter node value: ")))
tree_depth = math.log(len(scores), 2)
print(minmax(0, 0, True, scores, min_val, max_val, tree_depth))
