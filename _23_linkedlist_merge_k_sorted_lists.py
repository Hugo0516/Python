# Definition for singly-linked list.
import heapq
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode(-1)
        move = head
        while True:
            curHead = ListNode(float('inf'))
            curIndex = -1
            for i, llist in enumerate(lists):
                if llist and llist.val < curHead.val:
                    curHead = llist
                    curIndex = i
            if curHead.val == float('inf'):
                break
            curNext = curHead.next
            move.next = curHead
            curHead.next = None
            move = curHead
            curHead = curNext
            lists[curIndex] = curHead
        return head.next

    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode(-1)
        move = dummy
        heap = []
        heapq.heapify(heap)
        [heapq.heappush(heap, (l.val, i)) for i, l in enumerate(lists) if l]

        while heap:
            curVal, curIndex = heapq.heappop(heap)
            curHead = lists[curIndex]
            curNext = curHead.next
            move.next = curHead
            curHead.next = None
            move = move.next
            curHead = curNext
            if curHead:
                lists[curIndex] = curHead
                heapq.heappush(heap, (curHead.val, curIndex))
        return dummy.next


"""
    我個人覺得難在：要想到min heap => 在python 要實現 min heap 就會想到 heapq => 接著要在想到 enumerate 性質
    Time Complexity: method1: O(n*k), method2: O(n) (faster than 5%, faster than 98%)
    N是結果鍊錶的長度，K是每次題目給出的鍊錶個數
    Space Complexity: both O(1)
    https://blog.csdn.net/fuxuemingzhu/article/details/83068632
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
