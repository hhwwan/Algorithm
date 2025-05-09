"""
머쓱이는 태어난 지 6개월 된 조카를 돌보고 있습니다. 
조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음을 최대 한 번씩 사용해 조합한(이어 붙인) 발음밖에 하지 못합니다. 
문자열 배열 babbling이 매개변수로 주어질 때, 
머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.
"""

def solution(babbling):
    answer = 0
    word = ["aya", "ye", "woo", "ma"]
    
    for i in babbling:
        for j in word:
            if j in i:
                i = i.replace(j,' ') # word안에 있는 단어면 빈칸으로 변경
        i = i.replace(' ','') # 빈칸 없애기
        if i == '':
            answer += 1
    return answer