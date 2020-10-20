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

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        # Input: strs = ["eat","tea","tan","ate","nat","bat"]
        # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

        dict_1 = {}
        ans = []

        if strs is None:
            ans.append('')
            return ans
        else:
            for item in strs:
                item_2 = sorted(item)  # item_2 's type is List, I assume it would be str, however I am wrong!!!!
                # ['a', 'e', 't']
                print(type(item_2), type(item))

                item_2 = ''.join(item_2)
                # print(type(item_2))     # 這樣就可以變成 str type

                if item_2 in dict_1:
                    dict_1[item_2].append(item)
                else:
                    dict_1[item_2] = [item]
                # item = strs[i]
                # item_2 = sorted(item)
                # print(type(item_2))
        ans.append(dict_1.values())
        return ans


"""
    一個東西要可以用 sort, 其本身一定要是有序的, str這一種 type 本身就是無序的, 所以你強迫用 sorted(), 會把它轉型成 int 型態
    如果被強變成 int 型態, 那就要用 join 再把它聯起來!!!!!!

    https://www.youtube.com/watch?v=BHC0vgpsl5k
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    output_1 = demo.groupAnagrams(input_1)
    print(output_1)

    output_2 = demo.groupAnagrams2(input_1)
    print(output_2)
