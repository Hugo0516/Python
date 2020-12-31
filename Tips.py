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

"""
strip() 用法,
Python strip() 方法用於移除字符串頭尾指定的字符（默認為空格）或字符序列。

注意：該方法只能刪除開頭或是結尾的字符，不能刪除中間部分的字符。
"""

"""
permutation / next permutation / combination / subset => 為一組題型
"""

"""
map() 函式用法, map()會根據提供的函數對指定序列做映射。第一個參數function 以參數序列中的每一個元素調用function 函數，返回包含每次function 函數返回值的新列表。
=> 常常語 lambda 做搭配
int() 函式用法, int() 函數用於將一個字符串或數字轉換為整型。

.join() 函式用法

reduce()用法
yield 用法

closure 用法

sqrt()用法

functool m用法 , 1240

NP complete

heuristic algorithm

skyline, skyline的意思是 "高", EX: 在x, y座標裡 我可以稱每一的x點座標的高為 skyline

import copy => 為了使用 deepcopy => 256 題 

****** 980: 超好的 backtracking 模板 !!!! 
Whenever we see the context of grid traversal, 
the technique of backtracking or DFS (Depth-First Search) should ring a bell.

As a reminder, backtracking is a general algorithm for finding all (or some) solutions 
to some problems with constraints. It incrementally builds candidates to the solutions, 
and abandons a candidate as soon as it determines that the candidate cannot possibly lead to a solution.

nonlocal 變數

一般回溯問題分三種：

Find a path to success 有沒有解
Find all paths to success 求所有解
求所有解的個數
求所有解的具體信息
3.Find the best path to success 求最優解

37.
from the description of the Sudoku problem, 
one might have noticed the characteristics that hint on the solution of backtracking, 
such as the recursive nature of problem, 
a number of candidate solutions and some rules to filter out the candidates etc.
---------------------

"""

"""
1240, 看不懂 = =
"""

"""
Divide and Conquer:
Let's follow here a solution template for the divide and conquer problems :

Define the base case(s).

Split the problem into subproblems and solve them recursively.

Merge the solutions for the subproblems to obtain the solution for the original problem.

Divide and Conquer 題型要分析時間複雜度, 好像都得用 Master Therom
"""

"""
Greedy: 
Pick the locally optimal move at each step, and that will lead to the globally optimal solution.
"""

"""
DP:
The problem to find sum or maximum or minimum in an entire array or in a fixed-size sliding window
could be solved by the dynamic programming (DP) approach in linear time.

看 221 !!!!!!!

dp 問題, 為什麼我們常常會讓 dp數組的大小 row col 各加1呢？
=> 為了避免 out of range

256, good example !!!
Dynamic programming is iterative, unlike memoization, which is recursive.
Problems that have optimal substructure can be solved with greedy algorithms. 
If they also have overlapping subproblems, then they can be solved with dynamic programming algorithms.

"""

"""
monotonic queue/ deque
題型： 239
"""

"""
priority queue
=> 根據 leetcode 313 的說詞:
Write a program to find the nth super ugly number.
=> 根據 youtube 講解, 說我們電奧 nth 這種關鍵字 要想到 priority queue 即 heap
"""

"""
heapq, heappop, heappush
"""

"""
https://docs.python.org/3/library/functools.html#functools.lru_cache
functool 要看 !!!!!!!
"""

"""
22 題的 backtrack 很特別, 在做完 backtrack 後沒有用 remove function
=> 我發現是因為用了 String !!!!, String 很特別, 跟 list 不一樣, 然後 因為也沒有用 for 都是用 if !!!!
=> 我猜想的啦

17 題也是 看！！！

301 也是 => 共通點 都是因為 String
"""

"""
nonlocal 變數
"""

"""
Leetcode 108:
要注意！！！！ BST 不唯一 !!!!
詳細請看:https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/solution/
然後  inorder traversal 遍歷出來的數字是用 ascending 的 !!!!

Here is the funny thing about BST. Inorder traversal is not a unique identifier of BST. 
At the same time both preorder and postorder traversals are unique identifiers of BST

Here we have an additional condition: the tree should be height-balanced, 
i.e. the depths of the two subtrees of every node never differ by more than 1.

Basically, the height-balanced restriction means that 
at each step one has to pick up the number in the middle as a root. 

That works fine with arrays containing odd number of elements 
but there is no predefined choice for arrays with even number of elements.

It's known that inorder traversal of BST is an array sorted in the ascending order.


"""

"""
a / 2.0 => float
a / 2 ==> int
"""

"""
set 性質 , 可以用到 union , 參見 1249

"""

"""
棘手系列問題： parantheses 問題 , stock 問題, palindrome 問題, word break, 
"""

"""
itertool.xxx => 241
"""

"""
zip 用法, 122
orderdict 用法 146
"""

"""
use slow/fast pointer to find a mid point
"""

"""
python 去亂數方法 => from random import choice
                    choice(list_1) =>  從 list_1 取隨機數
"""

"""
any()用法 767
"""

"""
['a', 'b', 'c'], 注意, 要把這種包著 string 的 list, 轉成純string 要用 join!!
=> "".join(list)
"""

"""
2D traversal, 要想到 DFS, BFS
The choice of strategy depends on the nature of the problem. 
Though sometimes, they are both applicable for the same problem. 

In addition to 2D grids, these two algorithms are often applied to problems 
associated with tree or graph data structures as well.


"""

"""
isdigit() 用法, 224, isdigit 只能用在 string 
"""

"""
sliding window, 和 itertools.groupby 是一樣的東西？
leetcode 723
"""

"""
772 要再看過 ！！！！！！！！！！

"""

"""
in-place algorithm

Does in-place mean constant space complexity?

No. By definition, an in-place algorithm is an algorithm which transforms input using no auxiliary data structure.

The tricky part is that space is used by many actors, not only by data structures. 
The classical example is to use recursive function without any auxiliary data structures.

Is it in-place? Yes.

Is it constant space? No, because of recursion stack.
"""

"""
Catalan number !!!!!
要知道那是啥, 可以應用在很多題目上面
請直接看 wiki
Catalan number 的 時間複雜度 也要記！！！
Reference: 95 96 !!!
"""

"""
top-down 
bottom-up
比較題目！！！

=> 104, 250, 509
"""