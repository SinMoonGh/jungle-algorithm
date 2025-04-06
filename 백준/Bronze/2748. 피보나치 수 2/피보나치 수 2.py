import sys

input_s = sys.stdin.readline

def climb_stairs(n):
    dp = [0] * (n+1)

    if n <= 1:
        return 1
    
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


def pivo(n):
    dp = [0] * (n+1)

    for i in range(1, n+1):
        if i <= 1:
            dp[i] = i
            continue

        dp[i] = dp[i-1] + dp[i-2]
    # print(dp)
    return dp[n]


n = int(input_s())
print(pivo(n))