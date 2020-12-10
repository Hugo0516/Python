from typing import List


class Solution:

    # Hua Hua version
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.helper(nums, 0, len(nums), [], [])

    def helper(self, nums: List, degree: int, n: int, cur: List, res: List):
        if degree == n:
            res.append(cur)

        for i in range(len(nums)):
            if nums[i] in cur:
                continue
            cur.append(nums[i])
            self.helper(nums, degree + 1, n, cur[:], res)
            cur.pop()
        return res

    # Michelle version, use recursion
    def permute2(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]

        answer = []
        for i, num in enumerate(nums):
            n = nums[:i] + nums[i + 1:]
            for y in self.permute2(n):
                answer.append([num] + y)

        return answer

    # backtracking method, leetcode provided
    def permute3(self, nums: List[int]) -> List[List[int]]:
        # 因為要一直 recursion, 所以 first 代表這一回 nums 裡的哪一個數字是起頭
        def backtrack(first=0):
            # if all integers are used up
            if first == n:
                output.append(nums[:])
                return  # 加上這行速度會變快, 因為 prune unused call stack
            for i in range(first, n):
                # place i-th integer first
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        output = []
        backtrack()
        return output


class Solution2(object):
    def permute(self, nums):
        visited = [0] * len(nums)
        res = []

        def dfs(path):
            if len(path) == len(nums):
                res.append(path)
            else:
                for i in range(len(nums)):
                    if not visited[i]:
                        visited[i] = 1
                        dfs(path + [nums[i]])
                        visited[i] = 0  # 這行發揮 backtrack effect !!!

        dfs([])
        return res


"""
    這是自己寫出來的哦 嘻嘻
    可是我覺得還是可以 youtube 一下>,<
    
    Hua Hua 的太不實用
    
    Leetcode 要看圖才會懂
    
    Solution2 比較好理解 <負雪>
    
    Time Complexity: n * n! or n! <look leetcode explaination>
    Space Complexity: n!, since one has to keep n! solutions
    
"""
if __name__ == '__main__':
    demo = Solution()
    input_1 = [1, 2, 3]
    print(demo.permute(input_1))

    print(demo.permute2(input_1))

    print(demo.permute3(input_1))

    demo2 = Solution2()
    print(demo2.permute(input_1))

    print(input_1[:0])
    print(input_1[1:])