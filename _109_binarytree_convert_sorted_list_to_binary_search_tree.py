# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def findMiddle(self, head):

        # The pointer used to disconnect the left half from the mid node.
        prevPtr = None
        slowPtr = head
        fastPtr = head

        # Iterate until fastPr doesn't reach the end of the linked list.
        while fastPtr and fastPtr.next:
            prevPtr = slowPtr
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next

        # Handling the case when slowPtr was equal to head.
        if prevPtr:
            prevPtr.next = None

        return slowPtr

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        # If the head doesn't exist, then the linked list is empty
        if not head:
            return None

        # Find the middle element for the list.
        mid = self.findMiddle(head)

        # The mid becomes the root of the BST.
        node = TreeNode(mid.val)

        # Base case when there is just one element in the linked list
        if head == mid:
            return node

        # Recursively form balanced BSTs using the left and right halves of the original list.
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node


class Solution2:

    # Convert the given linked list to an array
    def mapListToValues(self, head):
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        # Form an array out of the given linked list and then
        # use the array to form the BST.
        values = self.mapListToValues(head)

        # l and r represent the start and end of the given array
        def convertListToBST(l, r):

            # Invalid case
            if l > r:
                return None

            # Middle element forms the root.
            mid = (l + r) // 2
            node = TreeNode(values[mid])

            # Base case for when there is only one element left in the array
            if l == r:
                return node
            # 這裡的功能就只是可以加快一點時間, 拿掉也沒有關係

            # Recursively form BST on the two halves
            node.left = convertListToBST(l, mid - 1)
            node.right = convertListToBST(mid + 1, r)
            return node

        return convertListToBST(0, len(values) - 1)


class Solution3:

    def findSize(self, head):
        ptr = head
        c = 0
        while ptr:
            ptr = ptr.next
            c += 1
        return c

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        # Get the size of the linked list first
        size = self.findSize(head)

        # Recursively form a BST out of linked list from l --> r
        def convert(l, r):
            nonlocal head

            # Invalid case
            if l > r:
                return None

            mid = (l + r) // 2

            # First step of simulated inorder traversal. Recursively form
            # the left half
            left = convert(l, mid - 1)

            # Once left half is traversed, process the current node
            node = TreeNode(head.val)
            node.left = left

            # Maintain the invariance mentioned in the algorithm
            head = head.next

            # Recurse on the right hand side and form BST out of them
            node.right = convert(mid + 1, r)
            return node

        return convert(0, size - 1)


"""
Approach 1: two pointer with recursion
Time Complexity: O(NlogN)
Space Complexity: O(logN)

Approach 2: conversion to array with recursion
Time Complexity: O(N)
Space Complexity: O(N)

Approach 3: inorder simulation
=> The inorder traversal on a binary search tree leads to a very interesting outcome.
*** Elements processed in the inorder fashion on a binary search tree turn out to be sorted in ascending order. ***
The reason we are able to use this idea in this problem is because we are given a sorted linked list initially !!!

=> We know that the leftmost element in the inorder traversal has to be the head of our given linked list. 
Similarly, the next element in the inorder traversal will be the second element in the linked list and so on. 
This is made possible because the initial list given to us is sorted in ascending order.

<第三個 我看不懂 = =>

Time Complexity: O(N)
Space Complexity: O(logN)

"""

if __name__ == '__main__':
    demo = Solution()
    demo2 = Solution2()
    demo3 = Solution3()

    root = ListNode(-10)
    root.next = ListNode(-1)
    root.next.next = ListNode(5)
    root.next.next.next = ListNode(64)
    root.next.next.next.next = ListNode(77)
    root.next.next.next.next.next = ListNode(100)

    # output_1 = demo.sortedListToBST(root)
    # output_2 = demo2.sortedListToBST(root)
    output_3 = demo3.sortedListToBST(root)

    stack = []
    while stack or output_3:
        if output_3:
            stack.append(output_3)
            output_3 = output_3.left
        else:
            output_3 = stack.pop()
            print(output_3.val, ' ')
            output_3 = output_3.right
