'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
'''
Reference: https://github.com/TheAlgorithms/Python/blob/master/data_structures/binary_tree/basic_binary_tree.py
'''

class Node():
    def __init__(self, data: int):
        self.data: int = data
        self.left: Node = None
        self.right: Node = None

    def __repr__(self) -> str:
        return f"Node({self.data}), Left({self.left}), Right({self.right})"
    

class BinaryTree():
    def __init__(self) -> None:
        self.root = None

    def set_value(self, data: int) -> None:
        if not self.root:
            self.root.data = data

    def get_value(self) -> int:
        if not self.root:
            return self.root.data
        else:
            return None

    