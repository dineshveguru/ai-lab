# import copy
# from heapq import heappush, heappop

# n = 3

# row = [1, 0, -1, 0]
# col = [0, -1, 0, 1]


# class priorityQueue:
#     def __init__(self) -> None:
#         self.heap = []

#     def push(self, k):
#         heappush(self.heap, k)

#     def pop(self):
#         return heappop(self.heap)

#     def empty(self):
#         if not self.heap:
#             return True
#         return False


# class node:

#     def __init__(self, parent, mat, empty_tile_pos, cost, level) -> None:
#         self.parent = parent
#         self.mat = mat
#         self.empty_tile_pos = empty_tile_pos
#         self.cost = cost
#         self.level = level

#     def __lt__(self, nxt):
#         return self.cost < nxt.cost

#     def calculateCost(mat, final):
#         count = 0
#         for i in range(n):
#             for j in range(n):
#                 if mat[i][j] and (mat[i][j] != final[i][j]):
#                     count += 1
#         return count

#     def newNode(mat, empty_tile_pos, new_empty_tile_pos, level, parent, final):
#         new_mat = copy.deepcopy(mat)
#         x1 = empty_tile_pos[0]
#         y1 = empty_tile_pos[0]
#         x2 = new_empty_tile_pos[0]
#         y2 = new_empty_tile_pos[0]
#         new_mat[x1][y1], new_mat
