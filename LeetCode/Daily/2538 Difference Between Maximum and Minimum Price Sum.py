"""
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""
from collections import defaultdict
from typing import List


class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        '''Solution:
        1. Root should be current node.
        2. Minimum sum will be only current node = root node.
        3. Maximum sum will be max path sum to all leaf node from root node.
        '''
        return 0

    def maxOutput2(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        '''Solution 2: In-Out DP
        1. Cosider any node as root node. count the total cost or edges which needs to reverse for the root node.
        2. Total cost = Number of edges needs to reverse for root.
        3. For child node Cost = Cost(child_subtree) + Cost(parent_subtree_without_current_child) + cost_of_edge
        '''
        # Define Reverse enumerate:
        def reversed_enumerate(l: list):
            for i in range(len(l)-1, -1, -1):
                yield i, l[i]

        # graph with the forward edges which incurred cost 0.
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        max_in = [0]*n
        max_out = [0]*n

        def dfs_maxpath_subtree(node, parent, max_in):
            for adj in graph[node]:
                if adj == parent:
                    continue
                dfs_maxpath_subtree(adj, node, max_in)
                max_in[node] = max(max_in[node], max_in[adj])
            max_in[node] += price[node]

        dfs_maxpath_subtree(0, -1, max_in)

        def dfs_maxpath_parent(node, parent, max_out):

            prefix_max = [0]*(len(graph[node]) + 1)
            suffix_max = [0]*(len(graph[node]) + 1)
            for i, sibling in enumerate(graph[node]):
                if sibling == parent:
                    prefix_max[i+1] = prefix_max[i]
                else:
                    prefix_max[i+1] = max(prefix_max[i], max_in[sibling])

            for i, sibling in reversed_enumerate(graph[node]):
                if sibling == parent:
                    suffix_max[i] = suffix_max[i+1]
                else:
                    suffix_max[i] = max(suffix_max[i+1], max_in[sibling])

            for i, adj in enumerate(graph[node]):
                if adj == parent:
                    continue

                # path towards all siblings. and Path towards grandparent
                max_out[adj] += max(prefix_max[i],
                                    suffix_max[i+1], max_out[node])
                # add cost for parent
                max_out[adj] += price[node]
                # print(adj, max_out)

                # * # Optimizing below O(N) loop into O(1).
                # * # Use Prefix_max & Suffix_max or Use Heap
                # for sibling in graph[node]:
                #     max_out[adj] = price[node] + max([max_out[node]] + [max_in[s] for s in graph[node] if s != adj and s != parent])

                dfs_maxpath_parent(adj, node, max_out)
            max_out[node] += price[node]

        dfs_maxpath_parent(0, -1, max_out)

        print(max_in)
        print(max_out)

        # Maximum path to any leaf node.
        max_paths = [max(i, j) for i, j in zip(max_in, max_out)]

        # Difference of max_path and min_path for each node.
        diff = [max_paths[i] - price[i] for i in range(n)]
        print(diff)

        return max(diff)
