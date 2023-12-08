from typing import List
class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        newWords = []
        for word in words:
            newWords.append(word.split("."))
        
        for word in newWords:
            if len(word) == 0:
                newWords.remove(word)
        return newWords

words = ["one.two.three","four.five","six"]
separator = "."
s = Solution()
s.splitWordsBySeparator(words, separator)