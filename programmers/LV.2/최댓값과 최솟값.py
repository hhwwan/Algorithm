"""
문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. 
str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.
예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.

s	return
"1 2 3 4"	"1 4"
"-1 -2 -3 -4"	"-4 -1"
"-1 -1"	"-1 -1"
"""

# 내가 푼 것
def solution(s):
    answer = ''
    num_list = s.split()
    new_list = []
    
    # 새로운 리스트에 int형으로 변환 후 삽입
    for i in num_list:
        new_list.append(int(i))
    
    # 최소값, 최대값 찾고 문자형으로 삽입
    answer += str(min(new_list)) 
    answer += ' '
    answer += str(max(new_list))
    
    return answer

# 모범답안
def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))