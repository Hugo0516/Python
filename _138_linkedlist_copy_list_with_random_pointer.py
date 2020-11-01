# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        self.visitedDict = {}  # <original, new_node>
        # key is the old node, value is new node

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        # If we have already processed the current node, then we simply return the cloned version of it.
        if head in self.visitedDict:
            new_node = self.visitedDict[head]
            return new_node
        else:

            # create a new node
            # with the value same as old node.
            new_node = Node(head.val, None, None)

            # Save this value in the hash map. This is needed since there might be
            # loops during traversal due to randomness of random pointers and this would help us avoid them.
            self.visitedDict[head] = new_node  # <original, new_node>

            # Recursively copy the remaining linked list starting once from the next pointer and then from the random pointer.
            # Thus we have two independent recursive calls.
            # Finally we update the next and random pointers for the new node created.
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
                new_curr = Node(curr.val, None, None)
                self.visitedDict[curr] = new_curr
                return self.visitedDict[curr]

        curr = head
        new_head = copyNode(curr)
        new_curr = new_head  # 54 行這一行用意是因為，底下 while 迴圈 new_curr 會一直 next, 所以保留 new_head 當作可以找到的頭！
        # 53, 54 和 56, 57 等義
        # new_head = Node(curr.val, None, None)
        # self.visitedDict[curr] = ned_head

        while curr:
            new_curr.next = copyNode(curr.next)
            new_curr.random = copyNode(curr.random)

            new_curr = new_curr.next
            curr = curr.next
        return new_head


# Time Complexity: O(n) / Space Complexity: O(1)
class Solution2(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head

        # Creating a new weaved list of original and copied nodes.
        ptr = head
        while ptr:
            # Cloned node
            new_node = Node(ptr.val, None, None)

            # Inserting the cloned node just next to the original node.
            # If A->B->C is the original linked list,
            # Linked list after weaving cloned nodes would be A->A'->B->B'->C->C'
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next

        ptr = head

        # Now link the random pointers of the new nodes created.
        # Iterate the newly created list and use the original nodes random pointers,
        # to assign references to random pointers for cloned nodes.
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        # Unweave the linked list to get back the original linked list and the cloned list.
        # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
        ptr_old_list = head  # A->B->C
        ptr_new_list = head.next  # A'->B'->C'
        head_old = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        return head_old


"""
    key store old data, value store new data
    
    Both method1 and method2:
    Time Complexity: O(n) / Space Complexity: O(n)
    
    method1: recursion 
    method2: iteration
    therefore: method2 在跑測資比較快
    https://www.youtube.com/watch?v=RK5KaR_gbg8
    
    
    2020 / 11 / 1 review:
    這一題 copy question 和 clone 一個 graph 一樣！！！！
    ** 複習～～ shallow copy and deep copy concept !!
    
    why we use hashtable?
    We find that this kind of shallow copy, deep copy question is very good to use <original, new_node> structure
    => just remember it !!
    
    recursive method:
    Time Complexity: O(N) where N is the number of nodes in the linked list.
    
    Space Complexity: O(N). ( 其實是 O(2N) => stack and dictionary)
    If we look closely, 
    we have the recursion stack and we also have the space complexity to keep track of nodes already cloned 
    i.e. using the visited dictionary. But asymptotically, the complexity is O(N). 
    
    https://www.youtube.com/watch?v=oXABtaRa37U 
    
    Solution 2 為 究極方法 很難想 ＝＝
    
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

    output = demo.copyRandomList2(root)
    while output:
        print(output.val, output.random.val if output.random else 0, end=' ')
        output = output.next
