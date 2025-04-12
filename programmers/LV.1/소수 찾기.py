"""
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)
"""

# 내가 푼 코드

def solution(n):
    answer = 0
    for i in range(2, n+1):
        cnt = 0
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                cnt += 1
                break
        if cnt == 0:
            answer += 1
    return answer

# 에라토스테네스의 체

def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
