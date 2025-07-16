"""
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 
종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
"""

from itertools import permutations

def Prime(x):
    if x <= 1:
        return 0
    elif x == 2:
        return 1
    else:
        found = False
        for i in range(2, x // 2 + 1):
            if x % i == 0:
                found = True
                return 0
        
        if not found:
            return 1
            

def solution(numbers):
    answer = 0
    
    all_nums = set()
    
    for i in range(1, len(numbers) + 1):
        perms = permutations(numbers, i)
        
        for j in perms:
            num_str = ''.join(j)
            num = int(num_str)
            all_nums.add(num)
    
    for i in all_nums:
        if Prime(i):
            answer += 1
        
        
    return answer