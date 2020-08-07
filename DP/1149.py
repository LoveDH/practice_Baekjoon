# RGB거리 RGB street

"""
규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값
1. 1번 집의 색은 2번집과 달라야함
2. N번 집의 색은 N-1번 집과 달라야함
3. i(2<=i<=N-1)번 집의 색은 i-1번, i+1번과 달라야함
"""

from sys import stdin

def cost(N):
    # DP를 저장할 리스트 생성 및 초기화
    RGB = [total_costs[0]]
    for num in range(1,N):

        local_costs = []
        #이전 항의 값 + 다음 항의 최솟값(이전 항의 인덱스는 제외)
        local_costs.append(total_costs[num][0] + min(RGB[num-1][1],RGB[num-1][2]))
        local_costs.append(total_costs[num][1] + min(RGB[num-1][0],RGB[num-1][2]))
        local_costs.append(total_costs[num][2] + min(RGB[num-1][0],RGB[num-1][1]))

        RGB.append(local_costs)

    return min(RGB[-1])

#입력값
N = int(stdin.readline())
total_costs = [list(map(int, stdin.readline().split())) for _ in range(N)]
print(cost(N))