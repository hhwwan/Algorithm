"""
자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 
이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.
"""

def solution(n):
    three_jin = []
    answer = 0
    while n >= 3:
        three_jin.append(n%3)
        n //= 3
    three_jin.append(n)
    print(three_jin)
    for i in range(len(three_jin)):
        answer += three_jin[i] * 3**(len(three_jin)-i-1)
        print(answer)
    return answer