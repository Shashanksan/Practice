from collections import deque

def bfs(graph, start):
    visited = [False] * len(graph)
    q = deque([start])
    visited[start] = True
    result = []

    while q:
        node = q.popleft()
        result.append(str(node))
        for i in range(len(graph)):
            if graph[node][i] == 1 and not visited[i]:
                visited[i] = True
                q.append(i)
    print(" ".join(result))


def dfs(graph, start, visited, result):
    visited[start] = True
    result.append(str(start))
    for i in range(len(graph)):
        if graph[start][i] == 1 and not visited[i]:
            dfs(graph, i, visited, result)


try:
    n = int(input())
    graph = []

    for _ in range(n):
        row = list(map(int, input().split()))
        if len(row) != n:
            print("Invalid row size.")
            exit()
        graph.append(row)

    while True:
        try:
            command = input().split()

            if not command:
                print("Invalid input.")
                continue

            choice = int(command[0])

            if choice == 3:
                break

            elif choice == 1:
                if len(command) != 2:
                    print("Invalid input.")
                    continue
                start = int(command[1])
                if start < 0 or start >= n:
                    print("Invalid source vertex.")
                    continue
                bfs(graph, start)

            elif choice == 2:
                if len(command) != 2:
                    print("Invalid input.")
                    continue
                start = int(command[1])
                if start < 0 or start >= n:
                    print("Invalid source vertex.")
                    continue
                visited = [False] * n
                result = []
                dfs(graph, start, visited, result)
                print(" ".join(result))

            else:
                print("Invalid choice.")

        except:
            print("Invalid input.")

except:
    pass