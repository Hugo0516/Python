# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        tmp = ListNode()
        res = tmp

        while l1 or l2:
            if l1 and l2:
                if l1.val <= l2.val:
                    tmp.next = l1
                    tmp = tmp.next
                    l1 = l1.next
                elif l1.val > l2.val:
                    tmp.next = l2
                    tmp = tmp.next
                    l2 = l2.next
            else:
                if l1:
                    tmp.next = l1
                    tmp = tmp.next
                    l1 = l1.next
                elif l2:
                    tmp.next = l2
                    tmp = tmp.next
                    l2 = l2.next

        return res.next

    # leetcode official solution
    # Time Complexity: O(n+m)
    # Space Complexity: O(1),
    # The iterative approach only allocates a few pointers, so it has a constant overall memory footprint.
    def mergeTwoLists2(self, l1, l2):
        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # exactly one of l1 and l2 can be non-null at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next

    # Recursive method
    # Time Complexity: O(n+m)
    # Space Complexity: O(n+m)
    # The first call to mergeTwoLists does not return until the ends of both l1 and l2 have been reached,
    # so n+m stack frames consume O(n+m) space.
    def mergeTwoLists3(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


"""
    I finished method 1 by myself
    
    Look method2, method3
"""

if __name__ == '__main__':
    demo = Solution()
    node1 = ListNode(1)
    node1_2 = ListNode(2)
    node1_3 = ListNode(4)
    node1.next = node1_2
    node1_2.next = node1_3

    node2 = ListNode(1)
    node2_2 = ListNode(3)
    node2_3 = ListNode(4)
    node2.next = node2_2
    node2_2.next = node2_3

    output = demo.mergeTwoLists(node1, node2)

    while output:
        print(output.val, end=' ')
        output = output.next
