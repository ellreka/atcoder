# https://atcoder.jp/contests/arc004/tasks/arc004_1

import math
n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
print(n, l)

max_d = 0

for i in range(n):
    for j in range(n):
        d = math.sqrt((l[i][0] - l[j][0]) ** 2 + (l[i][1] - l[j][1]) ** 2)
        max_d = max(max_d, d)

print(max_d)

# 2点間の距離は√(x2 - x1) ** 2 + (y2 - y1) ** 2
