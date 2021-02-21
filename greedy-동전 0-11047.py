# https://www.acmicpc.net/problem/11047

import sys

N, K = map(int, sys.stdin.readline().split())

v_list = []
for _ in range(N):
    v_list.append(int(sys.stdin.readline()))
v_list.reverse()

coin_cnt = 0
for i in range(N):
    if K == 0:
        break
    if K // v_list[i] != 0:
        coin_cnt += K // v_list[i]
        K -= ((K // v_list[i]) * v_list[i])

print(coin_cnt)
