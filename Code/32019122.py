n,m,g=map(int,input().split())
t=list(map(int,input().split()))
a=list(map(int,input().split()))
j=t[0]
print(t[0])
max_d=0
count=0
for i in t:
    if max_d<i-j:
        max_d=i-j
    j=i
for i in a:
    if max_d>=i:
        count=count+1
print(count)
