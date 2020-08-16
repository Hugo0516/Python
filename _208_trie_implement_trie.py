class Trie:
    class TrieNode(object):
        def __init__(self):
            self.is_word = False
            self.children = [None] * 26  # 創建太多空對象 浪費資源

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie.TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        p = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not p.children[index]:
                p.children[index] = Trie.TrieNode()
            p = p.children[index]
        p.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.find(word)
        return node is not None and node.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.find(prefix) is not None

    def find(self, prefix):
        p = self.root
        for c in prefix:
            index = ord(c) - ord('a')  # 轉型浪費資源
            if not p.children[index]: return None
            p = p.children[index]
        return p


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


class Trie2(object):
    def __init__(self):
        self.root = {}

    def insert(self, word):
        p = self.root
        for c in word:
            if c not in p:
                p[c] = {}
            p = p[c]
        p['#'] = True

    def search(self, word):
        node = self.find(word)
        return node is not None and '#' in node

    def startsWith(self, prefix):
        return self.find(prefix) is not None

    def find(self, prefix):
        p = self.root
        for c in prefix:
            if c not in p:
                return None

            p = p[c]
        return p


"""
    At most 26 children per node ([a-z] only)
    Time Complexity : O(l) (l 即為 Letter 個數)
    Space Complexity : O(prefix) or O(n*l^2)(worst case, 每個字母都不重複)
    
    Method 1: 注意我們用到 inner class 的概念！！
    Method 2: 比 Method 1 快, 用到 Dictionary 概念 比較好, 詳見 datastructure_trie2
    
   http://zxi.mytechroad.com/blog/data-structure/leetcode-208-implement-trie-prefix-tree/ 
"""
