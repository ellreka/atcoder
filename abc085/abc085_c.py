# https://atcoder.jp/contests/abc085/tasks/abc085_c

cnt, total = map(int, input().split())

def main():
    for a in range(cnt + 1):
        for b in range(cnt - a + 1):
                c = cnt - (a + b)
                if total == 10000 * a + 5000 * b + 1000 * c:
                    print(a, b, c)
                    return
    print(-1, -1, -1)

main()
