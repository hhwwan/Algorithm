# 내가 푼 것 -> 시간초과
# while (1):
#     n = int(input())
#     if n == 0:
#         break
#     result = None

#     # 2부터 n의 절반까지 반복하며 소수 찾기
#     for i in range(2, n//2 + 1):
#         tmp = True

#         # i가 소수인지 확인
#         for j in range(2, int(i ** 0.5) + 1):
#             if i % j == 0:
#                 tmp = False
#                 break

#         if tmp:
#             # n-i가 소수인지
#             for k in range(2, int((n-i)**0.5) + 1):
#                 if (n-i) % k == 0:
#                     tmp = False
#                     break

#             if tmp:
#                 # 조건을 만족하는 소수쌍 저장
#                 result = (i, n-i) # 가장 마지막에 발견된 소수 쌍이 b-a가 가장 큼

#     if result:
#         a, b = result
#         print(n, '=', a, '+', b)
#     else:
#         print("Goldbach's conjecture is wrong.")