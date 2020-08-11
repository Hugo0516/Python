from typing import List


# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""
#
#         for i in range(len(strs[0])):
#             for string in strs[1:]:
#                 if i >= len(string) or string[i] != strs[0][i]:
#                     return strs[0][:i]
#
#         return strs[0]  # 若是沒有這一行會 error

"""
    解題思路：
            跟樓下圖個影片
            line 11: i>=len(string): 像是 flower 比 flow 長，所以會 out of range會有error
            i >= len 在那一行一定要先判斷，要是or前後對調，就會有 error
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        i = 0

        while True:
            try:
                sets = set(string[i] for string in strs)  # 利用set的特性，因為set裡面不會有重複的東西，相同的只會保留一個
                if len(sets) == 1:  # if > 1 表示 有兩個不同數字在set
                    result += sets.pop()
                    i += 1
                # print('sets', sets)
                else:
                    break
            except Exception as e:
                break

        return result


"""
    解題思路：
            這個方法比較快
            高端寫法 ！！！！ 徹底想到set的性質
            Time Complexity: O(n) / Space Complexity: O(1) (我自己想ㄉ，待確認)
            https://www.youtube.com/watch?v=cGQez9SiScw
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = ["flower", "flow", "flight"]
    print(demo.longestCommonPrefix(input_1))
