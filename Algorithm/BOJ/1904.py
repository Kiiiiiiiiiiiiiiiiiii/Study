#수열의 길이가 i일때 경우의 수

n = int(input())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for i in range (3, n+1):
    dp[i] = (dp[i-2] + dp[i-1]) % 15746

print(dp[n])
