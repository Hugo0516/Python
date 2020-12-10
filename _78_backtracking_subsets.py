from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]

        for num in nums:
            output += [curr + [num] for curr in output]

        return output


class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0, curr=[]):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
                return  # 乾 一定要加這一行, 不然速度會被拖垮
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()

        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output


class Solution3:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []

        for i in range(2 ** n, 2 ** (n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]

            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])

        return output


"""
Approach 1: Cascading

Time Complexity: O( N * 2^N ) to generate all subsets and then copy them into output list.
Space Complexity: O( N * 2^N ) to keep all the subsets of length N, since each of N elements could be present or absent.
For a given number, it could be present or absent (i.e. binary choice) in a subset solution. 
As as result, for N numbers, we would have in total 2^N choices (solutions). 

Approach 2: Backtracking

Time Complexity: O( N * 2^N ) to generate all subsets and then copy them into output list.
Space Complexity: O( N * 2^N ) to keep all the subsets of length N, since each of N elements could be present or absent. 

Approach 3: Lexicographic (Binary Sorted) Subsets

Time Complexity: O( N * 2^N ) to generate all subsets and then copy them into output list.
Space Complexity: O( N * 2^N ) to keep all the subsets of length N, since each of N elements could be present or absent.

********  Approach 3 is unique and simple, plz recognize it!!!!!!!!1  ********

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [1, 2, 3]
    print(demo.subsets(input_1))

    demo2 = Solution2()
    demo3 = Solution3()

    print(demo2.subsets(input_1))
    print(demo3.subsets(input_1))

    print(bin(9))
