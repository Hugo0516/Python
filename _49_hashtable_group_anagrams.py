from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solution = {}
        if len(strs) < 1:
            return strs
        else:
            for i in range(len(strs)):
                reg = strs[i]
                regsort = "".join(sorted(reg))
                if regsort in solution:
                    solution[regsort].append(reg)
                else:
                    solution[regsort] = [reg]
        return solution.values()

"""
    https://www.youtube.com/watch?v=BHC0vgpsl5k
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    output_1 = demo.groupAnagrams(input_1)
    print(output_1)
