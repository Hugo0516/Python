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

"""
    I finished this by myself
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
