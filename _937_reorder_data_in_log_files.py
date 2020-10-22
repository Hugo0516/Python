from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)  # maxsplit 要特別注意!
            print(rest[0].isalpha())
            print((0, rest, _id))
            print((1,))
            return (0, rest, _id) if rest[0].isalpha() else (1,)

        return sorted(logs, key=get_key)
        # 這裡的 key, 用tuple 來維持, 我們可知如果是字串類的優限度為 (0, rest, _id), 數字類的為 (1, None, None)
        # 所以現在 (0, rest, _id), (1, None, None) 要開始互相比較
        # 由於字串的第一格 tuple = 0, 0 小於 數字類的 1, 所以字串類一定會比數字類前面
        # 接下來再字串類內鬥, 看 rest 所以 rest 越小的優先度越高(即 a 開頭的優先度 > z 開頭的)


"""
    Input: logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
    
    Constraints:
    0 <= logs.length <= 100
    3 <= logs[i].length <= 100
    
    logs[i] is guaranteed to have an identifier, and a word after the identifier.
    
    Let N be the number of logs in the list and M be the maximum length of a single log.
    Time Complexity: O(M⋅N⋅logN)
    
    The sorted() in Python is implemented with the Timsort algorithm whose time complexity is O(N⋅logN).
    Since the keys of the elements are basically the logs itself, the comparison between two keys can take up to O(M) time.
    Therefore, the overall time complexity of the algorithm is O(M⋅N⋅logN).
    
    Space Complexity: O(M⋅N) (背 !!!!!!!!!!!)
    
    First, we need O(M⋅N) space to keep the keys for the log.
    In addition, the worst space complexity of the Timsort algorithm is O(N), 
    assuming that the space for each element is O(1). 
    Hence we would need O(M⋅N) space to hold the intermediate values for sorting.

    In total, the overall space complexity of the algorithm is O(M⋅N+M⋅N)=O(M⋅N).
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    print(demo.reorderLogFiles(input_1))
