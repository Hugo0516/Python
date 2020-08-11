# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:  # 243 + 564
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = tail = ListNode(0)  # dummy 就是在head 前放一位數，這樣的話可以避免 head 被我們自己操作到不見之類的
        s = 0
        while l1 or l2 or s:
            # print(l1.val, l2.val)
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            tail.next = ListNode(s % 10)
            tail = tail.next
            s //= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            print(dummy.next.val, dummy.next.next)
        return dummy.next

    # 這是花花醬版本


# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         dummy = cur = ListNode(0)
#         carry = 0
#         while l1 or l2 or carry:
#             if l1:
#                 carry += l1.val
#                 l1 = l1.next
#             if l2:
#                 carry += l2.val
#                 l2 = l2.next
#             cur.next = ListNode(carry % 10)
#             cur = cur.next
#             carry //= 10
#         return dummy.next

# 這是 LeetCode 討論區找的
# https://leetcode.com/problems/add-two-numbers/discuss/1032/Python-concise-solution.

"""
    解題思路：
            Special cases:
            1. Two numbers have different lengths e.g. 123 +456789
            2. Sum has more digits e,g, 11 + 99 = 110
            
            可以用以下模板去做往後任何的大數相加：
            dummy = tail = ListNode(0)(dummy 在此處為 head)
            while l1 or l2 or carry:
                sum = l1?.val + l2?.val + carry
                tail.next = ListNode(sum % 10)
                tail = tail.next
                carry = sum /= 10
                l1, l2 = l1?.next, l2?.next
            return dummy.next
            
            Time Complexity = O(max(n, m))/ Space Complexity O(max(n, m))
            https://www.youtube.com/watch?v=-UBiYuIVErM
            
            Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
            Output: 7 -> 0 -> 8
            Explanation: 342 + 465 = 807.
            
            Dummy Node:
            Dummy node 是鏈表問題中一個重要的技巧，中文翻譯叫「啞節點」或者「假人頭結點」。
            Dummy node 是一個虛擬節點，也可以認為是標竿節點。Dummy node 就是在鏈表表頭 head 前加一個節點指向 head，
            即 dummy -> head。Dummy node 的使用多針對單向鏈表沒有前向指標的問題，保證鏈表的 head 不會在刪除操作中遺失。
            除此之外，還有一種用法比較少見，就是使用 dummy node 來進行head的刪除操作，
            比如 Remove Duplicates From Sorted List II，一般的方法current = current.next 是無法刪除 head 元素的，
            所以這個時候如果有一個dummy node在head的前面。

            所以，當鏈表的 head 有可能變化（被修改或者被刪除）時，使用 dummy node 可以簡化程式碼及很多邊界情況的處理，
            最終返回 dummy.next 即新的鏈表。
"""

if __name__ == '__main__':
    demo = Solution()
    node_1 = ListNode(2)
    node_1_2 = ListNode(4)
    node_1_3 = ListNode(3)
    node_1.next = node_1_2
    node_1_2.next = node_1_3

    node_2 = ListNode(5)
    node_2_2 = ListNode(6)
    node_2_3 = ListNode(4)
    node_2.next = node_2_2
    node_2_2.next = node_2_3

    node_3 = ListNode(0)
    node_4 = ListNode(7)
    node_4_2 = ListNode(9)
    node_4.next = node_4_2

    res = (demo.addTwoNumbers(node_1, node_2))
    print(res.val, res.next.val, res.next.next.val)

    res_2 = (demo.addTwoNumbers(node_3, node_4))
    print(res_2.val, res_2.next.val)

    node_5_2 = ListNode(11)
    node_5 = ListNode(10, node_5_2)

    print(node_5.val, node_5_2.val, node_5.next.val)
