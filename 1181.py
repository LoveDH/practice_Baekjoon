# 단어 정렬 sorting words

"""
주어진 N개의 단어를 정렬하기
1. 길이가 짧은 것 부터
2. 길이가 같으면 사전순으로
"""

from sys import stdin

N = int(stdin.readline())

words = list(set([stdin.readline().rstrip() for _ in range(N)]))
words.sort(key=lambda x: (len(x), x))
for word in words:
    print(word)

