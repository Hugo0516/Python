class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorials, nums = [1], ['1']
        for i in range(1, n):
            # generate factorial system bases 0!, 1!, ..., (n - 1)!
            factorials.append(factorials[i - 1] * i)
            # generate nums 1, 2, ..., n
            nums.append(str(i + 1))

        # fit k in the interval 0 ... (n! - 1)
        k -= 1

        # compute factorial representation of k
        output = []
        for i in range(n - 1, -1, -1):
            idx = k // factorials[i]
            k -= idx * factorials[i]

            output.append(nums[idx])
            del nums[idx]

        return ''.join(output)


"""
Time Complexity: O(N^2), because to delete elements from the list in a loop one has to perform N+(N−1)+...+1=N(N−1)/2 operations.
Space Complexity: O(N)

這題太難了 = =, 有需要再去 leetcode 看 (觀念我已經大致看過了)

Input: n = 3, k = 3
Output: "213"
123
132
213 => 3
231
213
321
"""

if __name__ == '__main__':
    demo = Solution()
    n, k = 3, 3
    n2, k2 = 4, 9

    print(demo.getPermutation(n, k))
    print(demo.getPermutation(n2, k2))
