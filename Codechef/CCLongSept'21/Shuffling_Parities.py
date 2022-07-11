t = int(input())
while t > 0:
    n = int(input())
    half_n = (n//2) if (n%2==0) else (n//2+1)
    arr = list(map(int,input().split()))
    even_count = 0
    for i in range(0,n):
        if(arr[i]%2 == 0):
            even_count+=1
    
    odd_count = n-even_count
    even_count_ones = half_n if (even_count > half_n) else even_count
    odd_count_ones = (n-half_n) if (odd_count > (n-half_n)) else odd_count
    # print(even_count_ones, odd_count_ones)
    print(even_count_ones + odd_count_ones)
    t-=1