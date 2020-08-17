# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> ListNode:
        fast, slow = head, head

        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                return True

        return False


"""
    use fast, flow pointer to solve
    
    https://www.youtube.com/watch?v=9SD2ccDW5CY
"""

if __name__ == '__main__':
    demo = Solution()
    root = ListNode(3)
    node_2 = ListNode(2)
    node_3 = ListNode(0)
    node_4 = ListNode(-4)
    root.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    print(demo.hasCycle(root))
