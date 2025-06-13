"""
정수로 이루어진 배열 numbers가 있습니다. 
배열 의 각 원소들에 대해 자신보다 뒤에 있는 숫자 중에서 자신보다 크면서 가장 가까이 있는 수를 뒷 큰수라고 합니다.
정수 배열 numbers가 매개변수로 주어질 때, 
모든 원소에 대한 뒷 큰수들을 차례로 담은 배열을 return 하도록 solution 함수를 완성해주세요. 
단, 뒷 큰수가 존재하지 않는 원소는 -1을 담습니다.
"""

# 내가 짠 코드 -> 시간초과
def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        exist = False
        for j in range(i+1, len(numbers)):
            if numbers[i] < numbers[j]:
                exist = True
                answer.append(numbers[j])
                break
        if not exist:
            answer.append(-1)  
            
    return answer

# 스택 사용
def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for i in range(len(numbers)-1, -1, -1):
        cur = numbers[i]
        
        # 현재 수보다 stack에 작은 수가 있다면 버림
        while stack and stack[-1] <= cur:
            stack.pop()
        
        if stack:
            answer[i] = stack[-1]
        
        stack.append(cur)
    
    return answer