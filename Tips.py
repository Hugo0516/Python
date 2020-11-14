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