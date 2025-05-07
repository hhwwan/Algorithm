"""
두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 
예를 들어 2와 7의 최소공배수는 14가 됩니다. 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. 
n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.
"""

# 최소공배수 구하기
def lcm(a,b):
    for i in range(max(a,b), (a*b)+1):
        if i % a == 0 and i % b == 0:
            return i
    

def solution(arr):
    # 가장 작은 두 숫자부터 차례대로 최소공배수 구하기
    while len(arr) > 1:
        arr.sort()
        lcm_num = lcm(arr[0],arr[1])
        del arr[:2]
        arr.append(lcm_num)
        
    return lcm_num