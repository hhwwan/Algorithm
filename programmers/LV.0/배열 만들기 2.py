"""
정수 l과 r이 주어졌을 때, l 이상 r이하의 정수 중에서 숫자 "0"과 "5"로만 이루어진 
모든 정수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

만약 그러한 정수가 없다면, -1이 담긴 배열을 return 합니다.
"""

def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if not set(str(i)) - set(['0', '5']):
            answer.append(i)

    if not answer:
        return [-1]
    
    return answer