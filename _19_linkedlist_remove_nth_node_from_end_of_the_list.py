# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)     # 善用 dummy head 的方法
        dummy.next = head
        fast, slow = dummy, dummy
        for i in range(n):
            fast = fast.next
        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next

"""
    解題思路：
            Time Complexity: O(n) / Space Complexity: O(1)
            https://www.youtube.com/watch?v=Ny4YACv-skc
            https://www.youtube.com/watch?v=kW7aIXyPbXI
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = ListNode(1)
    tmp = input_1
    for i in range(2, 6):
        node = ListNode(i)
        tmp.next = node
        tmp = tmp.next

    # print(input_1.val, tmp.val, end=' ')
    # print('')
    output_1 = demo.removeNthFromEnd(input_1, 2)

    while True:
        print(output_1.val, end=' ')
        if output_1.next is None:
            break
        else:
            output_1 = output_1.next



