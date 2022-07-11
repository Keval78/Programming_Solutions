n,k,q=map(int,input().split())
a=list(map(int,input().split()))
b=[]
for i in range(len(a)):
    if i==0:
        dic={}
    else:
        dic=b[i-1].copy()
    j=a[i]
    #print("j is",j)
    if j in dic:
        x=dic[j]
        x=x+1
        dic[j]=x
    else:
        dic[j]=1
    b.append(dic)
    #print(b)
ans=0
while(q>0):
    q=q-1
    count=0
    l,r=map(int,input().split())
    sp=min((l+ans)%n,(r+ans)%n)
    ep=max((l+ans)%n,(r+ans)%n)
    #print("range is(",sp," , ",ep,")")
    if sp>0:
        d1=b[sp-1].copy()
    else:
        d1={}
    d2=b[ep].copy()
    #print("d2 is",d2)
    #print("d1 is",d1)
    for key in d2:
        if key in d1:
            x=d2[key]-d1[key]
            d2[key]=x
    for key in d2:
        if d2[key]==k:
            count=count+1
    ans=count
    print(count)
