# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head:
            prev = None
            curr = head
            next_node = curr.next
            while next_node:
                curr.next = prev
                prev = curr
                curr = next_node
                next_node = curr.next

            curr.next = prev
            return curr
        else:
            return None

"""
    I finished this by myself.
"""

if __name__ == '__main__':
    demo = Solution()
    root = ListNode(5)
    root_2 = ListNode(4)
    root_3 = ListNode(3)
    root_4 = ListNode(2)
    root_5 = ListNode(1)
    root.next = root_2
    root_2.next = root_3
    root_3.next = root_4
    root_4.next = root_5

    output = demo.reverseList(root)

    while output:
        print(output.val, end=' ')
        output = output.next
