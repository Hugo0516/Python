# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None

        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        while start.next:
            end = start
            for i in range(k - 1):
                end = end.next
                if end.next == None:
                    return dummy.next

            res = self.reverse(start.next, end.next)
            start.next = res[0]
            start = res[1]
        return dummy.next

    def reverse(self, start, end):
        a = start.val
        b = end.val
        newhead = ListNode(0);
        newhead.next = start
        while newhead.next != end:
            tmp = start.next
            start.next = tmp.next
            tmp.next = newhead.next
            newhead.next = tmp
        return [end, start]

"""
    尚未看過 先抄= =
    https://reurl.cc/V6yojA
    
    跟 24 比對 = =
"""

if __name__ == '__main__':
    demo = Solution()
    node = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(4)
    node_5 = ListNode(5)
    node.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5

    output = demo.reverseKGroup(node, 2)

    while output:
        print(output.val, end=' ')
        output = output.next
