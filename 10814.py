# 나이순 정렬 sort by age

"""
나이와 이름이 주어질때, 나이가 증가하는 순으로 나열하기
이때 나이가 같으면 먼저 가입한 사람이 앞에 오도록 정렬
"""

from sys import stdin

N = int(stdin.readline())
user_list = [stdin.readline().split() for _ in range(N)]
user_list.sort(key=lambda x: int(x[0]))

for user in user_list:
    print(user[0],user[1])