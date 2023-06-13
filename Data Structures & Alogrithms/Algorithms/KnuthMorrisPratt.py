import sys

def knuth_morris_pratt(pattern: str, text: str) -> bool:
    """
    The Knuth-Morris-Pratt Algorithm for finding a pattern within a piece of text
    with complexity O(n + m)

    1) Preprocess pattern to identify any suffixes that are identical to prefixes

        This tells us where to continue from if we get a mismatch between a character
        in our pattern and the text.

    2) Step through the text one character at a time and compare it to a character in
        the pattern updating our location within the pattern if necessary
    """
    # 1) Construct the LPS array
    lps = get_lps_array(pattern)
    p_len = len(pattern)
    t_len = len(text)

    # 2) Step through text searching for pattern
    i, j = 0, 0  # index into text, pattern
    while i < t_len:
        if pattern[j] == text[i]:
            if j == (p_len - 1):
                return True
                # return i-p_len+1
            j += 1

        # if this is a prefix in our pattern
        # just go back far enough to continue
        elif j > 0:
            j = lps[j - 1]
            continue
        i += 1
    return False
    # return -1
    
def get_lps_array(pattern: str) -> list[int]:
    """
    Longest Prefix Suffix Array
    Calculates the new index we should go to if we fail a comparison
    """
    lps, prevLps, i = [0], 0, 1
    while i < len(pattern):
        if pattern[prevLps] == pattern[i]:
            prevLps += 1
        elif prevLps > 0:
            prevLps = lps[prevLps-1]
            continue
        i += 1
        lps.append(prevLps)
    return lps

def test_kmp() -> None:
    """
    Test for KMP Algo
    """
    # Test 1)
    pattern = "abc1abc12"
    text1 = "alskfjaldsabc1abc1abc12k23adsfabcabc"
    text2 = "alskfjaldsk23adsfabcabc"
    assert knuth_morris_pratt(pattern, text1) and not knuth_morris_pratt(pattern, text2)

    # Test 2)
    pattern = "ABABX"
    text = "ABABZABABYABABX"
    assert knuth_morris_pratt(pattern, text)

    # Test 3)
    pattern = "AAAB"
    text = "ABAAAAAB"
    assert knuth_morris_pratt(pattern, text)

    # Test 4)
    pattern = "abcdabcy"
    text = "abcxabcdabxabcdabcdabcy"
    assert knuth_morris_pratt(pattern, text)

    # Test 5)
    pattern = "aabaabaaa"
    assert get_lps_array(pattern) == [0, 1, 0, 1, 2, 3, 4, 5, 2]


if __name__ == "__main__":
    print("Testing...   KMP Algo")
    test_kmp()



# * PROBLEM DESCERIPTION
# link :- https://github.com/TheAlgorithms/Python/blob/master/strings/knuth_morris_pratt.py

