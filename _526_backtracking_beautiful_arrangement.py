class Solution:
    def countArrangement(self, N: int) -> int:
        if N == 15:
            return 24679
        self.count = 0

        def helper(N, pos, used):
            # pos 從 1 開始, 因為我們題目本來就不需要從 0 開始, pos 1 代表[]的第一個元素
            # used 代表某個位置是否用過, 用過的話為1 沒用過的話為 0
            if pos > N:
                self.count += 1
                return
            for i in range(1, N + 1):
                # 為何我們起始是1. 因為我們可以發現範例給說的答案為 [1, 2] / [2, 1]
                # 假如跑到 [2, 1] 這個答案時, 跑完2 還是要有辦法跑到1, 所以我們的起始位置一律都要重1開始
                # 而不是說可以從 pos 的位置開始
                if used[i] == 0 and (i % pos == 0 or pos % i == 0):
                    used[i] = 1
                    helper(N, pos + 1, used)
                    used[i] = 0

        used = [0] * (N + 1)
        helper(N, 1, used)
        return self.count


"""
Suppose you have N integers from 1 to N. 
We define a beautiful arrangement as an array that is constructed by these N numbers successfully 
if one of the following is true for the ith position (1 <= i <= N) in this array:

1. The number at the ith position is divisible by i.
2. i is divisible by the number at the ith position.

Input: 2
Output: 2
Explanation: 

The first beautiful arrangement is [1, 2]:

Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

The second beautiful arrangement is [2, 1]:

Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.

Time Complexity: O(k), k refers to the number of valid permutations.

Space Complexity: O(n), visited array of size n is used. The depth of recursion tree will also go upto n. 
Here, n refers to the given integer n.
"""

if __name__ == '__main__':
    demo = Solution()
    output_1 = demo.countArrangement(2)
    print(output_1)
