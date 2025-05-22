"""
후위 표기식과 각 피연산자에 대응하는 값들이 주어져 있을 때, 그 식을 계산하는 프로그램을 작성하시오.

첫째 줄에 피연산자의 개수(1 ≤ N ≤ 26) 가 주어진다. 그리고 둘째 줄에는 후위 표기식이 주어진다. 
(여기서 피연산자는 A~Z의 영대문자이며, A부터 순서대로 N개의 영대문자만이 사용되며, 
길이는 100을 넘지 않는다) 그리고 셋째 줄부터 N+2번째 줄까지는 각 피연산자에 대응하는 값이 주어진다. 
3번째 줄에는 A에 해당하는 값, 4번째 줄에는 B에 해당하는값 , 5번째 줄에는 C ...이 주어진다, 
그리고 피연산자에 대응 하는 값은 100보다 작거나 같은 자연수이다.

후위 표기식을 앞에서부터 계산했을 때, 식의 결과와 중간 결과가 -20억보다 크거나 같고, 20억보다 작거나 같은 입력만 주어진다.
"""
import sys
input = sys.stdin.readline

N = int(input())
formula = input()
num = [int(input()) for _ in range(N)]
stack = []

for i in formula:
    if 'A' <= i <='Z' :
        stack.append(num[ord(i) - ord('A')])
    else:
        if len(stack) >= 2:
            x = stack.pop()
            y = stack.pop()

            if i == '+':
                stack.append(y+x)
            elif i == '-':
                stack.append(y-x)
            elif i == '*':
                stack.append(y*x)
            elif i == '/':
                stack.append(y/x)

print("{:.2f}".format(stack.pop())) # 소수점 둘째자리에서 반올림