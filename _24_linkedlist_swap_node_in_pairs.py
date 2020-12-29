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


class Solution2(object):

    def swapPairs(self, head: ListNode) -> ListNode:
        # If the list has no node or has only one node left.
        if not head or not head.next:
            return head

        # Nodes to be swapped
        first_node = head
        second_node = head.next

        # Swapping
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node

        # Now the head is the second node
        return second_node

    def swapPairs2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        second = head.next
        returned = self.swapPairs(second.next)

        second.next = head
        head.next = returned
        return second


class Solution3:

    def swapPairs(self, head: ListNode) -> ListNode:
        # Dummy node acts as the prevNode for the head node
        # of the list and hence stores pointer to the head node.
        dummy = ListNode(-1)
        dummy.next = head

        prev_node = dummy

        while head and head.next:
            # Nodes to be swapped
            first_node = head;
            second_node = head.next;

            # Swapping
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # Reinitializing the head and prev_node for next swap
            prev_node = first_node
            head = first_node.next

        # Return the new head node.
        return dummy.next


"""
    有點難想
    https://www.youtube.com/watch?v=2VVLxAQd5uQ

We define the function to implement as swap(head), where the input parameter head refers to the head of a linked list. 
The function should return the head of the new linked list that has any adjacent nodes swapped.

1. First, we swap the first two nodes in the list, i.e. head and head.next;
2. Then, we call the function self as swap(head.next.next) to swap the rest of the list following the first two nodes.
3. Finally, we attach the returned head of the sub-list in step (2) with the two nodes swapped in step (1) to form a 
new linked list.

<Leetcode Below> 2020/ 12/ 27 update
Approach 2: Recursive
Time Complexity: O(N), where N is the size of linked list.
Space Complexity: O(N), stack space utilized for recursion.

=> Approach 2 的第二個 比較好一點點...

Approach 3: Iterative    
Time Complexity: O(N)
Space Complexity: O(1)

"""

if __name__ == '__main__':
    demo = Solution()
    demo2 = Solution2()
    demo3 = Solution3()

    # node = ListNode(1)
    # node.next = ListNode(2)
    # node.next.next = ListNode(3)
    # node.next.next.next = ListNode(4)
    # opt = demo.swapPairs(node)

    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    opt2 = demo2.swapPairs(node)

    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    opt3 = demo3.swapPairs(node)
