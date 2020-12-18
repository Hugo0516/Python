import collections


class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        n = len(nums)
        if n * k == 0:
            return []

        return [max(nums[i:i + k]) for i in range(n - k + 1)]


class Solution2:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        left = [0] * n
        left[0] = nums[0]
        right = [0] * n
        right[n - 1] = nums[n - 1]
        for i in range(1, n):
            # from left to right
            if i % k == 0:
                # block start
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])
            # from right to left
            j = n - i - 1
            if (j + 1) % k == 0:
                # block end
                right[j] = nums[j]
            else:
                right[j] = max(right[j + 1], nums[j])

        output = []
        for i in range(n - k + 1):
            output.append(max(left[i + k - 1], right[i]))

        return output


class Solution3(object):
    def maxSlidingWindow(self, nums, k):
        que = collections.deque()  # [[i, num]]
        res = []
        for i, num in enumerate(nums):
            # x, y, z = que, i - que[0][0], que[-1][1]
            if que and i - que[0][0] >= k:
                que.popleft()
            while que and que[-1][1] <= num:
                que.pop()
            que.append([i, num])
            if i >= k - 1:
                res.append(que[0][1])
        return res


class Solution4:
    def maxSlidingWindow(self, nums, k):
        indices = collections.deque()
        ans = []
        for i in range(len(nums)):
            while indices and nums[i] >= nums[indices[-1]]:
                indices.pop()
            indices.append(i)
            if i >= k - 1:
                # pop the max element
                ans.append(nums[indices[0]])
            if i - k + 1 == indices[0]:
                # 這裡是為了可以讓我們的 indices 保持在 k 個數字
                indices.popleft()
        return ans

    # 這裡的 monotonic queue 特性
    # push an element on the queue
    # void push(int e)
    # will pop all elements smaller than e
    # void pop()

"""

Approach 1: Brute force
Time Complexity: O(Nk), where N is number of elements in the array.
Space Complexity: O(N-k+1) for an output array.

Approach 2: DP
Time Complexity: O(N), since all we do is 3 passes along the array of length N.
Space Complexity: O(N) to keep left and right arrays of length N, and output array of length N - k + 1.

Approach 3: Deque
Time Complexity: O(N), since each element is processed exactly twice - it's index added and then removed from the deque.
Space Complexity: O(N) since O(N−k+1) is used for an output array and O(k) for a deque.

Approach 4: Hua Hua Monotonic deque
Time Complexity: O(N)
Space Complexity: OKk)

*** 第四個是我理解的 ***
可以和 480 比較 
"""
if __name__ == '__main__':
    demo = Solution()
    demo2 = Solution2()
    demo3 = Solution3()
    demo4 = Solution4()

    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(demo.maxSlidingWindow(nums, k))
    print(demo2.maxSlidingWindow(nums, k))
    print(demo3.maxSlidingWindow(nums, k))
    print(demo4.maxSlidingWindow(nums, k))
