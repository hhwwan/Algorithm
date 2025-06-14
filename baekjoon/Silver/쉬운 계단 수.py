"""
45656이란 수를 보자.

이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.

N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구해보자. 
0으로 시작하는 수는 계단수가 아니다.
"""

N = int(input())

# dp[x][y] -> x자리 y로 끝나는 수
dp = [[0] * 10 for _ in range(N+1)]
dp[1][1] = 1
dp[1][2] = 1
dp[1][3] = 1
dp[1][4] = 1
dp[1][5] = 1
dp[1][6] = 1
dp[1][7] = 1
dp[1][8] = 1
dp[1][9] = 1

for i in range(2, N + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1] % 1000000000
        elif j == 9:
            dp[i][j] = dp[i-1][j-1] % 1000000000
        else:
            dp[i][j] = (dp[i-1][j+1] + dp[i-1][j-1]) % 1000000000

answer = 0
for i in range(10):
    answer = (answer + dp[N][i]) % 1000000000

print(answer)