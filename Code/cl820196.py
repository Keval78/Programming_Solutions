modul=(10**9)+7
div2=500000004
mul=[]
for i in range(100005):
    mul.append(1)if i ==0 else mul.append((mul[i-1]*10)%modul)
test=int(input())
while(test):
    nl,lst=map(str,input().split())
    nr,rst=map(str,input().split())
    nl=int(nl)
    nr=int(nr)
    temp=""
    lst=lst[::-1]
    rst=rst[::-1]
    i=0
    while lst[i]=='0':
        temp+='9'
        i+=1
    if lst[i]!='1':
        temp+=str(int(lst[i])-1)
    else:
        temp+="0"
    lst=temp+lst[i+1:]
    #print(lst)
    total=0
    l=[]
    for i in range(len(lst)):
        total=(total+(mul[i]*int(lst[i])))%modul
        l.append(total)
    #print(l)
    number=(int(lst[0])*mul[0])%modul
    total1=(number*(number+1)*div2)%modul
    t=0
    for i in range(len(lst)):
        if(lst[i]=='0' or i==0):
            continue
        number=(int(lst[i])*mul[i])%modul
        number1=(int(lst[i])*mul[i-1])%modul
        t=(number*(number+1)*div2)%modul-(number1*(number1-1)*div2)%modul
        temp=(int(lst[i])*mul[i]*l[i-1])%modul
        if(lst[i]==lst[i-1]):
            if i!=1:
                total1=(t+temp+(total1-(int(lst[i])*mul[i-1]*(int(l[i-2])+1))))%modul
            else:
                total1=(t+temp+(total1-(int(lst[i])*mul[i-1])))%modul
        elif(lst[i]>lst[i-1]):
            total1+=t+temp
            total1%=modul
        else:
            total1=(t+temp+(total1-(int(lst[i])*mul[i-1]*mul[i-1])))%modul
    #print(total1)
    total=0
    r=[]
    #print(lst,rst)
    for i in range(nr):
        total=(total+(mul[i]*int(rst[i])))%modul
        r.append(total)
    #print(l,r)
    number=(int(rst[0])*mul[0])%modul
    total2=(number*(number+1)*div2)%modul
    #print(rst,r)
    for i in range(len(rst)):
        if(rst[i]=='0' or i==0):
            continue
        number=(int(rst[i])*mul[i])%modul
        number1=(int(rst[i])*mul[i-1])%modul
        t=(number*(number+1)*div2)%modul-(number1*(number1-1)*div2)%modul
        #print(i,number1,number,t,temp)
        temp=(int(rst[i])*mul[i]*r[i-1])%modul
        #print(temp,rst[i],rst[i-1],total2)
        if(rst[i]==rst[i-1]):
            if i!=1:
                #print("aaaaaaaa")
                total2=(t+temp+(total2-(int(rst[i])*mul[i-1]*(int(r[i-2])+1))))%modul
            else:
                #print("bbbbbbbb")
                total2=(t+temp+(total2-(int(rst[i])*mul[i-1])))%modul
                #print(rst[i],mul[i-1])
        elif(rst[i]>rst[i-1]):
            #print("cccccccc")
            total2+=t+temp
            total2%=modul
        else:
            #print("ddddddd")
            total2=(t+temp+(total2-(int(rst[i])*mul[i-1]*mul[i-1])))%modul
        #print(total2)
    #print(total2)
    Ans=(total2-total1)%modul
    print(Ans)
    test-=1
