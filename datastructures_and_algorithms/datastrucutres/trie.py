"""
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/

Reference:
https://github.com/TheAlgorithms/Python/blob/master/data_structures/trie/trie.py
https://gist.github.com/jtribble/e5bcfc16b82a2547c22fc39877e81217
"""

"""
A Trie/Prefix Tree is a kind of search tree used to provide quick lookup
of words/patterns in a set of words. A basic Trie however has O(n^2) space complexity
making it impractical in practice. It however provides O(max(search_string, length of
longest word)) lookup time making it an optimal approach when space is not an issue.
"""

# import sys




from dataclasses import dataclass, field
from typing import List, Optional
from collections import defaultdict  # , OrderedDict
@dataclass
class TrieNode:
    """Dataclass represing node of the trie.
    """
    is_leaf: bool = False
    children: 'TrieNode' = field(default_factory=lambda: defaultdict(TrieNode))

# Create node
# node = Node(val, None, None)


class Trie:
    """Trie/PrefixTree data structure.
    """

    def __init__(self) -> None:
        self.root: Optional['TrieNode'] = TrieNode()

    def insert(self, word: str) -> None:
        """Inserts a word into the Trie
        :param word: word to be inserted
        :return: None
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_leaf = True

    def insert_many(self, words: List[str]) -> None:
        """Inserts a list of words into the Trie
        :param words: list of string words
        :return: None
        """
        for word in words:
            self.insert(word)

    def find(self, word: str) -> bool:
        """Tries to find word in a Trie
        :param word: word to look for
        :return: Returns True if word is found, False otherwise
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_leaf

    def delete(self, word: str) -> None:
        """Deletes a word in a Trie
        :param word: word to delete
        :return: None
        """

        def _delete(curr: TrieNode, word: str, index: int) -> bool:
            if index == len(word):
                # If word does not exist
                if not curr.is_leaf:
                    return False
                curr.is_leaf = False
                return len(curr.children) == 0
            char = word[index]
            char_node = curr.children.get(char)
            # If char not in current trie node
            if not char_node:
                return False
            # Flag to check if node can be deleted
            delete_curr = _delete(char_node, word, index + 1)
            if delete_curr:
                del curr.children[char]
                return len(curr.children) == 0
            return delete_curr

        _delete(self.root, word, 0)

    def print_words(self, node: TrieNode, word: str = "") -> None:
        """Prints all the words in a Trie
        :param node: root node of Trie
        :param word: Word variable should be empty at start
        :return: None
        """
        if node.is_leaf:
            print(word, end=" ")

        for key, value in node.children.items():
            self.print_words(value, word + key)

    def __str__(self) -> str:
        """Overwrite string function
        """
        self.print_words(self.root)
        print()
        return ''


def test_trie() -> bool:
    """test Trie
    """
    words = "banana bananas bandana band apple all beast".split()
    trie = Trie()
    trie.insert_many(words)
    trie.print_words(trie.root, "")
    print()
    print([trie.find(word) for word in words])
    trie.delete("all")
    trie.print_words(trie.root)
    print()
    trie.delete("banana")
    trie.print_words(trie.root)
    print()


if __name__ == "__main__":
    test_trie()
