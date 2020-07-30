# N-Queen

"""
N이 주어졌을때의 N-퀸 문제 해결 방법 수
"""

from sys import stdin

def not_wrong(index):
    for cur_idx in range(index):
        if seq[index] == seq[cur_idx] or abs(seq[index]-seq[cur_idx]) == index - cur_idx:
            return False
    return True

def backtracking(index):
    global count

    if index == N:
        count+=1

    else:
        for num in range(N):
            seq[index] = num
            if not_wrong(index):
                backtracking(index+1)

N = int(stdin.readline())
count = 0
seq = [0]*N
backtracking(0)
print(count)