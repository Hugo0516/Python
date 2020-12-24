# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        last = None
        while head:
            # keep the next node
            tmp = head.next
            # reverse the link
            head.next = last
            # update the last node and the current node
            last = head
            head = tmp

        return last

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # reverse lists
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)

        head = None
        carry = 0
        while l1 or l2:
            # get the current values
            x1 = l1.val if l1 else 0
            x2 = l2.val if l2 else 0

            # current sum and carry
            val = (carry + x1 + x2) % 10
            carry = (carry + x1 + x2) // 10

            # update the result: add to front
            curr = ListNode(val)
            curr.next = head
            head = curr

            # move to the next elements in the lists
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            curr = ListNode(carry)
            curr.next = head
            head = curr

        return head


class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # find the length of both lists
        n1 = n2 = 0
        curr1, curr2 = l1, l2
        while curr1:
            curr1 = curr1.next
            n1 += 1
        while curr2:
            curr2 = curr2.next
            n2 += 1

        # parse both lists
        # and sum the corresponding positions
        # without taking carry into account
        # 3->3->3 + 7->7 --> 3->10->10 --> 10->10->3
        curr1, curr2 = l1, l2
        head = None
        while n1 > 0 and n2 > 0:
            val = 0
            if n1 >= n2:
                val += curr1.val
                curr1 = curr1.next
                n1 -= 1
            if n1 < n2:
                val += curr2.val
                curr2 = curr2.next
                n2 -= 1

            # update the result: add to front
            curr = ListNode(val)
            curr.next = head
            head = curr

        # take the carry into account
        # to have all elements to be less than 10
        # 10->10->3 --> 0->1->4 --> 4->1->0
        curr1, head = head, None
        carry = 0
        while curr1:
            # current sum and carry
            val = (curr1.val + carry) % 10
            carry = (curr1.val + carry) // 10

            # update the result: add to front
            curr = ListNode(val)
            curr.next = head
            head = curr

            # move to the next elements in the list
            curr1 = curr1.next

        # add the last carry
        if carry:
            curr = ListNode(carry)
            curr.next = head
            head = curr

        return head


"""
Approach 1: Reverse Input + Construct Output by Adding to Front

Time Complexity: O(N1 + N2), where N1+N2 is a number of elements in both lists
Space Complexity: O(1), space complexity without taking the output list into account, 
and O(max(N1, N2)) to store the output list. 

Approach 2: Follow Up: Do not Reverse Input.

Time Complexity: O(N1+N2), where N1 + N2  is a number of elements in both lists.
Space Complexity: O(1), space complexity without taking the output list into account, 
and O(max(N1, N2)) to store the output list. 

"""

if __name__ == '__main__':
    demo = Solution()
    root1 = ListNode(7)
    root1.next = ListNode(2)
    root1.next.next = ListNode(4)
    root1.next.next.next = ListNode(3)

    root2 = ListNode(5)
    root2.next = ListNode(6)
    root2.next.next = ListNode(4)

    output_1 = demo.addTwoNumbers(root1, root2)

    while output_1:
        print(output_1.val, end=' ')
        output_1 = output_1.next

    root1 = ListNode(7)
    root1.next = ListNode(2)
    root1.next.next = ListNode(4)
    root1.next.next.next = ListNode(3)

    root2 = ListNode(5)
    root2.next = ListNode(6)
    root2.next.next = ListNode(4)

    demo2 = Solution2()
    output_2 = demo2.addTwoNumbers(root1, root2)
