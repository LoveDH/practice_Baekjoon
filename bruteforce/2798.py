# 블랙잭 Blackjack

N, M = map(lambda x: int(x), input().split())
cards = list(map(lambda x: int(x), input().split()))

_max = 0
for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            _sum = cards[i]+cards[j]+cards[k]
            if _sum > _max and _sum <= M:
                _max = _sum
print(_max)