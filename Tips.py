import collections

tips = "This document is for noting some methods I used to forget"

'''
Sliding window algorithms can be implemented with a single pointer and a variable for window size.
Typically we use all of the elements within the window for the problem (for eg - sum of all elements in the window).

Two pointer technique is quite similar
but we usually compare the value at the two pointers instead of all the elements between the pointers.

Two pointers can also have variations like fast-slow pointer.
'''

'''
    在 138, 我們可以看到, 當我們想要在 class 用變數時, 儘量自己創一個  __init__ 來存放他
    在 23, 我們可以看到另外一個在 class 用變數時之方法, self.xxx => 然後不放置在 __init__ 裡面, 根本沒創建 __init__

'''

'''
    abc = collections.deque() => abc = []
'''

'''
    在 class 裡面 想要用變數的話不一定要宣告在 __init__(self,)裡面
    你也可以直接宣告 self.xxx 來用
    reference 124
'''

"""
    在 tree 的題型裡面 可以思考用 recursion 的方式解題, 以recursion 的邏輯下去做思考
"""
'''
    deque 用法, q = deque([]) => 裡面一定要放 []
'''

'''
    for i in string.ascii.lowercase: a......z
'''

test_1 = collections.defaultdict(list)
print(test_1)
abc = [2] + [3]
print(abc)

defg = [[2] + [3] + [4]]
print(defg)

layer = {}
layer["hot"] = [["hot", "fuck", "not"]]
newWord = "dot"
word = "hot"
abcd = [j + [newWord] for j in layer[word]]
print(abcd)

"""
    235 T.C 再確認/
    207
    
"""

"""
    Array and Strings:
    
    Linked List:
    
    Tree and Graphs:
                    DFS:
                    All possible solution / search on graph(treat tree,matrix as a graph) / 
                    If tree is too depth then DFS would not be a good choice
                    cycle detection 
                    U need some logic requiring backtracking
                    Stack have an chance to explode !
                    Question like forecasting something from source to destination
                    想要窮盡所有路徑 => search for entire tree
                    Depth First Search is commonly used when you need to search the entire tree. 
                    It's easier to implement (using recursion) than BFS, and requires less state: 
                    While BFS requires you store the entire 'frontier', 
                    DFS only requires you store the list of parent nodes of the current element.
                    
                    DFS, 無相圖找連通分量, 和 695. Max area of Island, 200. Number of Island!!!, 547. Friend Cycle

                    BFS: => 對二維數組找最優解 Time Complexity 最好
                    Shortest path on simple graph 
                    If tree is too width, then BFS is not a good choice, because we need to store all the nodes to be discovered next
                    只想找到一個最短路徑
                    Queue don't have a chance to explode.
                    Like FB => you want to establish friends circle !
                    Breadth First Search is generally the best approach when the depth of the tree can vary, 
                    and you only need to search part of the tree for a solution. 
                    For example, finding the shortest path from a starting value to a final value is a good place to use BFS.

                    https://stackoverflow.com/questions/3332947/when-is-it-practical-to-use-depth-first-search-dfs-vs-breadth-first-search-bf
                    
                    Topological Sort, 如果看到題目是要判斷DAG時, 請立馬想到 topological sort,
                    Topological Sort, 皆可以用DFS or BFS 來實現
                    helper()
                    
"""