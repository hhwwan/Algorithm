"""
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

둘째 줄에는 가장 긴 증가하는 부분 수열을 출력한다. 
그러한 수열이 여러가지인 경우 아무거나 출력한다.
"""

# 제대로 풀지 못했음 + 코드가 이해가 잘 안되니 추후 다시 꼭 풀어봐야함
N = int(input())
arr = list(map(int,input().split()))

dp = [1] * N # 길이
prev = [-1] * N 

for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j]+1
            prev[i] = j # 기록해두기

max_len = max(dp)
idx = dp.index(max_len)

lis = []
while idx != -1:
    lis.append(arr[idx])
    idx = prev[idx]

lis.reverse()

print(max_len)
print(' '.join(map(str,lis)))