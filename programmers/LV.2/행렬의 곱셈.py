"""
2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.
"""

def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)): # arr1 순회
        row = []
        for j in range(len(arr2[0])): # arr2 순회
            tmp = 0
            for k in range(len(arr2)):
                tmp += arr1[i][k] * arr2[k][j]
            row.append(tmp)
        answer.append(row)
    return answer