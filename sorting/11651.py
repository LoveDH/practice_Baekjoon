# 좌표 정렬하기 sorting points

"""
주어진 (x,y) 좌표 정렬하기
"""
from sys import stdin

N = int(stdin.readline())

#radix sort 사용
new_p_list1 = [False]*200001
new_p_list2 = [False]*200001

for n in range(N):
    p = list(map(int,stdin.readline().split()))
    if new_p_list1[p[0]+100000]:
        new_p_list1[p[0]+100000].append(p)
    else:
        new_p_list1[p[0]+100000]= [p]

for p in new_p_list1:
    if p:
        for new_p in p:
            if new_p_list2[new_p[1]+100000]:
                new_p_list2[new_p[1]+100000].append(new_p)
            else:
                new_p_list2[new_p[1]+100000]= [new_p]
            
for p in new_p_list2:
    if p:
        for new_p in p:
            print(new_p[0],new_p[1])