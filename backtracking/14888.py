# 연산자 끼워넣기 Insert Operator

"""
N개의 수와 N-1개의 연산자로 만들수있는 가장 큰 수와 작은 수
"""

from sys import stdin

#식 계산 함수
def cal(selected):
    global _max, _min

    value = numbers[0]
    for op in range(len(selected)):
        if selected[op] == 0:
            value += numbers[op+1]
        elif selected[op] == 1:
            value -= numbers[op+1]
        elif selected[op] == 2:
            value *= numbers[op+1]
        elif selected[op] == 3:
            if value>=0:
                value //= numbers[op+1]
            if value<0:
                value = -(abs(value)//numbers[op+1])

    if _max <= value:
        _max = value

    if _min >= value:
        _min = value        

#백트래킹 알고리즘
def backtracking(index):
    if index == N-1:
        cal(selected)
        return

    for i in range(4):
        #갯수가 모자라면 넘어감
        if operators[i]==0:
            continue
        selected[index] = i
        operators[i] -= 1
        backtracking(index+1)
        operators[i] += 1

N = int(stdin.readline())
numbers = list(map(int,stdin.readline().split()))
operators = list(map(int,stdin.readline().split()))

#연산자 노드 경로 저장
selected = [0]*(N-1)

#최댓값과 최솟값 선언
_max = -1000000000
_min = 1000000000

backtracking(0)
print(_max)
print(_min)