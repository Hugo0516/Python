# Definition for singly-linked list.
import heapq
from typing import List
from queue import PriorityQueue


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # brute force
    def mergeKLists1(self, lists):
        self.nodes = []

        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next

    # priority queue method (min-heap)
    def mergeKLists2(self, lists):
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next


# Merge with Divide And Conquer
class Solution2(object):

    # line 50 => mergesort algorithm !!!!!!
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next


"""
    我個人覺得難在：要想到min heap => 在python 要實現 min heap 就會想到 heapq => 接著要在想到 enumerate 性質
    
    method 1, brute force
    Time complexity : O(NlogN) where N is the total number of nodes.
    Collecting all the values costs O(N) time.
    A stable sorting algorithm costs O(NlogN) time.
    Iterating for creating the linked list costs O(N) time.
    
    Space complexity : O(N).
    Sorting cost O(N) space (depends on the algorithm you choose).
    Creating a new linked list costs O(N) space.
    
    method2:
    Time complexity : O(NKlogk) where k is the number of linked lists.
    => 有 K 個 linkedlist, 每個 linkedlist 有 N 個元素, 每一次 priority queue(min-heap) 始終只會保存 k 個元素,
       即 每一個 linkedlist 同時貢獻一個     
    
    The comparison cost will be reduced to O(logk) for every pop and insertion to priority queue. 
    But finding the node with the smallest value just costs O(1) time.
    There are N nodes in the final linked list.
    
    Space complexity :
    O(n) Creating a new linked list costs O(n) space.
    
    O(k) The code above present applies in-place method which cost O(1) space. 
    And the priority queue (often implemented with heaps) costs O(k) space (it's far less than N in most situations). 
    
    class 2:
    Time complexity : O(NKlogk) where k is the number of linked lists.

    We can merge two sorted linked list in O(n) time where n is the total number of nodes in two lists.
    Sum up the merge process and we can get: O(∑ i=1 ~ log 2, k) = O(Nlogk)
    
    Space complexity : O(1)
    
    We can merge two sorted linked lists in O(1) space.
    
    https://www.youtube.com/watch?v=XqA8bBoEdIY
"""

if __name__ == '__main__':
    demo = Solution()
    input1 = ListNode(1)
    input1_2 = ListNode(4)
    input1_3 = ListNode(5)
    input1.next = input1_2
    input1_2.next = input1_3

    input2 = ListNode(1)
    input2_2 = ListNode(3)
    input2_3 = ListNode(4)
    input2.next = input2_2
    input2_2.next = input2_3

    input3 = ListNode(2)
    input3_2 = ListNode(6)
    input3.next = input3_2

    list_1 = [input1, input2, input3]
    list_2 = [input1, input2, input3]
    # output = demo.mergeKLists(list_1)
    output2 = demo.mergeKLists2(list_2)

    # while output:
    #     print(output.val, end=' ')
    #     output = output.next
    #
    # print('\n')

    while output2:
        print(output2.val, end=' ')
        output2 = output2.next
