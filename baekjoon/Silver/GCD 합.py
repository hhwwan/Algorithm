"""
양의 정수 n개가 주어졌을 때, 가능한 모든 쌍의 GCD의 합을 구하는 프로그램을 작성하시오.
"""

# math 사용 -> 통과
import math

t = int(input())

for _ in range(t):
    num = list(map(int,input().split()))
    n = num[0] #개수
    nums = num[1:]

    answer = 0

    for i in range(n):
        for j in range(i+1, n):
            answer += math.gcd(nums[i], nums[j])
    
    print(answer)

# 함수 사용 -> 시간 초과
def Gcd(x,y):
    for i in range(max(x,y),1,-1):
        if x % i == 0 and y % i == 0:
            return i
    return 1

t = int(input())

for _ in range(t):
    num = list(map(int,input().split()))
    n = num[0] #개수
    nums = num[1:]

    answer = 0

    for i in range(n):
        for j in range(i+1, n):
            answer += Gcd(nums[i], nums[j])
    
    print(answer)

# 유클리드 호제법 사용
def Gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x