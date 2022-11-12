graph = {}

choice = 0
while choice != 1:
    node = input("enter node: ")
    adjacent_elements = input("enter it's adjacent elements: ").split(" ")
    graph[node] = adjacent_elements
    print("enter 0 to enter new node and 1 to exit")
    choice = int(input("enter choice: "))


def dfs(graph, start):
    visited = set()
    if start not in visited:
        visited.add(start)
        print(start)
        for i in graph[start]:
            dfs(graph, i)


def bfs(graph, start):
    visited = set()
    queue = []
    if start not in visited:
        visited.add(start)
    for i in graph[start]:
        queue.append(i)
    bfs(graph, queue.pop(0))


bfs(graph, list(graph.keys())[0])
