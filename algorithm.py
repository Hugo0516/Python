dp = [[0 for i in range(10)] for j in range(5)]
print(dp)

"""
algorithm tutorial:

Sorting and Searching:

Graph Algorithms:

Greedy Algorithms:

Dynamic Programming: 
<1. Overlapping sub-problem / 2. Optimal solutions>

Step 1: 定義數組元素的含義
Step 2: 找出數組元素之間的關係式, Ex: dp[n] = dp[n-1] + dp[n-2]
Step 3: 找出初始值

The table could be one-dimensional or two-dimensional
EX: dp = [[0 for i in range(10)] for j in range(5)] => actually we will initialize the form to 0 or -1
由於數組都是從 0 開始, 但現實中不能有dp[0][?], dp[?][0]這種東西, 所以初始化數組時, 通常都會增大一個空間
=> dp[? + 1][? + 1]

Brute-force
Top-down => memoization => actually need recursion
Bottom-up => tabularization => actually iteration => 用這個 !!! => easier
Advanced => use bottom-up solution with space optimization => Space 通常可以減少 O(n) => O(1)

題型: 
    總和題： dp[n] = dp[n-1] + dp[n-2]
    (走階梯的所有方式, 最後一步為一步 or 兩步)
    
    0/1背包, 返回最佳解題: dp[i][j] = max(dp[i-1][j] + dp[current], dp[i-1][j])
    
Fibonacci / Staircase / 0,1 Knapsack / Partition /  
"""