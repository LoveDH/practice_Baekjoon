# 01타일 01tiles

"""
1과 00으로 만들수 있는 이진수의 갯수
"""

from sys import stdin

N = int(stdin.readline())

memo = [0] * 1000001
memo[1] = 1
memo[2] = 2

for i in range(3, N+1):
    memo[i] = ((memo[i-2]%15746)+ (memo[i-1]%15746)) %15746

print(memo[N])