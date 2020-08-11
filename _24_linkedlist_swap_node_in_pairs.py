# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        p = head
        new_start = p.next

        while True:
            q = p.next
            temp = q.next

            q.next = p

            if not temp or not temp.next:
                p.next = temp
                break
            p.next = temp.next
            p = temp

        return new_start

"""
    有點難想
    https://www.youtube.com/watch?v=2VVLxAQd5uQ
"""

if __name__ == '__main__':
    demo = Solution()
    node = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    # node4 = ListNode(4)
    node.next = node2
    node2.next = node3
    # node3.next = node4

    output_1 = demo.swapPairs(node)
    while output_1:
        print(output_1.val, end=' ')
        output_1 = output_1.next
