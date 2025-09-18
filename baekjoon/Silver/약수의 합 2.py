"""
두 자연수 A와 B가 있을 때, A = BC를 만족하는 자연수 C를 A의 약수라고 한다. 
예를 들어, 2의 약수는 1, 2가 있고, 24의 약수는 1, 2, 3, 4, 6, 8, 12, 24가 있다. 
자연수 A의 약수의 합은 A의 모든 약수를 더한 값이고, f(A)로 표현한다. 
x보다 작거나 같은 모든 자연수 y의 f(y)값을 더한 값은 g(x)로 표현한다.

자연수 N이 주어졌을 때, g(N)을 구해보자.
"""

# 시간초과
N= int(input())
answer = 0

for num in range(1, N+1): # 1부터 N까지 모든 자연수
    for x in range(1, num+1): # 각 자연수들의 약수 구하기
        if num % x == 0:
            answer += x # 약수라면 더하기

print(answer)

# 다른 풀이
N= int(input())
answer = 0

for num in range(1, N+1): # 1부터 N까지 모든 자연수
    answer += num * (N // num) # num * num으로 나눠지는 수의 개수

print(answer)