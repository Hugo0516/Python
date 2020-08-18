# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if not fast or not fast.next:
            return None
        while head != slow:
            slow = slow.next
            head = head.next
        return head


"""
    use fast, flow pointer to solve
    
    負雪的代碼最後寫錯惹 # 18
    https://blog.csdn.net/fuxuemingzhu/article/details/79530638
    
    觀念：
    https://www.youtube.com/watch?v=UkKBPGt5Nok&t=175s
    https://www.youtube.com/watch?v=9SD2ccDW5CY
"""

if __name__ == '__main__':
    demo = Solution()
    root = ListNode(3)
    node_2 = ListNode(2)
    node_3 = ListNode(0)
    node_4 = ListNode(-4)
    root.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_2
    print(demo.detectCycle(root))
