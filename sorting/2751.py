# 수 정렬하기 2 sorting numbers 2

import sys

N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for i in range(N)]

numbers.sort()

for number in numbers:
    print(number)