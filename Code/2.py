def good_triplets(arr, n):
    dict1 = {}  # to keep count of each element
    nums = []   # to keep unique entries of each element
    for i in range(0, n):
        if dict1.get(int(arr[i])) is None:
            dict1[int(arr[i])] = 1
            nums.append(int(arr[i]))
        else:
            dict1[int(arr[i])] = dict1[int(arr[i])] + 1
    count = 0   #count of good triplets
    n = len(nums)

    # for every entry occuring atleast once in the given array (unique entry) [6,4,3]
    for i in range(0, n):
        for j in range(i + 1, n):
            sum = nums[i] + nums[j]
            for k in range(j + 1, n):
                sum += nums[k]
                c = 0
                if sum % nums[i] == 0:
                    c += 1
                if sum % nums[j] == 0:
                    c += 1
                if sum % nums[k] == 0:
                    c += 1
                if c == 1:
                    count += dict1[nums[i]] * dict1[nums[j]] * dict1[nums[k]]  #total count depends on how many times i,j,k appears in the actual array

    # for every entry occuring more than once in the given array (duplicate entries) eg.[6]
    for i in range(0, n):
        if dict1[nums[i]] < 2: # not to be executed for unique entries as they are already taken care of
            continue
        for j in range(0, n):
            if i == j:
                continue
            sum = nums[i] * 2 + nums[j] # i will be the duplicate element and j will be our third element in the triplet
            if sum % nums[i] != 0 and sum % nums[j] ==0:  # if the sum is divisible only by the third element (j)
                count += ((dict1[nums[i]] * (dict1[nums[i]] - 1)) / 2) * dict1[nums[j]]
    return count*6

n = int(input())
arr = []
for i in range(n):
    x = input()
    arr.append(x)

good_triplet_count = good_triplets(arr, n)
print(good_triplet_count)
