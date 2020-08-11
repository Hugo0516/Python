from typing import List


class Solution:
    # def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    #     n = len(nums)
    #     res = []
    #     nums.sort()
    #     for i in range(n - 3):
    #         if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > 0:
    #             break
    #         if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < 0:
    #             continue
    #         if 1 < i and nums[i] == nums[i - 1] == nums[i -2]:
    #             continue  # 可能全部是0 , 或是找不到任何解法
    #
    #         l, r = i + 2, n - 1  # 這裡是用左右兩邊往中間靠攏的方式，為什麼呢？
    #         # 聽影片是說如果我們按造以前固定左邊然後持續便利到最右邊的話時間複雜度是n^2
    #         # 兩頭往中間找的話，可以減少我們的時間複雜度(或是說intuition time)
    #
    #         while l < r:
    #             tmp = nums[i] + nums[i + 1] + nums[l] + nums[r]
    #             if tmp == 0:
    #                 res.append([nums[i], nums[i + 1], nums[l], nums[r]])
    #                 while l + 1 < r and nums[l] == nums[l + 1]:  # 左邊的推到更右邊
    #                     l += 1
    #                 l += 1  # 更新數字，這樣下次跑while loop 就會是全新的數字惹
    #                 while l < r - 1 and nums[r] == nums[r - 1]:  # 右邊的推到更左邊
    #                     r -= 1
    #                 r -= 1
    #             elif tmp < 0:  # 左邊數字佔的比重太高 or 太小了
    #                 l += 1
    #             else:  # 右邊數字佔的比重太高 or 太小了 (because tmp > 0)
    #                 r -= 1
    #     return res

    # hashtable method
    def fourSum2(self, num: List[int], target: int) -> List[List[int]]:
        numLen, res, dict = len(num), set(), {}
        if numLen < 4:
            return []
        num.sort()
        for p in range(numLen):
            for q in range(p + 1, numLen):
                if num[p] + num[q] not in dict:
                    dict[num[p] + num[q]] = [(p, q)]
                else:
                    dict[num[p] + num[q]].append((p, q))
        for i in range(numLen):
            for j in range(i + 1, numLen - 2):
                T = target - num[i] - num[j]
                if T in dict:
                    for k in dict[T]:
                        if k[0] > j: res.add((num[i], num[j], num[k[0]], num[k[1]]))
        return [list(i) for i in res]


"""
    解題思路：
            -2 -1 0 0 1 2
            -2 -1 0     2
            -2 -1   0   2
            -2 -1     0 2
            -2    0 0   2
            -2    0   0 2
            -2      0 0 2
            心得：乾 我原本要用 3sum 的想法下去解( 3sum 是透過左右兩邊同時往中間靠攏的方式來減少遍歷)
                可是 4sum 沒辦法用這方式(如我上圖所畫，如果我用原本的左右兩邊同時夾擠方式，會害我圖下面三行跑不出來)
                所以說 4sum 只能用傳統方式：固定 前兩個和後一個 如圖下三行，然後想辦法跑出來
                So => 第一個失敗！！！！！
                
            需要用到哈希表的思路，這樣可以空間換時間，以增加空間複雜度的代價來降低時間複雜度。
            首先建立一個字典dict，字典的key值為數組中每兩個元素的和，每個key對應的value為這兩個元素的下標組成的元組，元組不一定是唯一的。
            如對於num=[1,2,3,2]來說，dict={3:[(0,1),(0,3)], 4:[(0,2),(1,3)] , 5:[(1,2),(2,3)]}。
            這樣就可以檢查target-key這個值在不在dict的key值中，如果target-key在dict中並且下標符合要求，那麼就找到了這樣的一組解。
            由於需要去重，這裡選用set()類型的數據結構，即無序無重複元素集。最後將每個找出來的解(set()類型)轉換成list類型輸出即可。
            https://www.cnblogs.com/zuoyuan/p/3699384.html
            
            Time Complexity: O(n^3) / Space Complexity:O(n)
            複雜度參考：
            https://www.youtube.com/watch?v=YkxsyPItHeM
                
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [1, 0, -1, 0, -2, 2]
    # [-2, -1, 0, 0, 1, 2]
    print(demo.fourSum2(input_1, 0))
