"""
피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.

예를들어

F(2) = F(0) + F(1) = 0 + 1 = 1
F(3) = F(1) + F(2) = 1 + 1 = 2
F(4) = F(2) + F(3) = 1 + 2 = 3
F(5) = F(3) + F(4) = 2 + 3 = 5
와 같이 이어집니다.

2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.
"""

# 내가 푼것 -> 런타임 에러 및 시간초과
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1)+ fibonacci(num-2)

def solution(n):
    answer = fibonacci(n)
    
    return answer

# 정답 풀이
def solution(n):
    after = 0
    before = 1
    for _ in range(2, n + 1):
        num = before
        before = after + num
        after = num
    return before % 1234567