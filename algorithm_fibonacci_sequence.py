# 0, 1, 1, 2, 3, 5, 8
# method 1
# Time Complexity: O(n^2), Space ComplexityO(2^n)
def fib_recur(n):
    if n <= 1:
        return n
    return fib_recur(n - 1) + fib_recur(n - 2)


# method 2
# Time Complexity: O(n), Space Complexity: O(1)
def fib_loop_nolist(n):
    if n <= 1:  # 0,1 直接返回
        return n
    a, b = 0, 1
    for i in range(2, n + 1):  # 從2開始
        a, b = b, a + b
    return b
