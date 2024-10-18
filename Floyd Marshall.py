def floyd_warshall(matrix):
    n = len(matrix)
    dist = [[matrix[i][j] for j in range(n)] for i in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

matrix = [
    [0, 12, 3, float('inf'), 7, 10],
    [12, 0, 6, 6, 18, 8],
    [3, 6, 0, 4, 12, float('inf')],
    [float('inf'), 6, 4, 0, 9, float('inf')],
    [7, 18, 12, 9, 0, 12],
    [10, 8, float('inf'), float('inf'), 12, 0]
]

distances = floyd_warshall(matrix)
for row in distances:
    print(row)