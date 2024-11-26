w = int(input())
dp = []
dp.append([1, 0])
dp.append([0, 1])
dp.append([1, 1])
for i in range(2, w):
    dp.append([dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1]])
print(dp[w][0], dp[w][1])