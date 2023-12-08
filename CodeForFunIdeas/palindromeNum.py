class Solution:
    def isPalindrome(self, x: int) -> bool:
        numList = [int(x) for x in str(x)]
        if len(numList) == 1:
            return True
        for i in range(len(numList)):
            if numList[i] != numList[len(numList)-i-1]:
                return False
        return True
        
solution = Solution()
print(solution.isPalindrome(1551))

