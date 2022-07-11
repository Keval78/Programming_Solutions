t = int(input())
while t > 0:
    n, a, b = map(int,input().split())
    s = input()
    zero_count = 0
    for i in range(0,n):
        if s[i] == '0':
            zero_count += 1
    print((zero_count*a)+(b*(n-zero_count)))
    t-=1