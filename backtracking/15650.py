# N과 M (2) N & M (2)

"""
N개의 숫자에서 M개를 뽑아 수열을 만든다.
단, 수열은 오름차순
"""

from sys import stdin

#입력
N, M = map(int,stdin.readline().split())

#방문 여부와 수열을 저장할 리스트 생성
visited = [0]*(N+1)
seq = [0]*M

#백트래킹 알고리즘
def backtracking(index, n, m):
    #말단 노드에 도달하면 수열 출력
    if index == m:
        for num in seq:
            print(num, end=' ')
        print()
        return
    
    #이전 숫자보다 큰 숫자들에 대해 반복
    for num in range(seq[index-1],N+1):
        #이미 방문한 노드라면 넘어감
        if visited[num] or num==0:
            continue
        visited[num]=True
        seq[index]=num

        #재귀적으로 함수 호출
        backtracking(index+1, n, m)

        #방문 여부를 해제함 (다른 경로에서 재방문하기 위해)
        visited[num]=False

backtracking(0, N, M)