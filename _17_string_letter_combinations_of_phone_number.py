class Solution:
    # DFS
    def letterCombinations(self, digits):
        def dfs(digits, d, l, cur, ans):
            if l == len(digits):
                if l > 0: ans.append("".join(cur))
                return

            for c in d[ord(digits[l]) - ord('0')]:  # Time: 4^n
                cur[l] = c
                dfs(digits, d, l + 1, cur, ans)

        d = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]     # Space : 4^n
        cur = [' ' for _ in range(len(digits))]     # Space: n
        ans = []
        dfs(digits, d, 0, cur, ans)
        return ans

    # BFS
    def letterCombinations2(self, digits):
        if not digits: return []
        d = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = [""]
        for digit in digits:
            tmp = []
            for s in ans:
                for c in d[ord(digit) - ord('0')]:
                    tmp.append(s + c)
            ans = tmp

        return ans

    # 非 DFS or BFS 版本
    def letterCombinations3(self, digits):
        if len(digits) == 0:
            return []
        digit_map = {0: "0", 1: "1", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9:"wxyz"}

        result = [""]
        for digit in digits:
            tmp_list = []
            for ch in digit_map[int(digit)]:
                for str in result:
                    tmp_list.append(str + ch)
            result = tmp_list
        return result

"""
    解題思路：
            4 => 每個數字最多可以打出4種不同的數量 / n => 輸入的長度
            DFS: Time Complexity: O(4^n) / Space Complexity: O(4^n + n)
            BFS: Time Complexity: O(4^n) / Space Complexity: O(2 * 4^n)
            https://www.youtube.com/watch?v=fLy8t33M1qQ
            
            非 DFS / BFS 版本：
            
            https://www.youtube.com/watch?v=KAJnbsikSC8
            
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = "23"
    print(demo.letterCombinations3(input_1))
