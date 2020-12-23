from collections import OrderedDict

from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        """
        :type capacity: int
        """
        self.myCache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        """
        :type key: int
        :rtype: int
        """
        if key not in self.myCache:
            return - 1

        self.myCache.move_to_end(key)
        return self.myCache[key]

    def put(self, key: int, value: int) -> None:
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.myCache:
            self.myCache.move_to_end(key)
        self.myCache[key] = value
        if len(self.myCache) > self.capacity:
            self.myCache.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class DLinkedNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


class LRUCache2():
    def _add_node(self, node):
        """
        Always add the new node right after head.
        """
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """
        Remove an existing node from the linked list.
        """
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        """
        Move certain node in between to the head.
        """
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """
        Pop the current tail.
        """
        res = self.tail.prev
        self._remove_node(res)
        return res

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.cache.get(key, None)
        if not node:
            return -1

        # move the accessed node to the head;
        self._move_to_head(node)

        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = self.cache.get(key)

        if not node:
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value

            self.cache[key] = newNode
            self._add_node(newNode)

            self.size += 1

            if self.size > self.capacity:
                # pop the tail
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            # update the value.
            node.value = value
            self._move_to_head(node)


"""
Approach 1: Ordered dictionary:
 
Time Complexity: O(1),  both for put and get since all operations with ordered dictionary :
get/in/set/move_to_end/popitem (get/containsKey/put/remove) are done in a constant time.

Space Complexity: O(capacity), since the space is used only for an ordered dictionary with at most 
capacity + 1 elements. 

There is a structure called ordered dictionary, it combines behind both hashmap and linked list. 
In Python this structure is called OrderedDict and in Java LinkedHashMap.

Approach 2: Hashmap + DoubleLinkedList

Time Complexity: O(1), both for put and get

Space Complexity: O(capacity), since the space is used only for a hashmap and 
double linked list with at most capacity+1 element 


*** 這一題兩種解答都要會 !!! ***
因為面試時, 不知道能不能用 collections 的 ordereddict, 所以面試的時候要問面試官
我看 leetcode 評論說, 你知道這 library, 代表你很熟 python, 但是你同樣也會另外一種不用 library 的方式
這樣會代表你觀念很好

"""

if __name__ == '__main__':
    demo = LRUCache(2)
    print(demo.put(1, 1))
    print(demo.put(2, 2))
    print(demo.get(1))
    print(demo.put(3, 3))
    print(demo.get(2))
    print(demo.put(4, 4))
    print(demo.get(1))
    print(demo.get(3))
    print(demo.get(4))

    demo2 = LRUCache2(2)
    print(demo2.put(1, 1))
    print(demo2.put(2, 2))
    print(demo2.get(1))
    print(demo2.put(3, 3))
    print(demo2.get(2))
    print(demo2.put(4, 4))
    print(demo2.get(1))
    print(demo2.get(3))
    print(demo2.get(4))
