# 수 정렬하기 3 sorting numbers 3

import sys

N = int(sys.stdin.readline())

count_list = [0] * 10001

for number in range(N):
    count_list[int(sys.stdin.readline())] += 1

for idx in range(len(count_list)):
    if count_list != 0:
        for count in range(count_list[idx]):
            print(idx)