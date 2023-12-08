class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            pass
            return haystack.find(needle)
        else:
            return -1
s = Solution()
print(s.strStr("sadbutsad", "sad"))