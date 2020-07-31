# 스타트와 링크 start and link

"""
N명을 두팀으로 나누었을때 능력치의 차이가 최소가 되도록하는 방법
"""

from sys import stdin

def cal(start):
    global _min
    score = 0
    link = [i for i in range(1,N+1) if i not in start]

    for i in range(len(start)):
        for j in range(len(start)):
            if i != j:
                score += scores[start[i]-1][start[j]-1]
                score -= scores[link[i]-1][link[j]-1]

    if _min >= abs(score):
        _min = abs(score)

def backtracking(index, N, m):
    if index == m:
        cal(start_team)
        return
    else:
        for person in range(start_team[index-1],N+1):
            if visited[person] or person==0:
                continue
            start_team[index]=person
            visited[person]=True
            backtracking(index+1, N, m)
            visited[person]=False

N = int(stdin.readline())
scores = [list(map(int,stdin.readline().split())) for _ in range(N)]
start_team = [0]*(N//2)
visited = [0]*(N+1)
_min = 100*(N//2)
backtracking(0, N, N//2)
print(_min)