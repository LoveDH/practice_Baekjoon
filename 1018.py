# 체스판 다시 칠하기 re-painting chess board

N, M = list(map(int,input().split()))
chess = []
for line in range(N):
    chess.append(list(input()))


global_min_count = 64
for row in range(N-7):
    for col in range(M-7):

        start_B_count = 0
        start_W_count = 0

        start_with_B = 'B'
        start_with_W = 'W'

        for selected_row in range(8):
            start_with_B, start_with_W = start_with_W, start_with_B
            for selected_col in range(8):
                if chess[row+selected_row][col+selected_col] != start_with_B:
                    start_B_count+=1
                if chess[row+selected_row][col+selected_col] != start_with_W:
                    start_W_count+=1
                start_with_B, start_with_W = start_with_W, start_with_B

        if global_min_count > min(start_B_count, start_W_count):
            global_min_count = min(start_B_count, start_W_count)

print(global_min_count)