"""
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/

Reference:
https://github.com/TheAlgorithms/Python/blob/master/data_structures/binary_tree/avl_tree.py
https://gist.github.com/jtribble/e5bcfc16b82a2547c22fc39877e81217
"""

@dataclass
class Node:
    """Dataclass represing node of the tree.
    """
    data: int
    left: Optional['Node'] = None
    right: Optional['Node'] = None

# Create node
# node = Node(val, None, None)

class AVLTree:
    """AVLTree data structure.
    """

    def __init__(self) -> None:
        self.root: Optional[Node] = None

    def __str__(self) -> str:
        tree_str = f"{self.root.data}"
        tree_str += '('
        if self.root.left is not None:
            tree_str += str(self.root.left)
        tree_str += ')('
        if self.root.right is not None:
            tree_str += str(self.root.right)
        tree_str += ')'
        return tree_str