class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countUnivalSubtrees(self, root):
        if root is None:
            return 0

        self.count = 0
        self.is_uni(root)
        return self.count

    def is_uni(self, node):

        # base case - if the node has no children this is a univalue subtree
        if node.left is None and node.right is None:
            # found a univalue subtree - increment
            self.count += 1
            return True

        is_uni = True

        # check if all of the node's children are univalue subtrees and if they have the same value
        # also recursively call is_uni for children
        if node.left is not None:
            is_uni = self.is_uni(node.left) and is_uni and node.left.val == node.val

        if node.right is not None:
            is_uni = self.is_uni(node.right) and is_uni and node.right.val == node.val

        # increment self.res and return whether a univalue tree exists here
        self.count += is_uni
        return is_uni


class Solution2:
    def countUnivalSubtrees(self, root):
        self.count = 0
        self.is_valid_part(root, 0)

        return self.count

    def is_valid_part(self, node, val):

        # considered a valid subtree
        if node is None:
            return True

        # check if node.left and node.right are univalue subtrees of value node.val
        if not all([self.is_valid_part(node.left, node.val),
                    self.is_valid_part(node.right, node.val)]):
            return False

        # if it passed the last step then this a valid subtree - increment
        self.count += 1

        # at this point we know that this node is a univalue subtree of value node.val
        # pass a boolean indicating if this is a valid subtree for the parent node
        return node.val == val


class Solution3:
    def countUnivalSubtrees(self, root):
        self.count = 0
        self.is_valid_part(root)

        return self.count

    def is_valid_part(self, root: TreeNode):
        # base case
        if not root:
            return True

        # step 1, get information from two subtrees
        is_left_uni_subtree = self.is_valid_part(root.left)
        is_right_uni_subtree = self.is_valid_part(root.right)

        if (is_left_uni_subtree and is_right_uni_subtree and
                (root.left is None or root.val == root.left.val) and
                (root.right is None or root.val == root.right.val)):
            self.count += 1
            return True

        return False


"""
    解題思路：
    Given a node in our tree, we know that it is a univalue subtree if it meets one of the following criteria:
    
    1. The node has no children (base case)
    2. All of the node's children are univalue subtrees, and the node and its children all have the same value
    
    Step 1, 從 subtree 裡面拿訊息, 判斷 left subtree, right subtree 是否為 unival subtree
    Step 2, 當前, 判斷當前 subtree是否是 uni-value的, 是的話 total_count + 1
    Step 3, return 當前 subtree 是否為 uni-value 給其父節點
    
    => tricky招數, 要把 null children, 看成是合法 subtree, 不然會遇到 NULL POINTER EXCEPTION !!!
    
    Besides, 叫搞清楚我們的問題！！ (釐清問題)
    => input: root of subtree
    => problem: calculate if current subtree is a universal subtree, increment count if necessary
    => return: return if current subtree is a universal subtree !!!!
    
    Approach 3: => Bottom-up
    其實就是  Approach 2, 只不過我覺得這個比較好 !!!!!!!!
    *** 記住這個 ***
    Reference: https://www.youtube.com/watch?v=gnSuBULGasw
    
    -------------------------------------------------------------------
    
    Approach 1: Depth First Search
    Time Complexity: O(n)
    Space Complexity: O(H),  
    the recursive stack is bound by the longest path from the root to a leaf - 
    in other words the height of the tree. 

    Approach 2: Depth First Search - Pass Parent Values, Bottom-up    
    Time Complexity: O(n)
    Space Complexity: O(H),
    the recursive stack is bound by the longest path from the root to a leaf - 
    in other words the height of the tree. 
"""

if __name__ == '__main__':
    demo = Solution()
    demo2 = Solution2()

    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(5)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(5)

    print(demo.countUnivalSubtrees(root))
    print(demo2.countUnivalSubtrees(root))
