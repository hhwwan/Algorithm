"""
크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다. 
Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 
그러한 수가 없는 경우에 오큰수는 -1이다.

예를 들어, A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다. 
A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.
"""

# 내가 푼 풀이 -> 시간초과
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
result = []

for i in range(N):
    temp = False
    for j in range(i,N):
        if A[i] < A[j]:
            result.append(A[j])
            temp = True
            break
    if not temp:
        result.append(-1)

print(' '.join(map(str, result)))

# 수정본
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
result = [-1] * N  # 초기에는 모두 -1로 채워놓기
stack = []

for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        idx = stack.pop()
        result[idx] = A[i]
    stack.append(i)
print(' '.join(map(str, result)))