# 피보나치 수 2 fibonacci numbers 2

"""
n번째 피보나치 수 구하기
"""

from sys import stdin

def fib(n):
    mem[0] = 0
    mem[1] = 1
    for k in range(2,n+1):
        mem[k] = mem[k-2] + mem[k-1]
    return mem[n]

n = int(stdin.readline())
mem = [0]*(n+1)
print(fib(n))