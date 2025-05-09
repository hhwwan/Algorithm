"""
괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ( 와 ) 만으로 구성되어 있는 문자열이다. 
그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다. 
한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 
만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다. 
그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다. 
예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다. 

여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다. 
"""

import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    stack = []
    PS = list(input()) # 마지막에 자동으로 '\n'이 삽입됨
    
    for j in PS[:-1]: # 마지막꺼 제외하고 반복문 실행
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(j)
                break
    if not stack: # 스택에 남은 문자열이 없다면 즉, VPS 맞음
        print("YES")
    else:
        print("NO")