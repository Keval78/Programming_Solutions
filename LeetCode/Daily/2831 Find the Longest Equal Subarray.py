
def longestEqualSubarray(nums, k):
    n = len(nums)

    ranges = [[] for i in range(n+1)]

    prev = nums[0]
    last = 0
    for i in range(n):
        if nums[i] != prev:
            ranges[prev].append((last, i-1))
            last = i
        prev = nums[i]
    if n > 1:
        ranges[nums[-1]].append((last, n-1))
    print(ranges)

    ans = 0
    for rang in ranges:
        if len(rang) == 0:
            continue
        if len(rang) == 1:
            ans = max(ans, rang[0][1] - rang[0][0] + 1)
        else:
            # Sliding Window with counting k elements.
            kk = k
            nn = len(rang)
            i, j = 0, 1
            curr_max = 0
            while i < nn and j < nn:
                diff = rang[j][0] - rang[i][0] - 1
                print(diff, kk)
                if diff < kk:
                    kk -= diff
                    curr_max += rang[j][1] - rang[j][0] + 1
                    j += 1
                else:
                    curr_max -= rang[i][1] - rang[i][0] + 1
                    kk += (rang[i+1][0]-rang[i][0]-1)
                    i += 1
                if kk >= 0:
                    ans = max(ans, curr_max)

        print("ans", ans)
    return ans


nums = [1, 3, 2, 3, 1, 3]
print(longestEqualSubarray(nums, 3))

nums = [1, 1, 2, 2, 1, 1, 2, 1, 1, 1, 1]
print(longestEqualSubarray(nums, 2))
