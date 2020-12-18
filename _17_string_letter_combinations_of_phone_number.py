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

        d = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]  # Space : 4^n
        cur = [' ' for _ in range(len(digits))]  # Space: n
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
        digit_map = {0: "0", 1: "1", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

        result = [""]
        for digit in digits:
            tmp_list = []
            for ch in digit_map[int(digit)]:
                for str in result:
                    tmp_list.append(str + ch)
            result = tmp_list
        return result


class Solution2:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])

        output = []
        if digits:
            backtrack("", digits)
        return output


"""
    解題思路：
            4 => 每個數字最多可以打出4種不同的數量 / n => 輸入的長度
            DFS: Time Complexity: O(4^n) / Space Complexity: O(4^n + n)
            BFS: Time Complexity: O(4^n) / Space Complexity: O(2 * 4^n)
            https://www.youtube.com/watch?v=fLy8t33M1qQ
            
            非 DFS / BFS 版本：
            
            https://www.youtube.com/watch?v=KAJnbsikSC8
            
2020/ 12/ 18 update
Solution2, backtrack method
Time Complexity: O(3^N * 4^M)
Space Complexity: O(3^N * 4^M)
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = "23"
    print(demo.letterCombinations3(input_1))

    demo2 = Solution2()
    print(demo2.letterCombinations(input_1))
