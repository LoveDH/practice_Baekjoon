# 정수 삼각형 Integer triangle

"""
삼각형을 내려오면서 수의 합이 최대가 되게하는 경로
"""

from sys import stdin

def find_best_way(size):

    for i in range(size-1):
        for j in range(len(triangle[i+1])):
            if(j == 0):
                triangle[i + 1][j] = triangle[i][j] + triangle[i + 1][j]
            elif(j == len(triangle[i + 1]) - 1):
                triangle[i + 1][-1] = triangle[i][-1] + triangle[i + 1][-1]
            else:
                triangle[i + 1][j] = max(triangle[i][j - 1] + triangle[i + 1][j], triangle[i][j] + triangle[i + 1][j])
    return max(triangle[-1])

size = int(stdin.readline())
triangle = [list(map(int,stdin.readline().split())) for _ in range(size)]

print(find_best_way(size))