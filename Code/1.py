from collections import defaultdict
import math
def divSum(num):
    result = 0
    i = 2
    while i<= (math.sqrt(num)) :
        if (num % i == 0) :
            if (i == (num / i)) :
                result = result + i;
            else :
                result = result +  (i + num/i);
        i = i + 1
    return (result + 1);
def update2(Seg,ss,se,i,diff,si):
    if i<ss or i>se:
        return
    Seg[si]+=diff
    if se!=ss:
        mid=ss+(se-ss)//2
        update2(Seg,ss,mid,i,diff,2*si+1)
        update2(Seg,mid+1,se,i,diff,2*si+2)

def update(arr,Seg,n,i,x):
    if i<0 or i>n-1:
        return
    #Logic for min/max/sum/multipy/and/or/xor here...
    diff=x-arr[i]
    arr[i]=x
    update2(Seg,0,n-1,i,diff,0)

def getS(Seg,n,s,t):
    if s<0 or t>n-1 or s>t:
        return -1
    return getS2(Seg,0,n-1,s,t,0)

def getS2(Seg,ss,se,qs,qe,si):
    if qs<=ss and qe>=se:
        return Seg[si]
    if se<qs or ss>qe:
        return 0
    mid=ss+(se-ss)//2
    #Logic for min/max/sum/multipy/and/or/xor here...
    return getS2(Seg,ss,mid,qs,qe,2*si+1)+getS2(Seg,mid+1,se,qs,qe,2*si+2)
def construct(arr , n):
    x=math.ceil(math.log(n,2))
    maxi=2*(pow(2,x))-1
    Seg=[0]*(maxi)
    construct2(arr,0,n-1,Seg,0)
    return Seg

def construct2(arr,ss,se,Seg,si):
    if ss==se:
        Seg[si]=arr[ss]
        return arr[ss]
    mid=ss+(se-ss)//2
    Seg[si]=construct2(arr,ss,mid,Seg,si*2+1)+construct2(arr,mid+1,se,Seg,si*2+2)
    return Seg[si]

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def DFSUtil(self,v,visited):
        global count
        global inarr
        global outarr
        visited[v]=True
        count+=1
        inarr.append(count)
        #print(v+1,end=' ')
        for i in self.graph[v]:
            #print(i,"i")
            if visited[i]==False:
                self.DFSUtil(i,visited)
        outarr[v]=count
    def DFS(self,v):
        visited=[False]*len(self.graph)
        self.DFSUtil(v,visited)

n,q1=map(int,input().split(' '))
g = Graph()
inarr=[]
outarr=[0]*n
for i in range(n-1):
    p,q=map(int,input().split(' '))
    g.addEdge(p-1, q-1)
count=0
g.DFS(0)
#print(inarr)
#print(outarr)
arr=list(map(int,input().split(' ')))
#print(arr)
for i in range(n):
    result=0
    temp=int(math.sqrt(arr[i]))
    for j in range(1,temp+1):
        if(arr[i]%j==0):
            if(j==arr[i]//j):
                result+=j%3
            else:
                result+=(j+(arr[i]//j))%3
    if(result%3==0):
        arr[i]=1
    else:
        arr[i]=0
#print(arr)
Seg=construct(arr , n)
#print(Seg)
#print(getS(Seg,n,1,3))
#update(arr,Seg,n,0,2)
#print(arr)
#print(Seg)
while(q1!=0):
    l=list(map(int,input().split(' ')))
    if(l[0]==2):
        print(getS(Seg,n,inarr[l[1]-1]-1,outarr[l[1]-1]-1))#,inarr[l[1]-1]-1,outarr[l[1]-1]-1)
    else:
        result=0
        temp=int(math.sqrt(l[2]))
        for j in range(1,temp+1):
            if(arr[i]%j==0):
                if(j==arr[i]//j):
                    result+=j%3
                else:
                    result+=(j+(arr[i]//j))%3
        if(result%3==0):
            #arr[l[1]-1]=1
            update(arr,Seg,n,l[1]-1,1)
        else:
            #arr[l[1]-1]=0
            update(arr,Seg,n,l[1]-1,0)
        #print(Seg)
        #print(arr)
    q1-=1
'''
9 5
1 2
1 6
2 3
2 4
2 5
6 7
6 8
7 9
5 5
1 2
1 3
3 4
3 5
16 8 17 3 18
2 1
2 3
1 3 7
2 1
2 3
'''
