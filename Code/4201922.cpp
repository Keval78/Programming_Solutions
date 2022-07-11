n=int(input())
arr=[]
arr.append(0)
arr.append(0)
arr.append(1)
i=0
if i>=4:
    for i in range(3,n):
        s=0
        #print("i is",i)
        if i%2!=0:
            for j in range(2,i,2):
                #print(j)
                #print(i)
                #print("j and j+1",j,j+1)
                s=s+((j)*(j+1)//2)
                #print("s is",s)
        else:
            for j in range(1,i,2):
                #print(j)
                #print(i)
                #print("j and j+1",j,j+1)
                s=s+((j)*(j+1)//2)
                #print("s is",s)
        s=s+arr[i-1]
        i=i+1
        arr.append(s)
else:
    i=n
print(arr[i-1])
