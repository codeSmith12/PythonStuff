class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # sliced = " ".join(s.split())
        leftSliced = s.strip()
        # print("\'"+ leftSliced+ "\'")
        newStr = ""
        for i in range(len(leftSliced)-1,0,-1):
            if leftSliced[i] == ' ':
                return len(newStr[::-1])
            else:
                newStr = newStr + s[i]
s = Solution()
print(s.lengthOfLastWord("   fly me   to   the moon  "))
