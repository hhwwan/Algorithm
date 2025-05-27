"""
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
"""

A, B = map(int,input().split())

# 최대 공약수
def gcd(A, B):
    for i in range(min(A,B),1,-1):
        if A % i == 0 and B % i == 0:
            return i
    return 1

# 최소 공배수
def lcm(A, B):
    return (A * B) // gcd(A,B)

print(gcd(A, B))
print(lcm(A, B))