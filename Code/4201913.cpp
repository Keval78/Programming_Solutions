s=input()
m=0
count=0
for i in range(0,len(s)):
    if i>0:
        if s[i]!=s[i-1]:
            count=count+1
            #print("count is",count)
        else:
            #print("count is",count)
            count=1
    else:
        count=1
        m=1
    if count>m:
        m=count
    #print("m is",m)
print(m)
