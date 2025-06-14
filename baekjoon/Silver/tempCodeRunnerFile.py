dp[1][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 1
dp[3][3] = 1

# 점화식
for n in range(4, 100001):
    dp[n][1] = (dp[n-1][2] + dp[n-1][3])
    dp[n][2] = (dp[n-2][1] + dp[n-2][3])
    dp[n][3] = (dp[n-3][1] + dp[n-3][2])

for _ in range(T):
    n = int(input())
    answer = (dp[n][1] + dp[n][2] + dp[n][3]) % 1000000009

    print(answer)