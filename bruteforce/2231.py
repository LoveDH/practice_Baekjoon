# 분해합 Decomposition

N = int(input())

found = False
for num in range(0,N):
    num_digits = [int(i) for i in list(str(num))]
    _sum = num + sum(num_digits)
    if _sum == N:
        print(num)
        found = True
        break
if found == False:
    print(0)