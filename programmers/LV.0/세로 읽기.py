"""
문자열 my_string과 두 정수 m, c가 주어집니다. my_string을 한 줄에 m 글자씩 가로로 적었을 때
왼쪽부터 세로로 c번째 열에 적힌 글자들을 문자열로 return 하는 solution 함수를 작성해 주세요.
"""

def solution(my_string, m, c):
    answer = []
    result = []
    for i in range(1,len(my_string)//m+1):
        answer.append(my_string[m*i-m:m*i])
    for j in answer:
        result.append(j[c-1])
    return ''.join(result)

def solution(my_string, m, c):
    return my_string[c-1::m]