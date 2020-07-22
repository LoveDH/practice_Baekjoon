# 통계학 statistics

"""
N개의 수가 주어졌을때, 산술평균, 중앙값, 최빈값, 범위를 구하는 프로그램
"""

from sys import stdin

N = int(stdin.readline())
count_list = [0]*8001
_sum = 0
sorted_list = []

#counting sort 이용
for tmp in range(N):
    input_number =  int(stdin.readline())
    count_list[input_number+4000] += 1
    _sum += input_number

for idx in range(len(count_list)):
    if count_list[idx] != 0:
        sorted_list.extend([idx-4000]*count_list[idx])

# 산술평균
print(int(round(_sum/N,0)))

# 중앙값
print(sorted_list[N//2])

# 최빈값
max_count = max(count_list)
try:
    mode = count_list.index(max_count,count_list.index(max_count)+1) - 4000
except:
    mode = count_list.index(max_count) - 4000
print(mode)

# 범위
print(sorted_list[-1] - sorted_list[0])