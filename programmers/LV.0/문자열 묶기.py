"""
문자열 배열 strArr이 주어집니다. 
strArr의 원소들을 길이가 같은 문자열들끼리 그룹으로 묶었을 때 
가장 개수가 많은 그룹의 크기를 return 하는 solution 함수를 완성해 주세요.
"""

def solution(strArr):
    answer = 0
    temp = []
    
    for i in strArr:
        temp.append(len(i))
    temp.sort()
    
    for i in range(temp[-1]+1):
        if answer <= temp.count(i):
            answer = temp.count(i)
    return answer