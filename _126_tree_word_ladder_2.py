import collections
import string
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        wordSet = set(wordList)  # faster checks against dictionary
        layer = {beginWord: [[beginWord]]}

        while layer:
            newlayer = collections.defaultdict(list)  # returns [] on missing keys, just to simplify code
            for word in layer:
                if word == endWord:
                    return layer[word]  # return all found sequences
                for i in range(len(word)):  # change every possible letter and check if it's in dictionary
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:i] + c + word[i + 1:]
                        if newWord in wordSet:
                            newlayer[newWord] += [j + [newWord] for j in layer[word]]  # add new word to all sequences and form new layer element
                            # 23行要注意, [newWord] 要放後面, 不然的畫順序會剛好相反
            wordSet -= set(newlayer.keys())  # remove from dictionary to prevent loops
            layer = newlayer  # move down to new layer

        return []

    def findLadders2(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordLen = len(beginWord)
        front, back = collections.defaultdict(list), collections.defaultdict(list)
        front[beginWord].append([beginWord])
        back[endWord].append([endWord])
        # remove start from dict, add end to dict if it is not there
        wordList.discard(beginWord)
        if endWord not in wordList:
            wordList.add(endWord)
        forward, result = True, []
        while front:
            # get all valid transformations
            nextSet = collections.defaultdict(list)
            for word, paths in front.items():
                for index in range(wordLen):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        nextWord = word[:index] + ch + word[index + 1:]
                        if nextWord in wordList:
                            # update paths
                            if forward:
                                # append next word to path
                                nextSet[nextWord].extend([path + [nextWord] for path in paths])
                            else:
                                # add next word in front of path
                                nextSet[nextWord].extend([[nextWord] + path for path in paths])
            front = nextSet
            common = set(front) & set(back)
            if common:
                # path is through
                if not forward:
                    # switch front and back if we were searching backward
                    front, back = back, front
                result.extend([head + tail[1:] for word in common for head in front[word] for tail in back[word]])
                return result

            if len(front) > len(back):
                # swap front and back for better performance (smaller nextSet)
                front, back, forward = back, front, not forward

            # remove transformations from wordDict to avoid cycles
            wordList -= set(front)

        return []

    def findLadders3(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        word_set = set(wordList)
        layer_dict = {beginWord: [[beginWord]]}

        while layer_dict:
            new_layer = collections.defaultdict(list)

            for item in layer_dict:
                if item == endWord:
                    return layer_dict[item]
                for n in range(len(beginWord)):
                    new_word = [item[:n] + x + item[n + 1:] for x in string.ascii_lowercase]
                    for new_word2 in new_word:
                        if new_word2 in word_set:
                            new_layer[new_word2] += [[new_word2] + old_word for old_word in layer_dict[item]]

        word_set -= set(new_layer.keys())
        layer_dict = new_layer

        return []


'''
    Input:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    
    Output:
    [
      ["hit","hot","dot","dog","cog"],
      ["hit","hot","lot","log","cog"]
    ]
    
    這一題 Bidirectional BFS is too hard, 所以會 BFS 即可, 
    然後面試官問如何優化時, 再回答有 Bidirectional 即可,
    阿 會不會叫你寫出優化版本, 看情況
    
    method1:
    https://leetcode.com/problems/word-ladder-ii/discuss/40482/Python-simple-BFS-layer-by-layerhttps://leetcode.com/problems/word-ladder-ii/discuss/40482/Python-simple-BFS-layer-by-layer
    
    Time Complexity: O(n*26^l) -> O(n*26^l/2), l = len(word), n=|wordList|
    
    Space Complexity: O(n + k*p), k = number of path, p = path length
    
    Hua Hua:
    https://zxi.mytechroad.com/blog/searching/127-word-ladder/
'''

if __name__ == '__main__':
    demo = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["qit", "hiz", "hot", "dot", "dog", "lot", "log", "cog"]

    print(demo.findLadders(beginWord, endWord, wordList))
