# 단어 정렬 sorting words

"""
주어진 N개의 단어를 정렬하기
1. 길이가 짧은 것 부터
2. 길이가 같으면 사전순으로
"""

from sys import stdin

N = int(stdin.readline())

word_length = [False]*51

# 길이에 따라 같은 인덱스에 리스트로 추가
for n in range(N):
    word = stdin.readline().rstrip()
    if word_length[len(word)] and word not in word_length[len(word)]:
        word_length[len(word)].append(word)
    else:
        word_length[len(word)] = [word]

# 작은 인덱스부터 정렬하며 출력
for word_group in word_length:
    if word_group:
        word_group.sort()
        print('\n'.join(word_group))

# word_list = [stdin.readline().rstrip() for i in range(N)]
# word_list = list(set(word_list))
# word_list.sort(key=len)
# print('\n'.join())