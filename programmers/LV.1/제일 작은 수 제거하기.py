"""
정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요. 
단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 
예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.
"""

def solution(arr):
    key = min(arr) # 시간 단축을 위해 변수에 할당 (반복문 안에서 하면 매번 찾아야함)

    for i in range(len(arr)):
        if key == arr[i]:
            del arr[i]
            break
    if arr:
        return arr
    else:
        return [-1]