# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        current_node = head

        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]


class Solution3:

    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        # Find the end of first half and reverse second half.
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # Check whether or not there's a palindrome.
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # Restore the list and return the result.
        # I think this is unnecessary
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous


"""
Approach 1: Copy into Array List and then Use Two Pointer Technique
Time Complexity: O(n)
Space Complexity: O(n)

*** Follow UP ***
Could you do it in O(n) time and O(1) space? => so I can't not copy each of this !!!

Approach 3: Reverse Second Half In-place

Specifically, the steps we need to do are:

1. Find the end of the first half.
2. Reverse the second half.
3. Determine whether or not there is a palindrome.
4. Restore the list.
5. Return the result.

Time Complexity: O(n)
Space Complexity: O(1)

"""

if __name__ == '__main__':
    demo = Solution()
    demo3 = Solution3()

    root_1 = ListNode(1)
    root_1.next = ListNode(2)

    root_2 = ListNode(1)
    root_2.next = ListNode(2)
    root_2.next.next = ListNode(2)
    root_2.next.next.next = ListNode(1)

    print(demo.isPalindrome(root_1))
    print(demo3.isPalindrome(root_2))
