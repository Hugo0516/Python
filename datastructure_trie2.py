class Node:
    def __init__(self, children, isWord):
        self.children = children
        self.isWord = isWord


class Solution:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Node({}, False)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.trie
        for char in word:
            if not char in current.children:
                current.children[char] = Node({}, False)
            current = current.children[char]
        current.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        output = self._findWordsFromNode(word)
        return output is not None and output.isWord is True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        output = self._findWordsFromNode(prefix)
        return output is not None

    def autocomplete(self, prefix):
        current = self.trie
        for char in prefix:
            if not char in current.children:
                return []
            current = current.children[char]
        return self.completeWord(current, prefix)

    def completeWord(self, node, prefix):
        words = []
        if node.isWord:
            words.append(prefix)        # append = +=
        for char in node.children:
            words += self.completeWord(node.children[char], prefix + char)
        return words

    def _findWordsFromNode(self, prefix):
        curr = self.trie
        for char in prefix:
            if not char in curr.children:
                return None
            curr = curr.children[char]
        return curr


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

"""
    這裡實作了 trie 會用到的 methods, 可以參考 208 和 techlead，
    這是綜合那兩個，然後我自己所寫出來的版本
"""

if __name__ == '__main__':
    trie = Solution()
    trie.insert("apple")
    print(trie.search("apple"))  # returns true
    print(trie.search("app"))  # returns false
    print(trie.startsWith("app"))  # returns true
    trie.insert("app")
    print(trie.search("app"))  # returns true

    print('\n')
    print(trie.autocomplete("ap"))  # return ['app', 'apple']
