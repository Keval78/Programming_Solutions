import sys

def z_algorithm(pattern: str, text: str) -> int:
    """
    Example of using z-function for pattern occurrence
    Given function returns the number of times 'pattern'
    appears in 'input_str' as a substring

    >>> find_pattern("abr", "abracadabra")
    2
    >>> find_pattern("a", "aaaa")
    4
    >>> find_pattern("xz", "zxxzxxz")
    2
    """
    cnt = 0
    z_result = z_function(pattern + text)
    for val in z_result:
        if val >= len(pattern):
            cnt += 1
    return cnt


def z_function(input_str: str) -> list[int]:
    """
    For the given string this function computes value for each index,
    which represents the maximal length substring starting from the index and is the same as the prefix of the same size

    e.x.  for string 'abab' for index = 2 z-value would be 2
    For the value of the first element the algorithm always returns 0

    >>> z_function("abracadabra")
    [0, 0, 0, 1, 0, 1, 0, 4, 0, 0, 1]
    >>> z_function("aaaa")
    [0, 3, 2, 1]
    >>> z_function("zxxzxxz")
    [0, 0, 0, 4, 0, 0, 1]
    """
    
    n = len(input_str)
    z_result = [0]*n
    l, r = 0, 0
    for i in range(1, n):
        # case when current index is inside the interval
        if i <= r:
            z_result[i] = min(r - i + 1, z_result[i - l])

        while i + z_result[i] < n and input_str[z_result[i]] == input_str[i + z_result[i]]:
            z_result[i] += 1

        if i + z_result[i] - 1 > r:
            l, r = i, i + z_result[i] - 1

    return z_result


if __name__ == "__main__":
    print("Testing...   Z Algo")

# * PROBLEM DESCERIPTION
# link :- https://github.com/TheAlgorithms/Python/blob/master/strings/z_function.py