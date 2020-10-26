class Solution:
    # def trap(self, height: List[int]) -> int:
    #     left = 0
    #     right = len(height) - 1
    #     res = 0
    #     left_max = 0
    #     right_max = len(height) - 1
    #
    #     while left < right:
    #         if height[left] > height[right]:
    #             if height[right_max] < height[right]:
    #                 right_max = right
    #                 right = right - 1
    #             else:
    #                 res += height[right_max] - height[right]
    #                 right = right - 1
    #
    #         if height[left] <= height[right]:
    #             if height[left_max] < height[left]:
    #                 left_max = left
    #                 left = left + 1
    #             else:
    #                 res += height[left_max] - height[left]
    #                 left = left + 1
    #     return res

    def trap(self, height):

        if not height: return 0
        left_max = right_max = res = 0
        left, right = 0, len(height) - 1

        while left < right:
            if height[left] < height[right]:  # 左指針操作
                if height[left] < left_max:
                    res += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1  # 移動左指針
            else:
                if height[right] < right_max:  # 右指針操作
                    res += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1  # 移動右指針
        return res

    def trap3(self, height):
        n = len(height)
        if n == 0:
            return 0
        l, r = 0, n - 1
        max_l, max_r = height[l], height[r]
        ans = 0
        while l < r:
            if max_l < max_r:
                ans += (max_l - height[l])
                l += 1
                max_l = max(max_l, height[l])
            else:
                ans += (max_r - height[r])
                r -= 1
                max_r = max(max_r, height[r])
        return ans


"""
    方法二，使用雙指針法，在左右兩端分別設置指針left, right，並且用left_max， right_max記錄走過之後的最長最高的邊。
    例如， left_max就是指針left左邊最長的線，right_max同理。
    （1）如果 height[left] < height[right]，就是左指針指向的數字<右指針指向的數字（現在操作左指針）,
    說明此時，左邊已經走過的位置都小於height[right]，通俗的講，現在left指針位置的左右兩邊桶的短板，一定存在於左邊，
    又因為left_max記錄了當前left位置的左邊最高的那個邊，所以當前left位置的容量就是只需考慮left_max ， height[ left]這個兩個值的大小即可得出。

     問題：為什麼說左邊已經走過的位置都小於height[right]？因為兩個指針的移動條件是，那個指針小就移動那一個。

    （2）如果height[left] >= height[right]，同理（1）。直到兩個指針相遇。
    
    https://blog.csdn.net/XX_123_1_RJ/java/article/details/81048041
    
    這題有 DP 解法 注意一下
    
    trap3 => HuaHua solution
"""

if __name__ == '__main__':
    input_1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    demo = Solution()
    # print(demo.trap(input_1))

    print(demo.trap3(input_1))
