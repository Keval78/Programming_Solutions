# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def ii(): return int(input())
def si(): return input()
def mi(ss=" "): return map(int, input().strip().split(ss))
def msi(ss=" "): return map(str, input().strip().split(ss))
def li(ss=" "): return list(mi(ss))


arr = li()
n = len(arr)
x, y = mi()

arr.insert(0, 1)
prefix_sum = [0]*(y-x+2)
prefix_xor = [0]*(y-x+2)

for i in range(x, y+1):
    # print(x, y, prefix_sum[i-x], arr[i])
    prefix_sum[i-x+1] = prefix_sum[i-x] + arr[i]
    prefix_xor[i-x+1] = prefix_xor[i-x] ^ arr[i]

# print(prefix_sum)
# print(prefix_xor)

# max_cost = [(0, 0, float('-inf'))]
max_cost = float('-inf')
min_length = float('inf')
x_dash = 0

for i in range(x, y+1):
    for j in range(i, y+1):
        # print(i, j)
        current_sum = prefix_sum[j-x+1] - prefix_sum[i-x]
        current_xor = prefix_xor[j-x+1] ^ prefix_xor[i-x]
        current_cost = current_sum - current_xor
        if max_cost == current_cost:
            if min_length > j-i+1:
                min_length = j - i + 1
                x_dash = i
        if current_cost > max_cost:
            max_cost = current_cost
            min_length = j - i + 1
            x_dash = i
            # max_cost = [(i, j-i+1, current_cost)]

# print(max_cost)
print(x_dash, x_dash+min_length-1)


'''
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
arr = [10, 20, 30, 40, 50]
n = len(arr)
x, y = 1, 5

arr.insert(0, 1)
prefix_sum = [i for i in range(y-x+2)]
prefix_xor = [i for i in range(y-x+2)]

for i in range(x, y+1):
    # print(x, y, prefix_sum[i-x], arr[i])
    prefix_sum[i-x+1] = prefix_sum[i-x] + arr[i]
    prefix_xor[i-x+1] = prefix_xor[i-x] ^ arr[i]

print(prefix_sum)
print(prefix_xor)

max_cost = [(0, 0, float('-inf'))]
for i in range(x, y+1):
    for j in range(i, y+1):
        print(i, j)
        current_sum = prefix_sum[j-x+1] - prefix_sum[i-x]
        current_xor = prefix_xor[j-x+1] ^ prefix_xor[i-x]
        current_cost = current_sum - current_xor
        if max_cost[0][2] == current_cost:
            if max_cost[0][1] > j-i+1:
                max_cost.insert(0, (i, j-i+1, current_cost))
            else:
                max_cost.append((i, j-i+1, current_cost))
        if max_cost[0][2] < current_cost:
            max_cost = [(i, j-i+1, current_cost)]
        print(max_cost)
        

# for i in range(x, y+1):
#     val = (prefix_sum[i]-prefix_sum[x-1]) - (prefix_xor[i]^prefix_xor[x-1])
#     print(prefix_sum[i]-prefix_sum[x-1], prefix_xor[i]^prefix_xor[x-1])
#     print("s", val)
'''
