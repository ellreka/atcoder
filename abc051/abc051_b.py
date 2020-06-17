# https://atcoder.jp/contests/abc051/tasks/abc051_b

k, s = map(int, input().split())

ans = 0
for x in range(k + 1):
    for y in range(k + 1):
        z = s - (x + y)
        if 0 <= z and z <= k:
            ans += 1

print(ans)

# 3重ループすると時間計算量がO(K^3)となってしまうのでダメ
