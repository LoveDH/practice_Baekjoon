# 파도반 수열 padovan sequence

"""
파도반 수열의 N번째 수
"""

from sys import stdin

# 파도반 수열 계산 함수
def padovan(N):
    global mem
    
    for cnt in range(1,N+1):
        # 메모에 기록이 되어있지 않다면 새로 계산
        if mem[cnt] == -1:
            mem[cnt] = mem[cnt-1] + mem[cnt-5]
        else:
            continue
    return mem[N]

T = int(stdin.readline())
inputs = [int(stdin.readline()) for _ in range(T)]

# 초깃값
mem = [-1,1,1,1,2,2] + [-1]*95

for inp in inputs:
    print(padovan(inp))