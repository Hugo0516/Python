# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None

        len1, len2 = 0, 0
        moveA, moveB = headA, headB
        while moveA:
            len1 += 1
            moveA = moveA.next
        while moveB:
            len2 += 1
            moveB = moveB.next

        if len1 < len2:
            for _ in range(len2 - len1):
                headB = headB.next
        else:
            for _ in range(len1 - len2):
                headA = headA.next

        while headA and headB and headA != headB:
            headA = headA.next
            headB = headB.next
        return headA


"""
    Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
    Output: Reference of the node with value = 8
    Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
    From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. 
    There are 2 nodes before the intersected node in A; 
    There are 3 nodes before the intersected node in B.
"""
demo = Solution()
node_a = ListNode(4)
node_a_2 = ListNode(1)
node_a_3 = ListNode(8)
node_a_4 = ListNode(4)
node_a_5 = ListNode(5)
node_a.next = node_a_2
node_a_2.next = node_a_3
node_a_3.next = node_a_4
node_a_4.next = node_a_5

node_b = ListNode(5)
node_b_2 = ListNode(6)
node_b_3 = ListNode(1)
node_b.next = node_b_2
node_b_2.next = node_b_3
node_b_3.next = node_a_3

output = demo.getIntersectionNode(node_a, node_b)
print(output, output.val)
