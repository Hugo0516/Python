# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        count = 1
        dummy = ListNode(0)  # 0
        dummy.next = head  # dummy.next = 1
        pre = dummy  # pre = dummy = 0

        while pre.next and count < m:  # pre.next = 1
            pre = pre.next  # pre = pre.next = 1
            count += 1  # count = 2
        if count < m:
            return head

        mNode = pre.next  # mNode = 1
        curr = mNode.next  # curr = 2

        while curr and count < n:  # curr = 2, count = 2, n = 4
            next = curr.next  # next = 3
            curr.next = pre.next  # 2.next = pre.next = 1
            pre.next = curr  # pre.next = 2
            mNode.next = next  # 1.next = 3
            curr = next  # curr = 3
            count += 1  # count = 3

        return dummy.next

    def reverseBetween2(self, head: ListNode, m: int, n: int) -> ListNode:
        if head is None:
            return None

        dummy = ListNode(-1)
        dummy.next = head
        mNode = head
        preM = dummy
        nNode = head

        for i in range(1, m):
            preM = mNode
            mNode = mNode.next

        for i in range(1, n):
            nNode = nNode.next

        while mNode != nNode:
            preM.next = mNode.next
            mNode.next = nNode.next
            nNode.next = mNode
            mNode = preM.next

        return dummy.next


"""
    Reverse a linked list from position m to n. Do it in one-pass.
    Note: 1 ≤ m ≤ n ≤ length of list.
    
    Input: 1->2->3->4->5->NULL, m = 2, n = 4
    Output: 1->4->3->2->5->NULL
    
    method 1:
    t.ly/RyuI
    
    法二屌打！！！
    method2:
    https://www.youtube.com/watch?v=esl_A_pzBcg
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

    output = demo.reverseBetween2(root, 1, 3)

    while output:
        print(output.val, end=' ')
        output = output.next
