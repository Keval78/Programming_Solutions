from collections import defaultdict
n,m=map(int,input().split())
#print(n,m)
a=list(map(int,input().split()))
#print(a)
ind=[]
dic={}
while(m>0):
    m=m-1
    u,v=map(int,input().split())
    con1=False
    con2=False
    if(u in dic):
        con1=True
    if(v in dic):
        con2=True
    if(not con1 and not con2):
        x=len(ind)
        dic[u]=x
        dic[v]=x
        ind.append(len(ind))
    elif(con1 and not con2):
        x=dic[u]
        dic[v]=x
    elif(not con1 and con2):
        x=dic[v]
        dic[u]=x
    else:
        x=dic[u]
        x1=dic[v]
        ind[x1]=x
    #print(dic)
    #print(ind)
v = defaultdict(list)
for key in dic:
    x=dic[key]
    if x not in v:
        v[x].append(a[key-1])
        v[x].append(1)
    else:
        if v[x][0]<a[key-1]:
            v[x][0]=a[key-1]
            v[x][1]=1
        elif v[x][0]==a[key-1]:
            temp=v[x][1]
            temp=temp+1
            v[x][1]=temp
#print(v)
mul=1
for key in v:
    mul=(mul*v[x][1])%1000000007
print(mul)
