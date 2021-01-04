# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def str2tree(self, s: str) -> TreeNode:
        ix = s.find('(')    # 如果沒有找到的話, 會回傳 -1
        if ix < 0:
            return TreeNode(int(s)) if s else None

        balance = 0
        for jx, u in enumerate(s):
            if u == '(':
                balance += 1
            if u == ')':
                balance -= 1
            if jx > ix and balance == 0:
                break

        root = TreeNode(int(s[:ix]))
        root.left = self.str2tree(s[ix + 1:jx])
        root.right = self.str2tree(s[jx + 2:-1])
        return root


class Solution2:
    def str2tree(self, s: str) -> TreeNode:
        if not s or len(s) == 0:
            return None
        root, _ = self.helper(s, 0)
        return root

    def helper(self, s, i):
        start = i
        while i < len(s) and (s[i] == '-' or s[i].isdigit()):  # negative sign or digit
            i += 1
        node = TreeNode(int(s[start: i]))
        if i < len(s) and s[i] == '(':
            i += 1  # skip '('
            node.left, i = self.helper(s, i)
            i += 1  # skip ')'
        if i < len(s) and s[i] == '(':  # still has '(', create right tree
            i += 1  # skip '('
            node.right, i = self.helper(s, i)
            i += 1  # skip ')'
        return node, i


"""
Reference: https://leetcode.com/problems/construct-binary-tree-from-string/discuss/100422/Python-Straightforward-with-Explanation

Approach 1: Intuitive Recursion

Time Complexity: O(n^2)
Space Complexity: O(n^2), slice and stack => n*n = n^2

Approach 2: Recursion, with variables

Time Complexity: O(n)
Space Complexity:

"""

if __name__ == '__main__':
    demo = Solution()
    demo2 = Solution2()

    s1 = "4(2(3)(1))(6(5))"
    s2 = "4(2(3)(1))(6(5)(7))"
    s3 = "4(2(3)(1))(6(5)(7))"

    res1 = demo.str2tree(s1)
    res2 = demo.str2tree(s2)
    res3 = demo2.str2tree(s3)


    def level_order(node: TreeNode) -> TreeNode:
        queue = collections.deque([])
        queue.append(node)
        res = []
        while queue:
            tmp = queue.popleft()
            res.append(tmp.val)

            if tmp.left:
                queue.append(tmp.left)
            if tmp.right:
                queue.append(tmp.right)
        return res


    print(level_order(res1))
    print(level_order(res2))
    print(level_order(res3))
