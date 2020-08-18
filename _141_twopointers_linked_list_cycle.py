# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> ListNode:
        fast, slow = head, head

        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                return True

        return False


"""
    Can you solve it using O(1) (i.e. constant) memory?
    => 就是這句,讓這一整題變難

    use fast, flow pointer to solve
    這裡慢指針動一步, 快指針動兩步,
    那假如快指針我這裡變成動三步呢？ => 這樣的話有可能兩個 pointer 永遠都不會相遇！！！！！！！！！！！
    3-1 = 2 有可能永遠都遇不到
    fast 動4 步還有可能遇到彼此
    所以要注意陷阱！！！！！！
    
    
    Time Complexity: O(n)
    時間複雜度照理來說為那個圈圈的node個數-1 + 尚未進入圈圈的前面那一小段
    所以假如前面那一小段為長度為1, 那後面那個圈圈就為長度為n
    => O(1) + O(n-1) =O(n)
    
    所以說假如輸入的head總共有n個nodes, 然後圈圈特別大,前面那小段只有1個node, => 那Time Complexity 當然趨近O(n)
    
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
    print(demo.hasCycle(root))
