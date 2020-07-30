# 스도쿠 sudoku

"""
스도쿠 문제 빈칸 채우기
"""

from sys import stdin

sudoku = [list(map(int, stdin.readline().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

def backtracking(index):
    
    # 한 바퀴에서 모든 경우를 다 보았으면 출력
    if index == len(zeros):
        for row in sudoku:
            print(*row)
        exit()
    else:
        x = zeros[index][0]
        y = zeros[index][1]
        dx = (x//3) * 3
        dy = (y//3) * 3

        # 사용할 수 있는 숫자 9개
        num_list = [False] + [True for _ in range(9)]

        for j in range(9):
            # 가로 검사
            if(sudoku[x][j]):
                num_list[sudoku[x][j]] = False
            # 세로 검사
            if(sudoku[j][y]):
                num_list[sudoku[j][y]] = False

        # 3*3 box 검사
        for i in range(dx, dx + 3):
            for j in range(dy, dy + 3):
                check_num = sudoku[i][j]
                if(check_num):
                    num_list[check_num] = False

        # 현재 가능한 수만 가져옴
        # 가능한 수를 가져왔으면, 이전에 다뤄왔던 백트래킹을 사용하면 됨
        candidate_list = [i for i, k in enumerate(num_list) if k]
        
        # 경우의 수 고려
        for num in candidate_list:
            sudoku[x][y] = num
            backtracking(index + 1)
            sudoku[x][y] = 0
backtracking(0)