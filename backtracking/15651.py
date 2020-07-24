# N과 M (3) N & M (3)

"""
N개의 숫자에서 M개를 뽑아 수열을 만든다.
단, 같은 수를 여러번 골라도 됌
"""

from sys import stdin, stdout

#입력
N, M = map(int,stdin.readline().split())

#수열을 저장할 리스트 생성
#방문 여부가 필요가 없다. 모든 경우의 수를 탐색해야한다.
seq = [0]*M

#백트래킹 알고리즘
def backtracking(index, n, m):

    #말단 노드에 도달하면 수열 출력
    if index == m:
        for num in seq:
            stdout.write(str(num)+' ')
        stdout.write('\n')
        return
    
    #모든 숫자에 대해 반복
    for num in range(1,N+1):
        seq[index]=num
        #재귀적으로 함수 호출
        backtracking(index+1, n, m)

backtracking(0, N, M)