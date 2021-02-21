# https://www.acmicpc.net/problem/11399

N = int(input())
wait_list = list(map(int, input().split()))
wait_list.sort()
sum_list = []

res = 0
for i in range(N):
    sum_list.append(wait_list[i])
    res += sum(sum_list)

print(res)