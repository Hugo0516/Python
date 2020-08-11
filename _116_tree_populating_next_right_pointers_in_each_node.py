# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        if root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
        self.connect(root.left)  # pre-order!!!
        self.connect(root.right)
        return root

    # 花花版本
    def connect2(self, root: 'Node') -> 'Node':
        if not root or not root.left: return root
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect2(root.left)
        self.connect2(root.right)

        return root


"""
    Follow up:
    You may only use constant extra space.
    Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
    
    思路：
        Tree 90% => recursion
        Inordr / preorder/ postorder (這裡選preorder)
        
        善用Local view !!!!!!!!!! (隨便取一個點觀察他的特性, 然後再套用到宏觀世界)
        => cur.left.next = cur.right
        => cur.right.next = cur.next.left
        
        Time Complexity: O(n)
        Space Complexity: O(log(n))
        
        https://www.youtube.com/watch?v=YNu143ZN4qU

    https://blog.csdn.net/fuxuemingzhu/java/article/details/79559645
"""
