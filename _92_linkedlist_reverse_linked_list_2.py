# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        count = 1
        root = ListNode(0)
        root.next = head
        pre = root
        while pre.next and count < m:
            pre = pre.next
            count += 1
        if count < m:
            return head
        mNode = pre.next
        curr = mNode.next
        while curr and count < n:
            next = curr.next
            curr.next = pre.next
            pre.next = curr
            mNode.next = next
            curr = next
            count += 1
        return root.next

"""
    t.ly/RyuI
"""

if __name__ == '__main__':
    demo = Solution()
    root = ListNode(1)
    root_2 = ListNode(2)
    root_3 = ListNode(3)
    root_4 = ListNode(4)
    root_5 = ListNode(5)
    root.next = root_2
    root_2.next = root_3
    root_3.next = root_4
    root_4.next = root_5

    output = demo.reverseBetween(root, 2, 4)

    while output:
        print(output.val, end=' ')
        output = output.next
