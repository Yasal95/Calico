t = int(input())

for _ in range(t):
    b, l, e = map(int, input().split())

    # years from birth to first shower I can see
    first = (e + b) % 50

    if first > l:
        print(0)
    else:
print(1 + (l - first) // 50)
input:
3
10 100 0
0 20 0
5 10 49
output:
2
1
1
