# 1로 만들기 making 1

"""
주어진 수에 다음 연산을 한다.
1. 3으로 나누어떨어지면 3으로 나눈다
2. 2로 나누어떨어지면 2로 나눈다
3. 1을 뺀다
위 연산을 사용하는 횟수의 최솟값을 구한다
"""

from sys import stdin

def calculation(N):
    
    # 메모 초기화
    dp = [0,0,1,1]

    # N이 3이하면 초깃값에서 출력
    if N <= 3:
        return dp[N]
    
    # 나머지 자릿수 추가
    dp += [0]*(N-3)

    for idx in range(4,N+1):
        # 2와 3으로 나누어떨어지지 않으면? 이전 항의 값
        if idx%2!=0 and idx%3!=0:
            dp[idx] = dp[idx-1]+1

        # 2로만 나누어 떨어지면? 이전항과 2로 나눈 항 중 작은값
        elif idx%2==0 and idx%3!=0:
            dp[idx] = min(dp[idx//2]+1, dp[idx-1]+1)

        # 3으로만 나누어 떨어지면? 이전항과 3으로 나눈 항 중 작은값
        elif idx%2!=0 and idx%3==0:
            dp[idx] = min(dp[idx//3]+1, dp[idx-1]+1)

        # 그 밖의 경우(2와 3의 공배수) 이전항, 2로 나눈 항, 3으로 나눈 항 중 최솟값
        else:
            dp[idx] = min(dp[idx//2]+1, dp[idx//3]+1, dp[idx-1]+1)

    return dp[-1]

N = int(stdin.readline())
print(calculation(N))