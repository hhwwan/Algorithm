"""
이차원 정수 배열 arr이 매개변수로 주어집니다. 
arr의 행의 수가 더 많다면 열의 수가 행의 수와 같아지도록 각 행의 끝에 0을 추가하고, 
열의 수가 더 많다면 행의 수가 열의 수와 같아지도록 각 열의 끝에 0을 추가한 
이차원 배열을 return 하는 solution 함수를 작성해 주세요.
"""

def solution(arr):
    # 배열의 길이가 같지 않다면 반복
    while len(arr) != len(arr[0]):
        # 행의 수가 더 많을 때
        if len(arr) > len(arr[0]):
            for i in range(len(arr)):
                arr[i].append(0)
        # 열의 수가 더 많을 때
        elif len(arr) < len(arr[0]):
            for i in range(len(arr), len(arr[0])):
                arr.append([0]*len(arr[0]))
    return arr