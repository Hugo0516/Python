import collections
import string
from collections import deque
from typing import List


class Solution:
    # BFS method
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordDict = set(wordList)
        if endWord not in wordDict:
            return 0

        l = len(beginWord)
        steps = {beginWord: 1}
        q = deque([beginWord])
        while len(q) > 0:
            word = q.popleft()
            step = steps[word]
            for i in range(l):
                c = word[i]
                for t in string.ascii_lowercase:
                    if c == t:
                        continue
                    new_word = word[:i] + t + word[i + 1:]
                    if new_word == endWord:
                        return step + 1
                    if new_word not in wordDict:
                        continue
                    wordDict.remove(new_word)
                    steps[new_word] = step + 1
                    q.append(new_word)

        return 0

    # Bidirectional BFS
    def ladderLength2(self, beginWord, endWord, wordList):
        wordDict = set(wordList)
        if endWord not in wordDict:
            return 0

        l = len(beginWord)
        s1 = {beginWord}
        s2 = {endWord}
        wordDict.remove(endWord)
        step = 0
        while len(s1) > 0 and len(s2) > 0:
            step += 1
            if len(s1) > len(s2):  # 調換的原因是因為,我們希望底下的for 迴圈裡的s1, 可以是最小的 => 減少 loop 次數
                s1, s2 = s2, s1  # 算是一個小技巧

            s = set()
            for w in s1:
                new_words = [
                    w[:i] + t + w[i + 1:] for t in string.ascii_lowercase for i in range(l)]
                # (t, i) => a,0 => a,1 => a,2 => b,0 => b,1 => b.2 ==> ait, hat, hia / bit, hbt, hib
                for new_word in new_words:
                    if new_word in s2:
                        return step + 1
                    if new_word not in wordDict:
                        continue
                    wordDict.remove(new_word)
                    s.add(new_word)
            s1 = s

        return 0


from collections import defaultdict


class Solution2(object):
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i + 1:]].append(word)

        # Queue for BFS
        queue = collections.deque([(beginWord, 1)])
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i + 1:]

                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0


"""
    We will essentially be working with an undirected and unweighted graph with words as nodes 
    and edges between words which differ by just one letter. 
    The problem boils down to finding the shortest path from a start node to a destination node, 
    if there exists one. Hence it can be solved using Breadth First Search approach.
    
    Time Complexity: O(n*26^l)<BFS VERSION> -> O(n*26^l/2)<Bidirectional BFS>, l = len(word), n=|wordList|
    Space Complexity: O(n)
    
    http://zxi.mytechroad.com/blog/searching/127-word-ladder/
"""
if __name__ == '__main__':
    demo = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["ait", "bit", "hot", "dot", "dog", "lot", "log", "cog"]
    print(demo.ladderLength2(beginWord, endWord, wordList))

    demo2 = Solution2()
    print(demo2.ladderLength(beginWord, endWord, wordList))
