# https://www.acmicpc.net/problem/1932

import sys

n = int(sys.stdin.readline())

rect_num = []
res_list = []
for i in range(n):
    rect_num.append(list(map(int, sys.stdin.readline().split())))
    res_list.append([0] * (i + 1))

res_list[0] = rect_num[0]
for i in range(1, n):
    for j in range(len(rect_num[i])):
        if j == 0:  # 맨 왼쪽 값
            res_list[i][j] = rect_num[i][j] + res_list[i - 1][j]
        elif j == (len(rect_num[i]) - 1):  # 맨 오른쪽 값
            res_list[i][j] = rect_num[i][j] + res_list[i - 1][j - 1]
        else:  # 중앙 값
            res_list[i][j] = rect_num[i][j] + max(res_list[i - 1][j - 1], res_list[i - 1][j])

print(max(res_list[n - 1]))