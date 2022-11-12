import math


def minmax(cd, td, node, maxt, scr):
    if cd == td:
        return scr[node]
    if maxt:
        return max(minmax(cd + 1, td, node * 2, False, scr), minmax(cd + 1, td, node * 2 + 1, False, scr))
    else:
        return min(minmax(cd + 1, td, node * 2, True, scr), minmax(cd + 1, td, node * 2 + 1, True, scr))


scr = [50, 73, 45, 60, 47]
td = math.log(len(scr), 2)
cd = 0
nodev = 0
maxt = True
ans = minmax(cd, td, nodev, maxt, scr)
print(ans)
