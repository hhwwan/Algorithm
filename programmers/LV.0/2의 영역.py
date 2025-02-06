"""
정수 배열 arr가 주어집니다. 배열 안의 2가 모두 포함된 가장 작은 연속된 부분 배열을 return 하는 solution 함수를 완성해 주세요.

단, arr에 2가 없는 경우 [-1]을 return 합니다.
"""

def solution(arr):
    x = 0
    y = 0
    for i in range(len(arr)):
        if arr[i] == 2:
            x = i
            break
    for j in range(1, len(arr)):
        if arr[-j] == 2:
            y = j
            break
    if x == 0 and y == 0:
        return [-1]
    else:
        return arr[x:len(arr)+1 - y]