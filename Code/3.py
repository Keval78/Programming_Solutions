from collections import defaultdict
t=int(input())
while(t):
    n=int(input())
    arr=list(map(int,input().split()))
    #print(arr)
    xor=[]
    x=0
    xor.append(0)
    for i in range(n):
        x^=arr[i]
        xor.append(x)
    #print(xor)
    dic=defaultdict(list)
    for i in range(n+1):
        dic[xor[i]].append(i)
    #print(dic)
    count=0
    for k,l in dic.items():
        #print(k,l)
        length=len(l)
        count+=0-(length)*(length-1)//2
        #print(count)
        for i in range(length,0,-1):
            if i-1>=0:
                count+=(i-1)*l[i-1]
                #print(count,"After Plus")
                count-=(i-1)*l[length-i]
                #print(count,"After minus")
    print(count)
    t=t-1
