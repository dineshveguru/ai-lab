maze = [['Beg', 'Bre', 'Pit', 'Bre'],
        ['Ste', 'Ok ', 'Bre', 'Ok '],
        ['Wum', 'GSB', 'Pit', 'Bre'],
        ['Ste', 'Ok ', 'Bre', 'Ok']]
i = j = 0
flag = True
for k in maze:
    for l in k:
        print(f"{l} ", end="")
    print("")

while flag == True:
    move = input("enter your move: ")
    if move.lower() == "u":
        i -= 1
        if i < 0:
            print("you cant make that move")
            i += 1
    elif move.lower() == "d":
        i += 1
        if i > 3:
            print("you cant make that move")
            i -= 1
    elif move.lower() == "r":
        j += 1
        if j > 3:
            print("you cant make that move")
            j -= 1
    elif move.lower() == "l":
        j -= 1
        if j < 0:
            print("you cant make that move")
            j += 1
    flag = True
    if str(maze[i][j]) == "Pit":
        print("game over")
        flag = False
        break
    elif str(maze[i][j]) == "Wum":
        print("game over")
        flag = False
        break
    elif str(maze[i][j]) == "GSB":
        print("you won")
        flag = False
        break
    for k in maze:
        for l in k:
            print(l, end=" ")
        print("")
    print(f"you are at {str(maze[i][j])} ")
