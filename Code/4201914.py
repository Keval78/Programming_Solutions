s=input()
count=0
i=0
#print(s)
for i in range(0,len(s)):
    if s[i]=='6':
        continue
    else:
        count=count+1
if i==(len(s)-1):
    if s[i]=='6':
        print(s[i])
        count=-1
print(count)
