# 덩치 Big

N = int(input())

data = []
for i in range(0,N):
    data.append(tuple(map(int, input().split(' '))))

rank = [0]*N
for idx in range(0,N):
    count = 0
    for compare in range(0,N):
        if idx == compare:
            continue
        elif data[compare][0] > data[idx][0] and data[compare][1] > data[idx][1]:
            count+=1
    rank[idx]+=count+1

for tmp in rank:
    print(tmp, end=' ')