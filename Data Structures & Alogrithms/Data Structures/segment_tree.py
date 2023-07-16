"""
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/

Reference:
https://github.com/TheAlgorithms/Python/blob/master/data_structures/binary_tree/segment_tree.py
"""


import math


class SegmentTree:
    """SegmentTree:
        - Advance Sata Structure.
        - Range Query Data Structure
    """

    def __init__(self, a):
        self._len = len(a)
        self.seg_tree = [0] * (4 * self._len)
        self.zero_index = True
        self.build(0 if self.zero_index else 1, 0, self._len - 1)

    def left(self, idx):
        """Index for left child of the node."""
        return idx*2+1

    def right(self, idx):
        """Index for left child of the node."""
        return idx*2+2

    def operation(self, left, right):
        """Generalize the operation for the segment tree node."""
        return max(left, right)

    def nooverlap_case(self):
        """Generalize the Return val when range do not match."""
        return -math.inf

    def build(self, idx, l, r):  # noqa: E741
        """Build Segment Tree."""
        if l == r:
            self.seg_tree[idx] = A[l]
            return
        mid = (l + r) // 2
        self.build(self.left(idx), l, mid)
        self.build(self.right(idx), mid + 1, r)

        self.seg_tree[idx] = self.operation(
            self.seg_tree[self.left(idx)],
            self.seg_tree[self.right(idx)]
        )

    def update_recursive(self, idx, l, r, a, b, val):  # noqa: E741
        """update(1, 1, N, a, b, v) for update val v to [a,b]"""
        if r < a or l > b:
            return True

        if l == r:
            self.seg_tree[idx] = val
            return True

        mid = (l + r) // 2
        self.update_recursive(self.left(idx), l, mid, a, b, val)
        self.update_recursive(self.right(idx), mid + 1, r, a, b, val)
        self.seg_tree[idx] = self.operation(
            self.seg_tree[self.left(idx)],
            self.seg_tree[self.right(idx)]
        )
        return True

    def update(self, a, b, val):
        """Update val int Segment Tree"""
        return self.update_recursive(0 if self.zero_index else 1, 0, self._len - 1, a - 1, b - 1, val)

    def query_recursive(self, idx, l, r, a, b):
        """query(1, 1, N, a, b) for query max of [a,b]"""
        # No Overlap: (l, r) not lies inside (a,b)
        if r < a or l > b:
            return self.nooverlap_case()

        # Complete Overlap: (l, r) lies inside (a,b)
        if l >= a and r <= b:
            return self.seg_tree[idx]

        # Partial Overlap traverse both left and right
        mid = (l + r) // 2
        return self.operation(
            self.query_recursive(self.left(idx), l, mid, a, b),
            self.query_recursive(self.right(idx), mid + 1, r, a, b)
        )

    def query(self, a, b):
        """Update val int Segment Tree"""
        return self.query_recursive(0 if self.zero_index else 1, 0, self._len - 1, a - 1, b - 1)

    def show_data(self):
        """Print Segement Tree"""
        show_list = []
        for i in range(1, N + 1):
            show_list += [self.query(i, i)]
        print(show_list)


if __name__ == "__main__":
    A = [1, 2, -4, 7, 3, -5, 6, 11, -20, 9, 14, 15, 5, 2, -8]
    N = len(A)
    segt = SegmentTree(A)
    segt.show_data()
    print(segt.seg_tree)
    print(segt.query(4, 6))
    print(segt.query(7, 11))
    print(segt.query(7, 12))
    segt.update(1, 3, 111)
    segt.show_data()
    print(segt.seg_tree)
    print(segt.query(1, 15))
    segt.update(7, 8, 235)
    print(segt.seg_tree)
    segt.show_data()
