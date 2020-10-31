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


class Solution2:

    def reverseLinkedList(self, head, k):

        # Reverse k nodes of the given linked list.
        # This function assumes that the list contains
        # at least k nodes.
        prev_node, curr_node = None, head
        while k:
            # Keep track of the next node to process in the
            # original list
            next_node = curr_node.next

            # Insert the node pointed to by "ptr"
            # at the beginning of the reversed list
            curr_node.next = prev_node
            prev_node = curr_node

            # Move on to the next node
            curr_node = next_node

            # Decrement the count of nodes to be reversed by 1
            k -= 1

        # Return the head of the reversed list
        return prev_node

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        count = 0
        ptr = head

        # First, see if there are at least k nodes
        # left in the linked list.
        while count < k and ptr:
            ptr = ptr.next
            count += 1

        # If we have k nodes, then we reverse them
        if count == k:
            # Reverse the first k nodes of the list and
            # get the reversed list's head.
            reversedHead = self.reverseLinkedList(head, k)

            # Now recurse on the remaining linked list. Since
            # our recursion returns the head of the overall processed
            # list, we use that and the "original" head of the "k" nodes
            # to re-wire the connections.
            head.next = self.reverseKGroup(ptr, k)
            return reversedHead
        return head


class Solution3:

    def reverseLinkedList(self, head, k):

        # Reverse k nodes of the given linked list.
        # This function assumes that the list contains
        # atleast k nodes.
        new_head, ptr = None, head
        while k:
            # Keep track of the next node to process in the
            # original list
            next_node = ptr.next

            # Insert the node pointed to by "ptr"
            # at the beginning of the reversed list
            ptr.next = new_head
            new_head = ptr

            # Move on to the next node
            ptr = next_node

            # Decrement the count of nodes to be reversed by 1
            k -= 1

        # Return the head of the reversed list
        return new_head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        ptr = head
        ktail = None
        # Head of the final, modified linked list
        new_head = None

        # Keep going until there are nodes in the list
        while ptr:
            count = 0
            # Start counting nodes from the head
            # ptr = head    # 這一句是多餘的, 我不懂為啥有這行x

            # Find the head of the next k nodes
            while count < k and ptr:
                ptr = ptr.next
                count += 1

            # If we counted k nodes, reverse them
            if count == k:
                # Reverse k nodes and get the new head
                revHead = self.reverseLinkedList(head, k)

                # new_head is the head of the final linked list
                if not new_head:
                    new_head = revHead
                # ktail is the tail of the previous block of
                # reversed k nodes
                if ktail:   # 這一行是由先想出 152 後 反推得到
                    ktail.next = revHead

                ktail = head
                head = ptr

        # attach the final, possibly un-reversed portion
        if ktail:
            ktail.next = head

        return new_head if new_head else head


"""
    尚未看過 先抄= =
    https://reurl.cc/V6yojA
    
    跟 24 比對 = =
    
    *** 注意 method 2 也要會, 因為面試時會循序漸進 當你寫出這版本時 才會 move on 到 method 3
    method 2 : recursive method
    
    Time Complexity: O(N) since we process each node exactly twice. 
    Once when we are counting the number of nodes in each recursive call, 
    and then once when we are actually reversing the sub-list. 
    A slightly optimized implementation here could be that 
    we don't count the number of nodes at all and simply reverse k nodes. 
    If at any point we find that we didn't have enough nodes, 
    we can re-reverse the last set of nodes so as to keep the original structure 
    as required by the problem statement. 
    That ways, we can get rid of the extra counting.
    
    Space Complexity: O(N/k) used up by the recursion stack. 
    The number of recursion calls is determined by both k and N. 
    In every recursive call, we process k nodes and then make a recursive call to process the rest. 

    method 3 : iterative method:
    
    Time Complexity: O(N) since we process each node exactly twice. 
    Once when we are counting the number of nodes in each recursive call, 
    and then once when we are actually reversing the sub-list.
    
    Space Complexity: O(1). 
    
    head ~ which will always point to the original head of the next set of k nodes.
    
    revHead ~ which is basically the tail node of the original set of k nodes. 
    Hence, this becomes the new head after reversal.
    
    ktail ~ is the tail node of the previous set of k nodes after reversal.
    
    newHead ~ acts as the head of the final list that we need to return as the output. 
    Basically, this is the k(th) node from the beginning of the original list.
"""

if __name__ == '__main__':
    demo = Solution3()
    node = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(4)
    node_5 = ListNode(5)
    node.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5

    output = demo.reverseKGroup(node, 3)

    while output:
        print(output.val, end=' ')
        output = output.next
