"""
두 자연수 A와 B에 대해서, A의 배수이면서 B의 배수인 자연수를 A와 B의 공배수라고 한다. 
이런 공배수 중에서 가장 작은 수를 최소공배수라고 한다. 
예를 들어, 6과 15의 공배수는 30, 60, 90등이 있으며, 최소 공배수는 30이다.

두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성하시오.
"""

T = int(input())
# 내가 푼 것 -> 최소공약수 이용해서 (풀리긴하나 시간이 많이 걸림)
for _ in range(T):
    A, B = map(int,input().split())
    for i in range(min(A,B),0,-1):
        if A % i == 0 and B % i == 0:
            gcd = i
            break
    lcm = (A*B) // gcd
    print(lcm)

# 더 좋은 답
for _ in range(T):
    A, B = map(int,input().split())
    tmp = A * B

    while B > 0:
        A, B = B, A % B
    
    print(tmp // A)