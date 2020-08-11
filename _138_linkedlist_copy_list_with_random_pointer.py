# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        self.visitedDict = {}
        # key is the old node, value is new node

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        if head in self.visitedDict:
            new_node = self.visitedDict[head]
            return new_node
        else:
            new_node = Node(head.val, None, None)
            self.visitedDict[head] = new_node

            new_node.next = self.copyRandomList(head.next)
            new_node.random = self.copyRandomList(head.random)
        return new_node

    def copyRandomList2(self, head: 'Node') -> 'Node':
        def copyNode(curr: Node) -> Node:
            if not curr:
                return None

            if curr in self.visitedDict:
                return self.visitedDict[curr]
            else:
                new_curr = None(curr.val, None, None)
                self.visitedDict[curr] = new_curr
                return self.visitedDict[curr]

        curr = head
        new_head = copyNode(curr)
        new_curr = new_head

        while curr:
            new_curr.next = copyNode(curr.next)
            new_curr.random = copyNode(curr.random)

            new_curr = new_curr.next
            curr = curr.next
        return new_curr


# class Solution:
#     def copyRandomList(self, head: 'Node') -> 'Node':
#         nodeDict = dict()
#         dummy = Node(0, None, None)
#         nodeDict[head] = dummy
#         newHead, pointer = dummy, head
#         while pointer:
#             node = Node(pointer.val, pointer.next, None)
#             nodeDict[pointer] = node
#             newHead.next = node
#             newHead, pointer = newHead.next, pointer.next
#         pointer = head
#         while pointer:
#             if pointer.random:
#                 nodeDict[pointer].random = nodeDict[pointer.random]
#             pointer = pointer.next
#         return dummy.next

"""
    key store old data, value store new data
    
    Both method1 and method2:
    Time Complexity: O(n) / Space Complexity: O(n)
    
    method1: recursion 
    method2: iteration
    therefore: method2 在跑測資比較快
    https://www.youtube.com/watch?v=RK5KaR_gbg8
"""

if __name__ == '__main__':
    demo = Solution()
    root = Node(7)
    root_2 = Node(13)
    root_3 = Node(11)
    root_4 = Node(10)
    root_5 = Node(1)

    root.next = root_2
    root.random = None
    root_2.next = root_3
    root_2.random = root
    root_3.next = root_4
    root_3.random = root_5
    root_4.next = root_5
    root_4.random = root_3
    root_5.next = None
    root_5.random = root

    output = demo.copyRandomList(root)
    while output:
        print(output.val, output.random.val, end=' ')
        output = output.next
