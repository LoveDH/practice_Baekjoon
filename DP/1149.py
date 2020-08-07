# RGB거리 RGB street

"""
규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값
1. 1번 집의 색은 2번집과 달라야함
2. N번 집의 색은 N-1번 집과 달라야함
3. i(2<=i<=N-1)번 집의 색은 i-1번, i+1번과 달라야함
"""

from sys import stdin

def cost(N):
    for num in range(N):
        mem[num] = bills[num].index(max(bills[num]))
    return 

N = int(stdin.readline())
bills = [list(map(int, stdin.readline().split())) for _ in range(N)]
mem = [-1]*N
print(cost(N))