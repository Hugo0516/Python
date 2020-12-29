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


class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr is not None:
            next_tmp = curr.next
            curr.next = prev
            prev = curr
            curr = next_tmp

        return prev


class Solution3:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        first, second = head, head.next
        p = self.reverseList(second)

        second.next = first
        first.next = None

        return p


"""
    I finished this by myself.
    Input: 1->2->3->4->5->NULL
    Output: 5->4->3->2->1->NULL
    
    Approach 1, 2:
    Iterative:
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Approach 3:
    Recursive: 
    Time Complexity: O(n)
    Space Complexity: O(n)
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

    demo3 = Solution3()
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)

    output_2 = demo3.reverseList(node)
