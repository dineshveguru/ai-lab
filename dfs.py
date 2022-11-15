graph = {}
bfs_visited = []
dfs_visited = []
queue = []

choice = 0
while choice != 1:
    node = input("enter node: ")
    adjacent_elements = input("enter it's adjacent elements: ").split(" ")
    graph[node] = adjacent_elements
    print("enter 0 to enter new node and 1 to exit")
    choice = int(input("enter choice: "))

print("DFS>")


def dfs(graph, node):
    if node not in dfs_visited:
        print(node, end=" ")
        dfs_visited.append(node)
        if node in graph.keys():
            for neighbour in graph[node]:
                dfs(graph, neighbour)


def bfs(graph, start):
    print("BFS>")
    bfs_visited.append(start)
    queue.append(start)
    while queue:
        m = queue.pop(0)
        print(m, end=" ")
        if m in graph.keys():
            for neighbour in graph[m]:
                if neighbour not in bfs_visited:
                    bfs_visited.append(neighbour)
                    queue.append(neighbour)


dfs(graph, list(graph.keys())[0])
bfs(graph, list(graph.keys())[0])
