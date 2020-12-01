from typing import List


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        seen = {}
        dry = []
        res = []
        for i in range(len(rains)):
            if rains[i] != 0:
                if rains[i] not in seen:
                    res.append(-1)
                    seen[rains[i]] = i
                else:
                    if not dry or dry[-1] < seen[rains[i]]:
                        return None
                    else:
                        for j in dry:
                            if j > seen[rains[i]]:
                                res[j] = rains[i]
                                seen[rains[i]] = i
                                dry.remove(j)
                                res.append(-1)
                                break
            else:
                res.append(1)
                dry.append(i)
        return res


"""
    Reference:
    https://leetcode.com/problems/avoid-flood-in-the-city/discuss/701964/python-using-dictionary
    
    這題尚未研究 = =
    
"""

demo = Solution()
input_1 = [1, 2, 3, 4]
input_2 = [1, 2, 0, 0, 2, 1]
input_3 = [1, 2, 0, 1, 2]

print(demo.avoidFlood(input_1), demo.avoidFlood(input_2), demo.avoidFlood(input_3), end=' ')
