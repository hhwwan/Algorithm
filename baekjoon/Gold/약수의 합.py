"""
두 자연수 A와 B가 있을 때, A = BC를 만족하는 자연수 C를 A의 약수라고 한다. 
예를 들어, 2의 약수는 1, 2가 있고, 24의 약수는 1, 2, 3, 4, 6, 8, 12, 24가 있다. 
자연수 A의 약수의 합은 A의 모든 약수를 더한 값이고, f(A)로 표현한다. 
x보다 작거나 같은 모든 자연수 y의 f(y)값을 더한 값은 g(x)로 표현한다.

자연수 N이 주어졌을 때, g(N)을 구해보자.
"""
import sys
input = sys.stdin.readline

MAX = 1000000

# f(y) 계산: 약수 합
f = [0] * (MAX + 1)
for i in range(1, MAX + 1):
    for num in range(i, MAX + 1, i):
        f[num] += i

# g(N): 누적 합
g = [0] * (MAX + 1)
for j in range(1, MAX + 1):
    g[j] = g[j-1] + f[j]

T = int(input())

for _ in range(T):
    N = int(input())
    print(g[N])