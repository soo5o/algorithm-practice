n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
dp = [[1] * n for _ in range(n)]
cells = []
ans = 0
for i in range(n):
    for j in range(n):
        cells.append((lst[i][j], i, j))
cells.sort()
for v, x, y in cells:
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for dx, dy in move:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and v < lst[nx][ny]:
            dp[nx][ny] = max(dp[nx][ny], dp[x][y] + 1)
for i in range(n):
    for j in range(n):
        ans = max(ans, dp[i][j])
print(ans)
