# 소트인사이드 sort inside

"""
주어진 수의 자릿수를 내림차순으로 정렬
"""

from sys import stdin

nums = list(map(int,list(stdin.readline().strip())))

nums.sort()
print(''.join(list(map(str,nums[::-1]))))