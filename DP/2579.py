# 계단 오르기 Stair climb

"""
계단을 오르며 점수 쌓기
1. 한번에 한계단 혹은 두 계단 오를 수 있음
2. 연속된 세계의 계단을 밟아선 안됨
3. 마지막 도착 계단을 반드시 밟아야함
얻을수 있는 점수의 최댓값 구하기
"""

from sys import stdin

def climb(num):
    score = [stairs[0]]
    if num == 1:
        return score[0]
    score.append(score[0]+stairs[1])
    if num == 2:
        return score[-1]

    score.append(max(stairs[2]+score[0], stairs[2]+stairs[1]))

    for step in range(3,num):
        score.append(max(stairs[step] + stairs[step-1] + score[step-3],
                         stairs[step] + score[step-2]))
    
    return score[-1]

num_stairs = int(stdin.readline())
stairs = [int(stdin.readline()) for _ in range(num_stairs)]
print(climb(num_stairs))