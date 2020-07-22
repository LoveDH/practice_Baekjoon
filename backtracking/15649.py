# N과 M (1)  N & M (1)

"""
자연수 N과 M이 주어졌을 때, 1부터 N까지 자연수 중에서 M개를 고른 수열 출력
"""

from sys import stdin, stdout


N, M = map(int,stdin.readline().split())

visited = [0]*(N+1)
a = [0]*M

def go(index, n, m):
    if index == m:
        for i in range(m):
            print(a[i], end=' ')
        print()
        return
    
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        a[index] = i
        go(index+1, n, m)
        visited[i] = False

go(0, N, M)