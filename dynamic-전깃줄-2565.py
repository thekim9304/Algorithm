# https://www.acmicpc.net/problem/2565
# 최장 증가 수열(Longest Increasing Subsequence, LIS)

import sys

n = int(sys.stdin.readline())
dp = [1] * n
AB_list = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    AB_list.append([a, b])

AB_list.sort(key=lambda x: x[0])
for i in range(n):
    for j in range(i):
        if AB_list[i][1] > AB_list[j][1]:  # 증가 수열이면
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))