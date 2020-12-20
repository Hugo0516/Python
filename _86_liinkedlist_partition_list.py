# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def partition(self, head: ListNode, x: int) -> ListNode:

        # before and after are the two pointers used to create two list
        # before_head and after_head are used to save the heads of the two lists.
        # All of these are initialized with the dummy nodes created.
        # before_head and after_head are dummy head !!
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)

        while head:
            # If the original list node is lesser than the given x,
            # assign it to the before list.
            if head.val < x:
                before.next = head
                before = before.next
            else:
                # If the original list node is greater or equal to the given x,
                # assign it to the after list.
                after.next = head
                after = after.next

            # move ahead in the original list
            head = head.next

        # Last node of "after" list would also be ending node of the reformed list
        after.next = None
        # Once all the nodes are correctly assigned to the two lists,
        # combine them to form a single list which would be returned.
        before.next = after_head.next

        return before_head.next


"""

Time Complexity: O(N), where N is the number of nodes in the original linked list and we iterate the original list.

Space Complexity: O(1), we have not utilized any extra space, 
the point to note is that we are reforming the original list, 
by moving the original nodes, we have not used any extra space as such.

"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = ListNode(1)
    input_1.next = ListNode(4)
    input_1.next.next = ListNode(3)
    input_1.next.next.next = ListNode(2)
    input_1.next.next.next.next = ListNode(5)
    input_1.next.next.next.next.next = ListNode(2)

    ouput_1 = demo.partition(input_1, 3)

    while ouput_1:
        print(ouput_1.val, end='->')
        ouput_1 = ouput_1.next
