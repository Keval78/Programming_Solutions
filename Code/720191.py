t=int(input())
while(t):
    s=input()
    maxl=0
    count11=0
    count22=0
    #print(count1,count2)
    #print(len(s))
    for i in range(len(s)//2):
        if(s[i]=='('):
            count11=count11+1
    for i in range(len(s)//2,len(s)):
        if(s[i]==')'):
            count22=count22+1
    #print(count11,count22)
    i=len(s)//2
    while(count11!=count22):
        if(count11<count22):
            i=i+1
            if(s[i]=='('):
                count11=count11-1
            else:
                count22=coun22-1
        else:
            i=i-1
            if(s[i]=='('):
                count11=count11-1
            else:
                count22=coun22-1
    print(2*count11)
    t=t-1
