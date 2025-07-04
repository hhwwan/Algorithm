"""
크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오등큰수 NGF(i)를 구하려고 한다.

Ai가 수열 A에서 등장한 횟수를 F(Ai)라고 했을 때, 
Ai의 오등큰수는 오른쪽에 있으면서 수열 A에서 등장한 횟수가 F(Ai)보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 
그러한 수가 없는 경우에 오등큰수는 -1이다.

예를 들어, A = [1, 1, 2, 3, 4, 2, 1]인 경우 F(1) = 3, F(2) = 2, F(3) = 1, F(4) = 1이다. 
A1의 오른쪽에 있으면서 등장한 횟수가 3보다 큰 수는 없기 때문에, NGF(1) = -1이다. 
A3의 경우에는 A7이 오른쪽에 있으면서 F(A3=2) < F(A7=1) 이기 때문에, NGF(3) = 1이다. 
NGF(4) = 2, NGF(5) = 2, NGF(6) = 1 이다.
"""

# 카운터 사용 잘 해보기
import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
result = [-1] * N
count = Counter(A)
stack = []

for i in range(N):
    while stack and count[A[stack[-1]]] < count[A[i]]:
        idx = stack.pop()
        result[idx] = A[i]
    stack.append(i)

print(' '.join(map(str, result)))