def binary_search(n, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        mid_val = arr[mid]
        # print(mid_val)
        if mid_val == x:
            return True
        elif mid_val > x:
            return binary_search(n, low, mid - 1, x)
        else:
            return binary_search(n, mid + 1, high, x)
    else:
        return False