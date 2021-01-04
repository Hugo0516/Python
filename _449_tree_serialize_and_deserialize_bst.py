# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """
        Encodes a tree to a single string.
        """

        def postorder(root):
            return postorder(root.left) + postorder(root.right) + [root.val] if root else []

        return ' '.join(map(str, postorder(root)))

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        """

        def helper(lower=float('-inf'), upper=float('inf')):
            if not data or data[-1] < lower or data[-1] > upper:
                return None

            val = data.pop()
            root = TreeNode(val)
            root.right = helper(val, upper)
            root.left = helper(lower, val)
            return root

        data = [int(x) for x in data.split(' ') if x]
        return helper()


class Codec2:
    def postorder(self, root):
        return self.postorder(root.left) + self.postorder(root.right) + [root.val] if root else []

    def int_to_str(self, x):
        """
        Encodes integer to bytes string.
        """
        bytes = [chr(x >> (i * 8) & 0xff) for i in range(4)]
        bytes.reverse()
        bytes_str = ''.join(bytes)
        return bytes_str

    def serialize(self, root):
        """
        Encodes a tree to a single string.
        """
        lst = self.postorder(root)
        lst = [self.int_to_str(x) for x in lst]
        return 'ç'.join(map(str, lst))

    def str_to_int(self, bytes_str):
        """
        Decodes bytes string to integer.
        """
        result = 0
        for ch in bytes_str:
            result = result * 256 + ord(ch)
        return result

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        """

        def helper(lower=float('-inf'), upper=float('inf')):
            if not data or data[-1] < lower or data[-1] > upper:
                return None

            val = data.pop()
            root = TreeNode(val)
            root.right = helper(val, upper)
            root.left = helper(lower, val)
            return root

        data = [self.str_to_int(x) for x in data.split('ç') if x]
        return helper()
    # Your Codec object will be instantiated and called as such:


class Codec3:
    def postorder(self, root):
        return self.postorder(root.left) + self.postorder(root.right) + [root.val] if root else []

    def int_to_str(self, x):
        """
        Encodes integer to bytes string
        """
        bytes = [chr(x >> (i * 8) & 0xff) for i in range(4)]
        bytes.reverse()
        bytes_str = ''.join(bytes)
        return bytes_str

    def serialize(self, root):
        """
        Encodes a tree to a single string.
        """
        lst = [self.int_to_str(x) for x in self.postorder(root)]
        return ''.join(map(str, lst))

    def str_to_int(self, bytes_str):
        """
        Decodes bytes string to integer.
        """
        result = 0
        for ch in bytes_str:
            result = result * 256 + ord(ch)
        return result

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        """

        def helper(lower=float('-inf'), upper=float('inf')):
            if not data or data[-1] < lower or data[-1] > upper:
                return None

            val = data.pop()
            root = TreeNode(val)
            root.right = helper(val, upper)
            root.left = helper(lower, val)
            return root

        n = len(data)
        # split data string into chunks of 4 bytes
        # and convert each chunk to int
        data = [self.str_to_int(data[4 * i: 4 * i + 4]) for i in range(n // 4)]
        return helper()
    # Your Codec object will be instantiated and called as such:


# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

"""
*** 和 297 互相參照 ***
*** 這一題用 297 的 code 一樣也會過 ***
Approach 1: Postorder traversal to optimise space for the tree structure.

Time Complexity: O(N)
Space Complexity: O(N)

Approach 2: Convert int to 4-bytes string to optimise space for node values.

Time Complexity: O(N)
Space Complexity: O(N)

Approach 3: Get rid of delimiters.

Time Complexity: O(N)
Space Complexity: O(N)

"""

if __name__ == '__main__':
    pass
