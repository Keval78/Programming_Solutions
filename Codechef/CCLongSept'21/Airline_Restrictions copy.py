t = int(input())
while t > 0:
    a, b, c, d, e = map(int,input().split())
    if (a+b+c) > (d+e):
        print("NO")
    else:
        if ((a+b)<=d and c<=e) or ((b+c)<=d and a<=e) or ((c+a)<=d and b<=e):
            print("YES")
        else:
            print("NO")
    t-=1