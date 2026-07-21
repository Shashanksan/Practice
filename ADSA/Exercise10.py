INF = 9999

try:
    n = int(input())
    graph = []

    for _ in range(n):
        row = list(map(int, input().split()))
        if len(row) != n:
            print("Invalid row size.")
        graph.append(row)

    src = int(input())

    if src < 0 or src >= n:
        print("Invalid source vertex.")
    else:
        dist = [INF] * n
        visited = [False] * n
        dist[src] = 0

        for _ in range(n):
            u = -1
            min_dist = INF

            for i in range(n):
                if not visited[i] and dist[i] < min_dist:
                    min_dist = dist[i]
                    u = i

            if u == -1:
                break

            visited[u] = True

            for v in range(n):
                if (
                    graph[u][v] > 0
                    and not visited[v]
                    and dist[u] + graph[u][v] < dist[v]
                ):
                    dist[v] = dist[u] + graph[u][v]

        for i in range(n):
            print(f"Distance from Source to Vertex {i}: {dist[i]}")

except Exception as e:
    print(f"Error: {e}")