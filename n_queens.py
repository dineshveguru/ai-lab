n = int(input())
col = set()
pos_diag = set()
neg_diag = set()
board = [["." for i in range(n)] for i in range(n)]


def backtrack(r):
    if r == n:
        for i in range(len(board)):
            for j in range(len(board[i])):
                print(board[i][j], end=" ")
            print(" ")
        print("--------------------------------")
        return
    for c in range(n):
        if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
            continue
        col.add(c)
        pos_diag.add(r + c)
        neg_diag.add(r - c)
        board[r][c] = "Q"
        backtrack(r + 1)
        col.remove(c)
        pos_diag.remove(r + c)
        neg_diag.remove(r - c)
        board[r][c] = "."


backtrack(0)
