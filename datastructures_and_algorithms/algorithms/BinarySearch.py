def binary_search_find(low, high, arr, x):
    """Recursive Binary_search Search value is available
    """
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] > x:
            return binary_search(low, mid-1, arr, x)
        else:
            return binary_search(mid+1, high, arr, x)
    else:
        return False


def binary_search(low, high, arr, x):
    """Recursive Binary_search Search value is available
    """
    if low < high:
        mid = (low + high) // 2
        if arr[mid] >= x:  # keep equal for left point
            return binary_search(low, mid, arr, x)
        else:
            return binary_search(mid+1, high, arr, x)
    return low


def binary_search_itertive(low, high, arr, val):
    """Itertive Binary_search
    """
    while low < high:
        mid = (low + high)//2
        if arr[mid] <= val:
            low = mid+1
        else:
            high = mid
    return low
