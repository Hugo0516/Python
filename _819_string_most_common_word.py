from collections import defaultdict
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_words = set(banned)  # 我試過, 這一句不需要
        ans = ""
        max_count = 0
        word_count = defaultdict(int)
        word_buffer = []

        for p, char in enumerate(paragraph):
            # 1). consume the characters in a word
            if char.isalnum():
                word_buffer.append(char.lower())
                if p != len(paragraph) - 1:
                    continue

            # 2). at the end of one word or at the end of paragraph
            if len(word_buffer) > 0:
                word = "".join(word_buffer)
                if word not in banned_words:  # 這裡其實直接用 banned 也可
                    word_count[word] += 1
                    if word_count[word] > max_count:
                        max_count = word_count[word]
                        ans = word
                # reset the buffer for the next word
                word_buffer = []

        return ans


"""
    Input:
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    Output: "ball"
    
    Time Complexity: O(N+M). => 這裡+M, 是因為 set() function 會花 O(M) time, 即 banned 長度
    但是我認為題目沒特別說 banned 李會有重複的字, 所以我覺得可以不用用到 set() function.

    It would take O(N) time to process each stage of the pipeline as we built.
    In addition, we built a set out of the list of banned words, which would take O(M) time.
    Hence, the overall time complexity of the algorithm is O(N+M).
    
    Space Complexity: O(N+M).
    
    We built a hashmap to count the frequency of each unique word, whose space would be of O(N).
    Similarly, we built a set out of the banned word list, which would consume additional O(M) space.
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ['hit']
    demo.mostCommonWord(input_1, banned)
