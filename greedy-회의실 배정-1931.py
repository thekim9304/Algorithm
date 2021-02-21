import sys

N = int(sys.stdin.readline())
meet_list = []
for _ in range(N):
    meet_list.append([*map(int, sys.stdin.readline().split())])
    meet_list[-1].append(meet_list[-1][1] - meet_list[-1][0])

meet_list.sort(key=lambda x: x[0])
meet_list.sort(key=lambda x: x[1])

meet_cnt = 1
e_time = meet_list[0][1]
for i in range(1, N):
    if meet_list[i][0] >= e_time:
        e_time = meet_list[i][1]
        meet_cnt += 1

print(meet_cnt)