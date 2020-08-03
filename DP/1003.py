# 피보나치 함수 fibonacci function

"""
피보나치를 재귀로 한다면 1과 0을 얼마나 출력할까
"""

from sys import stdin

#주어진 함수
def fibonacci(n):
    global count_0, count_1

    if n==0:
        count_0+=1
        return 0
    elif n==1:
        count_1+=1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#동적 계획법
def fib(n):
    if n==0:
        return 0
    elif n==-1:
        return 1
    mem = [0]*(n+1)
    mem[0] = 0
    mem[1] = 1
    for k in range(2,n+1):
        mem[k] = mem[k-2] + mem[k-1]
    return mem[n]


# 테스트케이스 수와 입력값
num_T = int(stdin.readline())
T = [int(stdin.readline()) for _ in range(num_T)]

# 테스트 해본 결과 입력값이 n일때 
# count_0은 피보나치의 n-1번째 수
# count_1은 피보나치의 n번째 수

# 테스트 코드
# while True:
#     case = int(input())
#     count_0, count_1 = 0, 0
#     fibonacci(case)
#     print(count_0, count_1)

for case in T:
    print(fib(case-1), fib(case))