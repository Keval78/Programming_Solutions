t = int(input())
while t > 0:
    n, x = map(int,input().split())
    # print(n,x)
    arr = list(map(int,input().split()))
    arr_dic = {}
    for i in range(0,n):
        if arr[i] in arr_dic:
            arr_dic[arr[i]] += 1
        else:
            arr_dic[arr[i]] = 1
        if x != 0:
            if arr[i]^x in arr_dic:
                arr_dic[arr[i]^x] += 1
            else:
                arr_dic[arr[i]^x] = 1
    max_value = 0
    max_key = 0
    for key, value in arr_dic.items():
        if value > max_value:
            max_value = value
            max_key = key
    # print(max_key, max_value)
    
    step_count = 0
    for i in range(0,n):
        if(arr[i]^x == max_key):
            step_count += 1
        
    print(max_value, min(step_count,(n-step_count)))
    t-=1