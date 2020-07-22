# 영화감독 숌 movie director shawm

"""
6이 적어도 3개이상 연속으로 들어가는 수 -> 종말의 숫자
N번째로 작은 종말 숫자는?
"""

N = int(input())

number = 666
count = 0

while True:

    if '666' in str(number):
        count+=1

    # count가 N과 같아지면 break
    if count == N:
        break
    else:
        number+=1
        continue

print(number)
