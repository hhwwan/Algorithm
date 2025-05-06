"""
경화는 과수원에서 귤을 수확했습니다. 경화는 수확한 귤 중 'k'개를 골라 상자 하나에 담아 판매하려고 합니다. 
그런데 수확한 귤의 크기가 일정하지 않아 보기에 좋지 않다고 생각한 경화는 귤을 크기별로 분류했을 때 서로 다른 종류의 수를 최소화하고 싶습니다.

예를 들어, 경화가 수확한 귤 8개의 크기가 [1, 3, 2, 5, 4, 5, 2, 3] 이라고 합시다. 
경화가 귤 6개를 판매하고 싶다면, 크기가 1, 4인 귤을 제외한 여섯 개의 귤을 상자에 담으면, 
귤의 크기의 종류가 2, 3, 5로 총 3가지가 되며 이때가 서로 다른 종류가 최소일 때입니다.

경화가 한 상자에 담으려는 귤의 개수 k와 귤의 크기를 담은 배열 tangerine이 매개변수로 주어집니다. 
경화가 귤 k개를 고를 때 크기가 서로 다른 종류의 수의 최솟값을 return 하도록 solution 함수를 작성해주세요.
"""

# 내가 푼 것 -> 시간초과
from collections import Counter

def solution(k, tangerine):
    answer = 0
    tangerine_dict = Counter(tangerine) # 각 숫자별로 카운트

    while k > 0:
        most_tangerine = max(tangerine_dict, key = lambda x: tangerine_dict[x]) # 가장 많은 사이즈의 귤 찾기
        k -= tangerine_dict[most_tangerine] # 가장 많은 개수의 귤부터 k에서 빼기
        del tangerine_dict[most_tangerine] # 위에 사용한 숫자는 뺴기
        answer += 1
        
    return answer

# while문 밖에서 정렬 후 for문 돌리기 
from collections import Counter

def solution(k, tangerine):
    answer = 0
    tangerine_dict = Counter(tangerine) # 각 숫자별로 카운트
    
    # value 기준으로 내림차순 정렬된 리스트 생성
    sorted_counts = sorted(tangerine_dict.values(), reverse=True)

    for count in sorted_counts:
        k -= count # 가장 많은 개수부터 빼기
        answer += 1
        if k <= 0:
            break
        
    return answer