# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """

        def rserialize(root, string):
            """ a recursive helper function for the serialize() function."""
            # check base case
            if root is None:
                string += 'None,'
            else:
                string += str(root.val) + ','  # ',' 改成 '#' 或其他東西都可以, 這是我們自定的!!!
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)
            return string

        return rserialize(root, '')

    def serialize2(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def dfs(root):
            if not root:
                res.append("None,")
                return
            res.append(str(root.val) + ",")
            dfs(root.left)
            dfs(root.right)

        res = []
        dfs(root)
        return "".join(res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """

        def rdeserialize(l):
            """ a recursive helper function for deserialization."""
            if l[0] == 'None':
                l.pop(0)
                return None

            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)     # 你可能會想說, 疑括號內變數一樣是 'l' 嗎？
            root.right = rdeserialize(l)    # 是的, 因為傳送的 l 是 list, 所以在別層迴圈進行pop(),效果或一直都在
            return root

        data_list = data.split(',')     # 做完 split 之後會變成 list !!!
        root = rdeserialize(data_list)
        return root


class Codec2:
    '''       O(n) time and O(n) space, BFS traversal
    e.g., 1
         / \
        2   5
       / \
      3   4  , level order traversal, serialize will be '1,2,5,3,4,None,None,None,None,None,None,'; deserialize
      with queue as well, convert back. Time and Space O(n).
    '''

    def serialize(self, root):
        if not root:
            return ''
        queue = collections.deque()
        queue.append(root)
        res = ''
        while queue:
            node = queue.popleft()
            if not node:
                res += 'None,'
                continue
            res += str(node.val) + ','
            queue.append(node.left)
            queue.append(node.right)
        return res

    def deserialize(self, data):
        if not data:
            return None
        ls = data.split(',')
        root = TreeNode(int(ls[0]))
        queue = collections.deque()
        queue.append(root)
        i = 1
        while queue and i < len(ls):
            node = queue.popleft()
            if ls[i] != 'None':
                left = TreeNode(int(ls[i]))
                node.left = left
                queue.append(left)
            i += 1
            if ls[i] != 'None':
                right = TreeNode(int(ls[i]))
                node.right = right
                queue.append(right)
            i += 1
        return root


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

"""
*** 和 449 互相參照 ***

To serialize a binary tree means to: 

1. Encode tree structure.

2. Encode node values.

3. Choose delimiters to separate the values in the encoded string.

Approach 1: Depth First Search (DFS), preorder
=> 思路：一開始看到這要直覺想到, DFS & BFS, 然後, 後來選擇 DFS, 是因為 DFS deserialize 比較好寫

用 serialize 的 Time Complexity:in both serialization and deserialization functions, we visit each node exactly once, 
thus the time complexity is O(N), where N is the number of nodes, i.e. the size of tree.
=> !!! 我覺得實際上是 O(N^2), 畢竟他用 String + ',', 可是 String 是 immutable, 所以每一次都要 copy

用 serialize2 的 Time Complexity: O(N), 最後再用 join 才會總共只需要 O(N) 

Space Complexity:  in both serialization and deserialization functions, we keep the entire tree, 
either at the beginning or at the end, therefore, the space complexity is O(N).

Approach 2: BFS version

Time Complexity:
Space Complexity:
"""

if __name__ == '__main__':
    demo = Codec()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    ans = demo.serialize(root)
    print(ans)
    res = demo.deserialize(ans)
