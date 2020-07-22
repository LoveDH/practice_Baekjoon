# 수 정렬하기 sorting numbers

"""
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램
"""

def quickSort(num_list):
    if len(num_list) <= 1 : return num_list
    pivot = num_list[len(num_list)//2]
    less_arr, equal_arr, big_arr = [], [], []
    for i in num_list:
        if i < pivot : less_arr.append(i)
        elif i > pivot : big_arr.append(i)
        else : equal_arr.append(i)
    return quickSort(less_arr) + equal_arr + quickSort(big_arr)

N = int(input())
number_list = [int(input()) for i in range(N)]

for num in quickSort(number_list):
    print(num)